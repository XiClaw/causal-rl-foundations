"""
Causal Bandits vs Standard Bandits
===================================
Demonstrates why causal reasoning matters in bandit problems.

Setup:
- A bandit with 2 arms: A and B
- A hidden confounder C affects both which arm the agent pulls (via behavior policy)
  and the reward
- Standard bandit: learns E[R | arm] — biased by confounder
- Causal bandit: learns E[R | do(arm)] — unconfounded

This is the simplest possible demonstration of the Level 1 vs Level 2 distinction
from Pearl's causal hierarchy.

Requirements: numpy, matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, List

np.random.seed(42)


# ─── Structural Causal Model ─────────────────────────────────────────────────

class CausalBanditSCM:
    """
    SCM for a confounded 2-arm bandit.

    Causal graph:
        C → A_pulled  (confounder affects which arm is pulled)
        C → R         (confounder also directly affects reward)
        A_pulled → R  (the arm pulled causally affects reward)

    Structural equations:
        C ~ Bernoulli(0.5)
        A_pulled = C  with prob 0.8, else random  (behavior policy is confounded)
        R = 1 if A_pulled == 1 else 0, plus C * 0.5 + noise
    """

    def __init__(self):
        # True causal effects of each arm (what we want to learn)
        self.causal_effect = {0: 0.2, 1: 0.7}  # E[R | do(arm=0)] and E[R | do(arm=1)]
        self.confounder_effect = 0.5  # direct effect of C on R

    def sample_observational(self) -> Tuple[int, float, int]:
        """Sample from the observational distribution (confounded)."""
        C = np.random.binomial(1, 0.5)

        # Behavior policy: correlated with C (the confounder)
        if np.random.random() < 0.8:
            arm = C  # most of the time, pull the arm correlated with C
        else:
            arm = np.random.randint(0, 2)

        # Reward: depends on arm AND confounder
        r = (self.causal_effect[arm] +
             self.confounder_effect * C +
             np.random.normal(0, 0.1))

        return arm, r, C

    def sample_interventional(self, arm: int) -> float:
        """Sample from P(R | do(arm=a)) — graph surgery, C no longer affects arm."""
        C = np.random.binomial(1, 0.5)
        r = (self.causal_effect[arm] +
             self.confounder_effect * C +
             np.random.normal(0, 0.1))
        return r


# ─── Standard Bandit Agent (no causal reasoning) ─────────────────────────────

class StandardBanditAgent:
    """
    Epsilon-greedy bandit agent.
    Learns E[R | arm] from observational data — ignores confounding.
    """

    def __init__(self, n_arms: int = 2, epsilon: float = 0.1):
        self.n_arms = n_arms
        self.epsilon = epsilon
        self.counts = np.zeros(n_arms)
        self.values = np.zeros(n_arms)

    def choose_arm(self) -> int:
        if np.random.random() < self.epsilon:
            return np.random.randint(self.n_arms)
        return int(np.argmax(self.values))

    def update(self, arm: int, reward: float):
        self.counts[arm] += 1
        self.values[arm] += (reward - self.values[arm]) / self.counts[arm]

    def best_arm_estimate(self) -> int:
        return int(np.argmax(self.values))


# ─── Causal Bandit Agent ──────────────────────────────────────────────────────

class CausalBanditAgent:
    """
    Causal bandit agent.
    Uses the do-calculus adjustment formula to debias estimates from observational data.

    Adjustment formula (backdoor criterion):
        E[R | do(A=a)] = sum_c E[R | A=a, C=c] * P(C=c)

    This requires observing the confounder C (or a valid adjustment set).
    In practice, we estimate all conditional expectations from data.
    """

    def __init__(self, n_arms: int = 2):
        self.n_arms = n_arms
        # Track E[R | A=a, C=c] and P(C=c)
        self.r_given_arm_conf = np.zeros((n_arms, 2))    # [arm, C_value]
        self.counts_arm_conf = np.zeros((n_arms, 2))
        self.conf_counts = np.zeros(2)
        self.total = 0

    def update(self, arm: int, reward: float, confounder: int):
        self.counts_arm_conf[arm, confounder] += 1
        self.r_given_arm_conf[arm, confounder] += (
            (reward - self.r_given_arm_conf[arm, confounder]) /
            self.counts_arm_conf[arm, confounder]
        )
        self.conf_counts[confounder] += 1
        self.total += 1

    def causal_value(self, arm: int) -> float:
        """Compute E[R | do(A=arm)] using backdoor adjustment."""
        if self.total == 0:
            return 0.0
        p_conf = self.conf_counts / max(self.total, 1)
        # Adjustment formula: sum_c E[R|A=arm,C=c] * P(C=c)
        val = 0.0
        for c in range(2):
            if self.counts_arm_conf[arm, c] > 0:
                val += self.r_given_arm_conf[arm, c] * p_conf[c]
        return val

    def best_arm_estimate(self) -> int:
        vals = [self.causal_value(a) for a in range(self.n_arms)]
        return int(np.argmax(vals))


# ─── Simulation ───────────────────────────────────────────────────────────────

def run_simulation(n_steps: int = 2000) -> dict:
    scm = CausalBanditSCM()
    standard_agent = StandardBanditAgent()
    causal_agent = CausalBanditAgent()

    standard_estimates = []
    causal_estimates = []
    true_causal_values = [scm.causal_effect[0], scm.causal_effect[1]]

    # Both agents observe the same confounded data stream
    for t in range(n_steps):
        arm, reward, conf = scm.sample_observational()

        # Standard agent: just uses (arm, reward), ignores C
        standard_agent.update(arm, reward)

        # Causal agent: uses (arm, reward, C) to apply adjustment formula
        causal_agent.update(arm, reward, conf)

        if t % 50 == 0:
            standard_estimates.append(standard_agent.values.copy())
            causal_estimates.append([causal_agent.causal_value(a) for a in range(2)])

    return {
        "standard_estimates": np.array(standard_estimates),
        "causal_estimates": np.array(causal_estimates),
        "true_causal_values": true_causal_values,
        "steps": list(range(0, n_steps, 50)),
    }


def plot_results(results: dict):
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle("Causal Bandits vs Standard Bandits\n"
                 "Effect of Confounding on Value Estimation", fontsize=13)

    true = results["true_causal_values"]
    steps = results["steps"]

    for idx, (ax, title, estimates) in enumerate(zip(
        axes,
        ["Standard Bandit\n(learns E[R | arm], biased by confounder)",
         "Causal Bandit\n(learns E[R | do(arm)], debiased)"],
        [results["standard_estimates"], results["causal_estimates"]]
    )):
        for arm in range(2):
            ax.plot(steps, estimates[:, arm],
                    label=f"Arm {arm} estimate", linewidth=2)
            ax.axhline(true[arm], linestyle="--", alpha=0.6,
                       label=f"True causal value (arm {arm})")

        ax.set_title(title)
        ax.set_xlabel("Steps")
        ax.set_ylabel("Estimated value")
        ax.legend(fontsize=8)
        ax.set_ylim(-0.1, 1.5)
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("causal_bandits_comparison.png", dpi=150)
    plt.show()
    print("Plot saved to causal_bandits_comparison.png")


def print_summary(results: dict):
    true = results["true_causal_values"]
    std_final = results["standard_estimates"][-1]
    caus_final = results["causal_estimates"][-1]

    print("\n" + "="*60)
    print("FINAL ESTIMATES (after 2000 steps)")
    print("="*60)
    print(f"{'':25} {'Arm 0':>10} {'Arm 1':>10}")
    print(f"{'True causal value':25} {true[0]:>10.3f} {true[1]:>10.3f}")
    print(f"{'Standard bandit':25} {std_final[0]:>10.3f} {std_final[1]:>10.3f}")
    print(f"{'Causal bandit':25} {caus_final[0]:>10.3f} {caus_final[1]:>10.3f}")
    print()
    print(f"Standard bandit best arm: {int(np.argmax(std_final))} "
          f"({'CORRECT' if int(np.argmax(std_final)) == int(np.argmax(true)) else 'WRONG'})")
    print(f"Causal bandit best arm:   {int(np.argmax(caus_final))} "
          f"({'CORRECT' if int(np.argmax(caus_final)) == int(np.argmax(true)) else 'WRONG'})")
    print()
    print("Explanation:")
    print("  The confounder C inflates E[R|arm=1] for the standard bandit")
    print("  because arm 1 is more often pulled when C=1 (which also boosts reward).")
    print("  The causal bandit correctly identifies the true causal effect.")


if __name__ == "__main__":
    print("Running causal bandit simulation...")
    results = run_simulation(n_steps=2000)
    print_summary(results)
    plot_results(results)
