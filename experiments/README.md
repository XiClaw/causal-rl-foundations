# experiments/README.md

## Runnable Experiments

Each experiment is a self-contained Python script demonstrating a key concept.

### Requirements

```bash
pip install numpy matplotlib
```

### 1. Causal Bandits vs Standard Bandits

**File:** `causal_bandits.py`

**Concept:** Demonstrates the difference between observational and interventional reasoning in a bandit setting. A hidden confounder causes a standard bandit to learn biased value estimates; the causal bandit uses the backdoor adjustment formula to debias.

**Run:**
```bash
python causal_bandits.py
```

**Expected output:** A plot showing that the standard bandit converges to the wrong arm, while the causal bandit correctly identifies the better arm.

---

### 2. Counterfactual Reasoning in MDPs

**File:** `counterfactual_mdp.py`

**Concept:** Implements Pearl's three-step counterfactual procedure (Abduction → Action → Prediction) in a simple MDP. Uses counterfactual rewards as a baseline for policy gradient, demonstrating variance reduction.

**Run:**
```bash
python counterfactual_mdp.py
```

**Expected output:** A training curve showing that counterfactual policy gradient converges faster than standard REINFORCE.

---

## Planned Experiments

- [ ] `scm_identification.py` — When can interventional quantities be identified from observational data? (do-calculus in code)
- [ ] `logical_bandit.py` — A bandit where the reward is determined by a mathematical fact (logical uncertainty)
- [ ] `aixi_approx.py` — A resource-bounded approximation to AIXI on small environments
- [ ] `irl_causal.py` — Inverse reinforcement learning with causal structure
