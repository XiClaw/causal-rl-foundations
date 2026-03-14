# Elias Bareinboim — CausalAI Lab & Causal Artificial Intelligence

> **Source**: [causalai.net](https://causalai.net/) | [causalai-book.net](https://causalai-book.net/)  
> **Affiliation**: Columbia University, Dept. of Computer Science  
> **Lab**: CausalAI Laboratory  
> **Role**: AAAI Fellow, Associate Editor, *Journal of Causal Inference*

---

## Who Is Elias Bareinboim?

Elias Bareinboim is one of the world's leading researchers on **causal inference and causal AI**. He is a student/collaborator of Judea Pearl and has substantially extended Pearl's causal framework — particularly in the directions of **transportability** (generalizing causal results across domains), **data fusion** (combining heterogeneous datasets), and **causal reinforcement learning**.

His lab (CausalAI Laboratory at Columbia) is producing some of the most rigorous theoretical work at the intersection of causality, machine learning, fairness, and decision-making.

---

## Research Directions

### 1. Causal Reinforcement Learning (CRL)

Bareinboim's CRL framework places RL within Pearl's Causal Hierarchy:

| PCH Layer | RL Concept | Formal Notation |
|-----------|-----------|-----------------|
| L1 (Observational) | Passive data, behavior cloning | P(r \| s, a) |
| L2 (Interventional) | Policy optimization, do-calculus | P(r \| do(a), s) |
| L3 (Counterfactual) | Credit assignment, off-policy evaluation | P(r_{a'} \| a, s, r) |

**Key insight**: Standard RL operates at L1/L2. Genuine credit assignment (why did reward happen?) requires L3 counterfactual reasoning. An agent that only operates at L1 cannot distinguish:
- "I got reward because my action caused it" (L2)  
- "I would have gotten reward even without my action" (L3 counterfactual)

**Sequential Causal Games** (2026, preprint):
Extension of CRL to multi-agent settings. Each player is modeled as an AIXI-like agent with a causal world model. Nash equilibria under counterfactual reasoning.

### 2. Transportability and Data Fusion

**The problem**: You have experimental data from population Π, but want to make inferences about population Π*. They differ in observable ways (characterized by selection diagrams).

**Transportability theorem** (Bareinboim & Pearl, 2012):
A causal effect P(y | do(x)) is transportable from Π to Π* iff it is identified by the **transport formula** using the selection diagram S. The do-calculus is **complete** for transportability.

**Data fusion** (Bareinboim & Pearl, 2016, PNAS):
Formally combines:
- Randomized experiments (interventional, L2)
- Observational studies (L1)
- Data from multiple heterogeneous populations

Unifies IV (instrumental variables), RD (regression discontinuity), and experimental designs under a single causal framework.

**RL connection**: Offline RL is fundamentally a transportability problem — training data comes from behavior policy π_b, we want to evaluate π_e. Off-policy evaluation = causal transportability.

### 3. Causal Fairness Analysis (FnTML 2024)

Comprehensive framework for fairness through causality. Key contributions:

**Decomposition of discrimination**:
```
TE(x₀, x₁) = DE(x₀, x₁) + IE(x₀, x₁) + SE(x₀, x₁)
```
Where:
- TE = Total Effect
- DE = Direct Effect (via direct path X → Y)  
- IE = Indirect Effect (via mediators)
- SE = Spurious Effect (via backdoor paths / common causes)

**Fairness criteria as causal constraints**:
- Counterfactual fairness: P(Y_{x=1} | X=0) = P(Y_{x=0} | X=0)
- Demographic parity: P(Y | X=1) = P(Y | X=0) [L1]
- Equalized odds: P(Y | do(X=1)) = P(Y | do(X=0)) [L2]

**Fairness-Accuracy Trade-Offs (AAAI 2025)**:
Proves that for a given causal model, the Pareto frontier between fairness and accuracy is computable from the causal graph + data.

### 4. Confounding Robust Deep RL (NeurIPS 2025)

**Problem**: Standard deep RL agents fail under unmeasured confounders — when the data collection policy created correlations between states and actions that are *not* due to the agent's choices.

**Solution**: Use causal identification theory to:
1. Detect whether confounders are present (testable from data + causal graph)
2. Apply robust estimation methods that remain valid under partial confounding

**Paper**: *Confounding Robust Deep Reinforcement Learning*, NeurIPS 2025.

### 5. Neural Causal Abstractions (AAAI 2024)

**Problem**: How do you learn a high-level causal model from a low-level neural representation?

**Causal abstraction**: A mapping τ: low-level SCM → high-level SCM that preserves interventional distributions.

**Key result**: Necessary and sufficient conditions for a neural model to be a valid causal abstraction of a ground-truth SCM. Uses representation theory to characterize when abstractions exist.

**Transportable Representations for Domain Generalization (AAAI 2024)**:
A representation φ(X) is domain-generalizable iff it is causally sufficient for the target variable Y across domains. Formalized using transportability theory.

### 6. Counterfactual Image Editing (ICML 2024, NeurIPS 2025)

Applies causal inference to image generation:
- Edit an image by intervening on latent causal variables
- Counterfactual: "What would this image look like if [causal variable] had been different?"
- Uses a disentangled causal latent space (ICML 2024) and counterfactual realizability theory (ICLR 2025)

**Counterfactual Realizability (ICLR 2025)**:
Formal conditions under which a counterfactual query can be answered from observational + interventional data.

---

## The Causal AI Book

**Title**: *Causal Artificial Intelligence: A Roadmap for Building Causally Intelligent Systems*  
**Author**: Elias Bareinboim  
**Status**: Draft version (Oct 11, 2025) — freely available  
**URL**: [causalai-book.net](https://causalai-book.net/)

### Book Structure (30 Lectures across 7 Parts)

| Part | Title | Key Topics |
|------|-------|------------|
| **I** | Foundations | Causal graphs, SCMs, Pearl's Causal Hierarchy (PCH) |
| **II** | Causal Reasoning | Interventions (do-calculus), counterfactuals, fairness analysis |
| **III** | Decision Making | Causal decision models, MDPs, CRL, offline/online learning, causal games |
| **IV** | Generalization | Transportability, domain adaptation, partial transportability |
| **V** | Generative Modeling | Neural causal models, structural constraints, causal abstraction |
| **VI** | Learning | Observational/interventional equivalence classes, structural learning, causal representation learning |
| **VII** | Special Topics | Parameter identification (linear SCMs, IV), doubly robust estimation, graphical model hierarchies |

### Recommended Reading Paths

**For RL researchers**: Part I → Part III (Decision Making) → Part IV (Generalization)

**For ML/fairness researchers**: Part I → Part II (Causal Reasoning, Fairness) → Part VI (Learning)

**For generative model researchers**: Part I → Part V (Generative Modeling) → Part VI

**Full year course**: Part I–II (semester 1), Part III–VII (semester 2)

---

## Key Collaborations and Alumni

Many of Bareinboim's PhD students have become assistant professors, indicating the centrality of this group:

| Former Student | Current Position | Focus |
|----------------|-----------------|-------|
| Juan D. Correa | Assistant Professor | Counterfactual identification |
| Yonghan Jung | Assistant Professor | Nonparametric estimation |
| Sanghack Lee | Assistant Professor | Causal discovery |
| Junzhe Zhang | Assistant Professor | Causal RL, off-policy evaluation |
| Drago Plecko | Assistant Professor | Causal fairness |

---

## Connection to This Repository

Bareinboim's work provides the **formal infrastructure** for much of this repository:

1. **do-calculus** → the language for stating causal claims in AIXI and CRL
2. **Transportability** → the formal framework for offline RL and generalization
3. **CRL framework** → the direct application of PCH to sequential decision-making
4. **Causal fairness** → alignment between agent behavior and human values
5. **Counterfactual realizability** → conditions under which counterfactual alignment objectives are well-defined

The book *Causal Artificial Intelligence* is essentially a textbook for this repository's Theory section.

---

## Key Papers to Read

| Priority | Paper | Why |
|----------|-------|-----|
| ⭐⭐⭐ | *On Pearl's Hierarchy and the Foundations of Causal Inference* (ACM 2022) | Foundation of the whole framework |
| ⭐⭐⭐ | *Causal Inference and the Data-Fusion Problem* (PNAS 2016) | The unifying data fusion theorem |
| ⭐⭐ | *Causal Fairness Analysis* (FnTML 2024) | TE/DE/IE/SE decomposition |
| ⭐⭐ | *Robust Agents Learn Causal World Models* (ICLR 2024) | Necessity of causal representations |
| ⭐⭐ | *Sequential Causal Games* (preprint 2026) | Multi-agent CRL |
| ⭐ | *Confounding Robust Deep RL* (NeurIPS 2025) | Practical confounding-robust RL |
| ⭐ | *Counterfactual Realizability* (ICLR 2025) | Formal conditions for L3 queries |

---

## References

- Bareinboim, E. (2025). *Causal Artificial Intelligence: A Roadmap*. Draft. https://causalai-book.net/
- Bareinboim, E. & Pearl, J. (2016). *Causal Inference and the Data-Fusion Problem*. PNAS.
- Bareinboim, E. et al. (2022). *On Pearl's Hierarchy and the Foundations of Causal Inference*. ACM Book Chapter.
- Plecko, D. & Bareinboim, E. (2024). *Causal Fairness Analysis*. Foundations and Trends in ML.
- Richens, J. & Everitt, T. (2024). *Robust Agents Learn Causal World Models*. ICLR.
- CausalAI Laboratory: https://causalai.net/
