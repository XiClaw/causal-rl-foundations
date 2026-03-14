# Causal Inference in Reinforcement Learning

> **Status**: Living document — last updated March 2026  
> **Scope**: Formal bridge between Pearl's causal hierarchy, structural causal models (SCMs), and reinforcement learning; covering theory, algorithms, and alignment implications

---

## 1. The Pearl Causal Hierarchy (PCH) and Its RL Implications

### 1.1 Three Layers

The **Pearl Causal Hierarchy** (PCH), formalized in Bareinboim & Correa (2022):

| Layer | Type | Query | Typical question | RL mapping |
|-------|------|-------|-----------------|------------|
| **L1** | Association | $P(y \mid x)$ | "What is?" | Offline data analysis |
| **L2** | Intervention | $P(y \mid do(x))$ | "What if I do?" | Action execution in RL |
| **L3** | Counterfactual | $P(y_x \mid x', y')$ | "What if I had done?" | Off-policy eval, policy improvement |

**Causal Hierarchy Theorem (CHT):** L1 data cannot uniquely determine L2 distributions; L2 data cannot uniquely determine L3 distributions. The three layers are irreducible.

**RL consequence:** Offline RL data (L1 observations) cannot replace true interventions (L2) in general — off-policy learning is fundamentally constrained by counterfactual identifiability.

### 1.2 Causal Reinforcement Learning (CRL) Framework

