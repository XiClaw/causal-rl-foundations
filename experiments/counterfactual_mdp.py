"""
Counterfactual Reasoning in Simple MDPs
=========================================
Demonstrates how counterfactual reasoning can improve credit assignment
in reinforcement learning.

Scenario: A 3-state MDP where an agent must navigate to a goal.
We ask: "What would have happened if the agent had taken a different action
at step t?"

This is a toy implementation of the three-step counterfactual procedure:
    1. Abduction: infer latent noise from observed trajectory
    2. Action: modify the structural equations (take counterfactual action)
    3. Prediction: propagate through the modified SCM

Requirements: numpy, matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from typing import List, Tuple, Dict, Optional
from dataclasses import dataclass

np.random.seed(0)


# ─── MDP Definition ──────────────────────────────────────────────────────────

@dataclass
class Transition:
    state: int
    action: int
    next_state: int
    reward: float
    noise: float  # the exogenous noise variable U


class SimpleMDP:
    """
    A 5-state linear MDP:
        States: 0, 1, 2, 3, 4 (4 is the goal)
        Actions: 0 = left, 1 = right
        Transition: stochastic — action succeeds with prob (1 - noise)

    Structural equation for next state:
        S_{t+1} = f(S_t, A_t, U_t)
        where U_t ~ Uniform(0, 1) is the exogenous noise

        If A_t = 1 (right) and U_t < 0.8: S_{t+1} = min(S_t + 1, 4)
        If A_t = 1 (right) and U_t >= 0.8: S_{t+1} = max(S_t - 1, 0)  (slip)
        If A_t = 0 (left): symmetric, with success prob 0.8
    """

    n_states = 5
    n_actions = 2
    goal = 4
    success_prob = 0.8

    def transition(self, state: int, action: int, noise: float) -> Tuple[int, float]:
        """Structural equation for transition."""
        if action == 1:  # right
            if noise < self.success_prob:
                next_state = min(state + 1, self.n_states - 1)
            else:
                next_state = max(state - 1, 0)
        else:  # left
            if noise < self.success_prob:
                next_state = max(state - 1, 0)
            else:
                next_state = min(state + 1, self.n_states - 1)

        reward = 1.0 if next_state == self.goal else 0.0
        return next_state, reward

    def sample_transition(self, state: int, action: int) -> Transition:
        """Sample a transition with explicit noise variable."""
        noise = np.random.uniform(0, 1)
        next_state, reward = self.transition(state, action, noise)
        return Transition(state, action, next_state, reward, noise)


# ─── Counterfactual Reasoning ─────────────────────────────────────────────────

class CounterfactualReasoner:
    """
    Implements Pearl's three-step counterfactual procedure for the MDP.

    Given an observed trajectory (the factual world), ask:
    "What would have happened if action a_t had been a'_t instead?"
    """

    def __init__(self, mdp: SimpleMDP):
        self.mdp = mdp

    def factual_trajectory(self, start: int, policy: List[int]) -> List[Transition]:
        """
        Simulate a factual trajectory under a given policy.
        Saves all noise variables (U_t) — these are needed for counterfactuals.
        """
        trajectory = []
        state = start
        for action in policy:
            t = self.mdp.sample_transition(state, action)
            trajectory.append(t)
            state = t.next_state
        return trajectory

    def counterfactual_trajectory(
        self,
        factual: List[Transition],
        cf_action_at: int,
        cf_action: int
    ) -> List[Transition]:
        """
        Compute the counterfactual trajectory:
        "What if at step cf_action_at we had taken cf_action instead?"

        Step 1 (Abduction): already done — we have the noise variables from factual
        Step 2 (Action): replace action at step cf_action_at
        Step 3 (Prediction): propagate forward using the SAME noise variables

        This captures the key insight: the counterfactual world shares the same
        "background conditions" (noise) as the factual world.
        """
        cf_trajectory = []

        # Replay the trajectory with the same noise, but different action at cf_action_at
        state = factual[0].state

        for t, trans in enumerate(factual):
            action = cf_action if t == cf_action_at else trans.action
            noise = trans.noise  # SAME noise as factual (abduction step)
            next_state, reward = self.mdp.transition(state, action, noise)
            cf_trajectory.append(Transition(state, action, next_state, reward, noise))
            state = next_state

        return cf_trajectory

    def counterfactual_reward_gain(
        self,
        factual: List[Transition],
        cf_action_at: int,
        cf_action: int
    ) -> float:
        """
        Counterfactual credit: how much more reward would have been obtained
        if we had taken cf_action at step cf_action_at?
        """
        cf = self.counterfactual_trajectory(factual, cf_action_at, cf_action)
        factual_reward = sum(t.reward for t in factual)
        cf_reward = sum(t.reward for t in cf)
        return cf_reward - factual_reward


# ─── Counterfactual Policy Gradient ──────────────────────────────────────────

class CounterfactualPolicyGradient:
    """
    A policy gradient agent that uses counterfactual baselines for variance reduction.

    Standard policy gradient:
        ∇J(θ) ≈ E[ ∇log π(a|s) * R ]

    With counterfactual baseline:
        ∇J(θ) ≈ E[ ∇log π(a|s) * (R - b_CF(s,a)) ]

    where b_CF(s,a) = E[R | do(A≠a)] — the counterfactual baseline.
    """

    def __init__(self, n_states: int, n_actions: int, lr: float = 0.05):
        # Tabular softmax policy
        self.logits = np.zeros((n_states, n_actions))
        self.lr = lr

    def policy(self, state: int) -> np.ndarray:
        """Softmax policy."""
        logits = self.logits[state] - np.max(self.logits[state])
        exp_logits = np.exp(logits)
        return exp_logits / exp_logits.sum()

    def choose_action(self, state: int) -> int:
        probs = self.policy(state)
        return int(np.random.choice(len(probs), p=probs))

    def update(self, trajectory: List[Transition], cf_rewards: Dict[Tuple[int,int], float]):
        """
        Update policy using counterfactual advantage.
        cf_rewards[(t, a')] = counterfactual total reward if action a' had been taken at step t
        """
        total_reward = sum(t.reward for t in trajectory)

        for t_idx, trans in enumerate(trajectory):
            state = trans.state
            action = trans.action
            probs = self.policy(state)

            # Counterfactual baseline: average reward under other actions
            other_actions = [a for a in range(len(probs)) if a != action]
            if other_actions:
                cf_baseline = np.mean([
                    cf_rewards.get((t_idx, a), 0.0) for a in other_actions
                ])
            else:
                cf_baseline = 0.0

            advantage = total_reward - cf_baseline

            # Policy gradient update
            for a in range(len(probs)):
                if a == action:
                    self.logits[state, a] += self.lr * advantage * (1 - probs[a])
                else:
                    self.logits[state, a] -= self.lr * advantage * probs[a]


# ─── Training Loop ────────────────────────────────────────────────────────────

def train(n_episodes: int = 500) -> Dict:
    mdp = SimpleMDP()
    reasoner = CounterfactualReasoner(mdp)

    # Two agents: standard PG and counterfactual PG
    standard_agent = CounterfactualPolicyGradient(mdp.n_states, mdp.n_actions, lr=0.05)
    cf_agent = CounterfactualPolicyGradient(mdp.n_states, mdp.n_actions, lr=0.05)

    standard_rewards = []
    cf_rewards_history = []

    for episode in range(n_episodes):
        start_state = 0
        max_steps = 8
        gamma = 0.95

        # --- Standard Policy Gradient ---
        std_trajectory = []
        state = start_state
        for _ in range(max_steps):
            action = standard_agent.choose_action(state)
            trans = mdp.sample_transition(state, action)
            std_trajectory.append(trans)
            state = trans.next_state
            if state == mdp.goal:
                break

        std_total = sum(t.reward * (gamma ** i) for i, t in enumerate(std_trajectory))

        # Simple REINFORCE update (no counterfactual baseline)
        for i, trans in enumerate(std_trajectory):
            probs = standard_agent.policy(trans.state)
            a = trans.action
            for aa in range(mdp.n_actions):
                grad = (1 - probs[aa]) if aa == a else (-probs[aa])
                standard_agent.logits[trans.state, aa] += standard_agent.lr * std_total * grad

        standard_rewards.append(std_total)

        # --- Counterfactual Policy Gradient ---
        cf_traj = []
        state = start_state
        for _ in range(max_steps):
            action = cf_agent.choose_action(state)
            trans = mdp.sample_transition(state, action)
            cf_traj.append(trans)
            state = trans.next_state
            if state == mdp.goal:
                break

        # Compute counterfactual rewards for each (step, alternative_action) pair
        cf_reward_dict = {}
        for t_idx in range(len(cf_traj)):
            for alt_action in range(mdp.n_actions):
                if alt_action != cf_traj[t_idx].action:
                    cf_traj_alt = reasoner.counterfactual_trajectory(
                        cf_traj, t_idx, alt_action
                    )
                    cf_total = sum(
                        t.reward * (gamma ** i) for i, t in enumerate(cf_traj_alt)
                    )
                    cf_reward_dict[(t_idx, alt_action)] = cf_total

        cf_agent.update(cf_traj, cf_reward_dict)
        cf_total_reward = sum(t.reward * (gamma ** i) for i, t in enumerate(cf_traj))
        cf_rewards_history.append(cf_total_reward)

    return {
        "standard": standard_rewards,
        "counterfactual": cf_rewards_history,
        "cf_agent": cf_agent,
        "standard_agent": standard_agent,
    }


def plot_training(results: Dict):
    def smooth(x, w=30):
        return np.convolve(x, np.ones(w)/w, mode='valid')

    std = smooth(results["standard"])
    cf = smooth(results["counterfactual"])

    plt.figure(figsize=(10, 5))
    plt.plot(std, label="Standard Policy Gradient", alpha=0.8, linewidth=2)
    plt.plot(cf, label="Counterfactual Policy Gradient", alpha=0.8, linewidth=2)
    plt.xlabel("Episode")
    plt.ylabel("Smoothed discounted reward")
    plt.title("Counterfactual Reasoning in MDPs\n"
              "Counterfactual baseline reduces variance and speeds up learning")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("counterfactual_mdp.png", dpi=150)
    plt.show()
    print("Plot saved to counterfactual_mdp.png")


def print_policy(agent: CounterfactualPolicyGradient, name: str):
    print(f"\n{name} — Learned Policy (probability of going RIGHT):")
    for s in range(5):
        probs = agent.policy(s)
        bar = "█" * int(probs[1] * 20)
        marker = " ← GOAL" if s == 4 else ""
        print(f"  State {s}: {probs[1]:.2f} {bar}{marker}")


if __name__ == "__main__":
    print("Training agents...")
    results = train(n_episodes=600)

    print_policy(results["standard_agent"], "Standard PG")
    print_policy(results["cf_agent"], "Counterfactual PG")

    plot_training(results)

    print("\nKey insight:")
    print("  Counterfactual reasoning provides a better baseline for policy gradient.")
    print("  Instead of asking 'was this reward good?', we ask")
    print("  'was this reward better than what would have happened otherwise?'")
    print("  This is the causal question — and it leads to lower variance updates.")