**Paper:** *An Introduction to Causal Reinforcement Learning* — Bareinboim, Zhang & Lee (2024; Columbia Tech Report R-65; [PDF](https://www.causalai.net/r65.pdf))

Defines three core tasks of CRL:
1. **Generalized Policy Learning**: unifies online (L2 interventions), offline (L1 observations), and do-calculus learning into a single policy optimization framework
2. **When and Where to Intervene**: uses causal graph structure to determine optimal intervention sets
3. **Counterfactual Decision-Making**: policy optimization based on L3 counterfactual reasoning

---

## 2. Causal Bandits

### 2.1 Foundations

**Paper:** *Causal Bandits: Learning Good Interventions via Causal Inference* — Lattimore, Lattimore & Reid (NeurIPS 2016; [arXiv:1606.03203](https://arxiv.org/abs/1606.03203))

Formal setup:
- Action set = set of interventions on a causal graph: $\{do(X = x)\}$
- Reward = $P(Y \mid do(X = x))$
- Goal: minimize simple regret (find the best intervention)

**Key result:** Algorithms that exploit causal structure achieve strictly better simple regret bounds than algorithms that ignore it.

**Significance:** First formal proof that structural causal knowledge systematically accelerates intervention learning.

---

**Paper:** *Regret Analysis of Bandit Problems with Causal Background Knowledge* — Lu, Meisami, Tewari & Yan (UAI 2020; [PMLR](https://proceedings.mlr.press/v124/lu20a.html))

**Algorithms:**
- **C-UCB** (Causal UCB): exploits d-separation relations to prune the effective exploration space
- **C-TS** (Causal Thompson Sampling): Bayesian causal bandits
- **CL-UCB / CL-TS**: extensions to linear bandit settings

**Regret bounds:** CL-UCB/CL-TS cumulative regret depends only on feature dimension $d$, not number of interventions $N$ — resolves an open problem from Lattimore et al. 2016.

**Empirical result:** After only a few hundred iterations, causal algorithms achieve ~2/3 less regret than standard bandit algorithms.

---

### 2.2 Unknown Causal Graph

**Paper:** *Causal Bandits with Unknown Graph Structure* (NeurIPS 2021; [link](https://papers.nips.cc/paper/2021/hash/d010396ca8abf6ead8cacc2c2f2f26c7-Abstract.html))

Even when the causal graph is unknown, regret bounds for causal trees, forests, and general graphs remain significantly better than standard MAB algorithms. Key idea: simultaneous structure learning via exploratory interventions.

---

**Paper:** *Partial Structure Discovery is Sufficient for No-regret Learning in Causal Bandits* (NeurIPS 2024; [link](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c50e3c72bf45a361afc7c16d26c21a1a-Abstract-Conference.html))

**Breakthrough:** Complete causal structure discovery is **not necessary** for no-regret learning. First formal characterization of the minimal sufficient subset of latent confounders that needs to be identified.

**Algorithm (two phases):**
1. Random intervention sampling to learn the reward node's ancestor subgraph
2. UCB over the set of possibly optimal arms

**Guarantees:** Sample complexity grows **polynomially** in number of nodes; overall regret is **sublinear**.

---

**Paper:** *Linear Causal Bandits: Unknown Graph and Soft Interventions* (NeurIPS 2024; [link](https://proceedings.neurips.cc/paper_files/paper/2024/hash/2aba6ec20299931d46ddeefd5ddcb442-Abstract-Conference.html))

Simultaneously handles unknown graph structure and soft interventions; removes two major assumptions from prior work.

---

**Paper:** *Causal Bandits: The Pareto Optimal Frontier of Adaptivity* (ICML 2024; [PMLR](https://proceedings.mlr.press/v235/liu24b.html))

Establishes novel reduction from causal bandits to **linear bandits**, obtaining first instance-dependent regret bounds.

---

## 3. Counterfactual Reasoning in RL

### 3.1 Counterfactual Multi-Agent Policy Gradients (COMA)

**Paper:** *Counterfactual Multi-Agent Policy Gradients* — Foerster, Farquhar, Afouras, Nardelli & Whiteson (AAAI 2018; [link](https://aaai.org/papers/11794-counterfactual-multi-agent-policy-gradients/))

**Problem:** Multi-agent credit assignment — determining each agent's true contribution to the team reward.

**Algorithm:**
- Centralized critic estimating joint Q-function $Q(s, \mathbf{a})$
- **Counterfactual baseline:** marginalizes over agent $i$'s actions:

$$\text{baseline}(s, \mathbf{a}_{-i}) = \sum_{a'_i} \pi(a'_i \mid \tau_i) \cdot Q(s, (a'_i, \mathbf{a}_{-i}))$$

- Advantage: $A^i(s, \mathbf{a}) = Q(s, \mathbf{a}) - \text{baseline}(s, \mathbf{a}_{-i})$

**Results:** Significantly outperforms other multi-agent actor-critic methods on StarCraft micromanagement; approaches centralized optimal controller.

---

### 3.2 Proximal Causal Inference for Confounded RL

**Paper:** *Proximal Reinforcement Learning: Efficient Off-Policy Evaluation in Partially Observed MDPs* — Bennett et al. (Operations Research 2023; [arXiv:2110.15332](https://arxiv.org/pdf/2110.15332))

Extends proximal causal inference to POMDP off-policy evaluation (OPE). Introduces **bridge function sequences** to obtain consistent estimates in the presence of unmeasured confounders — directly applicable to medical/educational offline RL.

---

### 3.3 Two-way Deconfounder for OPE (NeurIPS 2024)

**Paper:** *Two-way Deconfounder for Off-Policy Evaluation in Causal RL* (NeurIPS 2024; [PDF](https://openreview.net/pdf?id=Lu9Rasfmjj))

Inspired by two-way fixed-effects panel data regression; proposes a **bidirectional deconfounder** for OPE problems with unmeasured confounding.

---

## 4. Causal Discovery in RL Environments

### 4.1 Causal Discovery as RL

**Paper:** *Causal Discovery with Reinforcement Learning* — Zhu, Ng et al. (ICLR 2020 Oral; [arXiv:1906.04477](https://arxiv.org/abs/1906.04477))

Reformulates causal discovery (learning DAG structure) as an RL problem. The RL agent searches the DAG space; BIC or similar causal scoring functions serve as rewards. Avoids local search heuristics of classical score-based methods.

**Paper:** *Ordering-Based Causal Discovery with Reinforcement Learning* (IJCAI 2021; [PDF](https://www.ijcai.org/proceedings/2021/0491.pdf))

Reduces search space via variable ordering; scalable to graphs with thousands of variables.

---

### 4.2 Causal Structured World Models for Offline RL

**Paper:** *Offline Reinforcement Learning with Causal Structured World Models (FOCUS)* — Zhu et al. (2022; [arXiv:2206.01474](https://arxiv.org/abs/2206.01474))

**Algorithm FOCUS** (oFfline mOdel-based RL with CaUsal Structure):
- Learns a causally structured world model (rather than a fully-connected network)
- Constrains spurious correlations between unrelated state variables

**Theorem (first of its kind):** Provides an explicit **upper bound on generalization error** for causal world models in offline RL, provably better than unconstrained world models.

---

### 4.3 Causal Curiosity

**Paper:** *Causal Curiosity: RL Agents Discovering Self-supervised Experiments for Causal Representation Learning* — Sontakke, Mehrjou, Itti & Schölkopf (ICML 2021; [arXiv:2010.03110](https://arxiv.org/abs/2010.03110))

Introduces **causal curiosity** as an intrinsic reward that drives agents to actively perform experiments for causal representation learning. Binary tree traversal exploration algorithm; learned representations transfer to downstream tasks.

---

### 4.4 CSCG: Clone-Structured Causal Graphs

**Paper:** *Space is a latent sequence: Structured sequence learning as a unified theory of representation in the hippocampus* — Raju et al. (2022; [arXiv:2212.01508](https://arxiv.org/abs/2212.01508))

**CSCG** maps sensory inputs to different contexts via a higher-order graph structure. Core idea: spatial representations emerge from compression of sequential and episodic experience. Provides a causal planning substrate for RL agents; unifies over a dozen hippocampal representation phenomena.

---

### 4.5 CausalVAE: Disentangled Causal Representations

**Paper:** *CausalVAE: Disentangled Representation Learning via Neural Structural Causal Models* — Yang et al. (CVPR 2021; [IEEE](https://ieeexplore.ieee.org/document/9578520))

Integrates an SCM layer (Mask Layer) into the VAE framework to learn causally disentangled latent variables. Provides interpretable state representations for policy learning with improved generalization.

---

## 5. Causal Imitation Learning

### 5.1 Causal Confusion in Imitation Learning

**Paper:** *Causal Confusion in Imitation Learning* — de Haan, Jayaraman & Levine (NeurIPS 2019; [arXiv:1905.11979](https://arxiv.org/abs/1905.11979))

**Key findings:**
- Behavioral cloning is **non-causal** — ignores the causal structure of expert-environment interaction
- **Counterintuitive:** providing more input features can *decrease* performance because the model latches onto spurious correlations
- Demonstrates **causal misidentification** in multiple control tasks and real driving scenarios

**Solution:** Correct causal feature identification via environment interventions and expert queries.

---

### 5.2 Causal Imitation Learning with Unobserved Confounders

**Paper:** *Causal Imitation Learning With Unobserved Confounders* — Zhang, Kumor & Bareinboim (NeurIPS 2020 Oral; [PDF](https://proceedings.neurips.cc/paper/2020/file/8fdd149fcaa7058caccc9c4ad5b0d89a-Paper.pdf))

Introduces the concept of **imitability**: using do-calculus to derive necessary and sufficient conditions for whether imitation is achievable when the expert has access to unobservable variables.

---

**Paper:** *Sequential Causal Imitation Learning with Unobserved Confounders* — Kumor, Zhang & Bareinboim (NeurIPS 2021; [link](https://proceedings.neurips.cc/paper/2021/hash/7b670d553471ad0fd7491c75bad587ff-Abstract.html))

Extends to multi-step sequential decisions. Provides a **graphical criterion** that is a **necessary and sufficient condition** for imitability in sequential settings; gives an efficient algorithm to check the criterion.

---

### 5.3 Causal Imitation under Temporally Correlated Noise

**Paper:** *Causal Imitation Learning under Temporally Correlated Noise* — Swamy, Choudhury & Bagnell (ICML 2022; [PMLR](https://proceedings.mlr.press/v162/swamy22a.html))

**Problem:** Expert behavior data contains temporally correlated noise, causing behavioral cloning to learn spurious correlations.

**Algorithms:**
- **DoubIL**: instrument variable regression (IVR) using a simulator to eliminate noise correlation
- **ResiduIL**: game-theoretic style, fully offline, no online expert interaction

**Core idea:** Treats expert noise as a confounding variable; uses causal instrumental variable methods to remove its influence.

---

## 6. Recent Advances (2020–2025)

### 6.1 Causality-Aware Entropy Regularization (ACE, ICML 2024)

**Paper:** *ACE: Off-Policy Actor-Critic with Causality-Aware Entropy Regularization* — Ji et al. (ICML 2024 Oral; [arXiv:2402.14528](https://arxiv.org/abs/2402.14528))

Analyzes **causal relationships** between each action dimension and reward to design causally-aware entropy regularization:

$$\mathcal{L}_{\text{ACE}} = \mathcal{L}_{\text{AC}} + \beta \sum_i w_i \cdot H(\pi(a_i \mid s))$$

where $w_i$ is the causal importance weight of action dimension $i$. Includes gradient dormancy detection and reset mechanisms.

**Results:** Significantly outperforms SAC/TD3 across 29 continuous control tasks (7 domains); ~20–30% improvement on high-dimensional tasks like Humanoid.

---

### 6.2 Causal Data Augmentation (CAIAC, ICML 2024)

**Paper:** *Causal Action Influence Aware Counterfactual Data Augmentation (CAIAC)* — Armengol-Urpí et al. (ICML 2024; [PMLR](https://proceedings.mlr.press/v235/armengol-urpi-24a.html))

Generates feasible synthetic samples from a fixed offline dataset via causal-influence-aware counterfactual augmentation.

---

### 6.3 Non-Stationarity via Causal Representations (COREP, ICML 2024)

**Paper:** *Tackling Non-Stationarity in RL via Causal-Origin Representation* — Zhang et al. (ICML 2024; [GitHub: PKU-RL/COREP](https://github.com/PKU-RL/COREP))

Learns **Causal-Origin Representations (COR)** to handle non-stationarity in RL environments.

---

### 6.4 DeepMind: Causal Reasoning in Probability Trees

**Paper:** *Algorithms for Causal Reasoning in Probability Trees* — Genewein, McGrath, Delétang et al. (DeepMind 2020; [arXiv:2010.12237](https://arxiv.org/abs/2010.12237); [GitHub](https://github.com/google-deepmind/deepmind-research/tree/master/causal_reasoning))

Develops causal reasoning algorithms covering the full PCH (association/intervention/counterfactual) for probability trees. More general than causal Bayesian networks; represents causal relations that CBNs cannot. Applicable to arbitrary discrete stochastic processes.

---

### 6.5 Sequential Causal Games (Bareinboim Lab, 2024–2025)

**Paper:** *Sequential Causal Games* (Bareinboim lab; [PDF](https://causalai.net/r145.pdf))

Existing game-theoretic frameworks (extensive-form games, Markov games) cannot capture causal relations between agents. This work embeds SCMs into multi-agent sequential decision-making and formalizes existence and computation of Nash equilibria in causal games.

---

## 7. Alignment Implications: Causality and Intent Alignment

### 7.1 Reward Hacking and Causal Confusion

**Paper:** *Causal Confusion and Reward Misidentification in Preference-Based Reward Learning* — Tien, He, Erickson, Dragan & Brown (ICLR 2023; [OpenReview](https://openreview.net/forum?id=R0Xxvr_X3ZA))

**Key findings:**
- Reward misidentification in preference learning is a systematic manifestation of causal confusion
- **Root cause of reward hacking:** The learned reward function has low test error but poor out-of-distribution generalization; optimizing the misidentified reward causes policy to escape the training distribution
- Three contributing factors: non-causal spurious features, preference noise, partial observability

**RLHF relevance:** These findings directly apply to reward hacking in RLHF.

---

**Paper:** *Addressing Reward Hacking in RLHF with Causality* (ETH Zurich, 2024; [PDF](https://las.inf.ethz.ch/wp-content/uploads/2024/10/rlhf-reward-hacking-proposal.pdf))

Argues that reward hacking in RLHF is primarily caused by causal misidentification; proposes causal inference methods to correctly identify true human intent.

---

### 7.2 The PCH-Alignment Connection

Applying Pearl's causal hierarchy to the alignment problem:

1. **The L1→L2 Gap (Observation to Intervention):** Language models train on massive observational data (L1), but act interventionally at deployment (L2). Unidentifiable confounding leads to reward misspecification.

2. **Counterfactual Reasoning and Intent:** Truly understanding human intent requires L3 reasoning — "Would the human have been satisfied if the agent had not taken this action?" — which requires a causal world model.

3. **Bareinboim CRL for Alignment:**
   - Under Generalized Policy Learning, agents can infer do(X)-level intent from human feedback (L1)
   - The causal graph reveals which features are **truly causally relevant** (intent) vs. spuriously correlated (reward hacking targets)

---

## 8. Surveys and Resources

| Resource | Authors | Year | Link |
|----------|---------|------|------|
| Causal RL: A Survey | Deng, Jiang, Long, Zhang | TMLR 2023 | [arXiv:2307.01452](https://arxiv.org/abs/2307.01452) |
| A Survey on Causal RL | Zeng et al. | TNNLS 2024 | [IEEE](https://ieeexplore.ieee.org/abstract/document/10771589) |
| Intro to Causal RL | Bareinboim, Zhang, Lee | 2024 | [PDF](https://www.causalai.net/r65.pdf) |
| CRL Tutorial (ICML 2020) | — | 2020 | [crl.causalai.net](https://crl.causalai.net/) |
| Awesome Causal RL List | libo-huang | ongoing | [GitHub](https://github.com/libo-huang/Awesome-Causal-Reinforcement-Learning) |

---

## 9. Algorithm Summary

| Algorithm | Paper | Year | Core idea |
|-----------|-------|------|-----------|
| C-UCB / C-TS | Lu et al. | 2020 | Causal graph prunes exploration space |
| COMA | Foerster et al. | 2018 | Counterfactual baseline for multi-agent credit |
| DoubIL / ResiduIL | Swamy et al. | 2022 | Instrumental variables for temporally correlated noise |
| FOCUS | Zhu et al. | 2022 | Causal world models for offline RL |
| ACE | Ji et al. | 2024 | Causality-aware entropy regularization |
| Causal Curiosity | Sontakke et al. | 2021 | Intrinsic causal curiosity reward |
| iCaRL / IRM-RL | Lu et al. | 2022 | Invariant causal representations |
| Proximal RL | Bennett et al. | 2023 | Proximal causal inference for confounded POMDP |
| CAIAC | Armengol-Urpí et al. | 2024 | Counterfactual data augmentation |
| COREP | Zhang et al. | 2024 | Causal-origin representations for non-stationarity |
