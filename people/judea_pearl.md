# Judea Pearl — Causality, SCMs, and the Do-Calculus

> **Source**: [bayes.cs.ucla.edu/jp_home.html](https://bayes.cs.ucla.edu/jp_home.html)  
> **Affiliation**: UCLA (Professor Emeritus), Cognitive Systems Laboratory  
> **Awards**: Turing Award (2011), Benjamin Franklin Medal, Harvey Prize  
> **Known for**: Bayesian Networks, Structural Causal Models, do-calculus, Pearl's Causal Hierarchy

---

## Who Is Judea Pearl?

Judea Pearl is the architect of modern causal inference. He received the 2011 **Turing Award** — the highest honor in computer science — for his foundational contributions to probabilistic and causal reasoning in AI.

Pearl began with **Bayesian networks** in the 1980s (a computational framework for reasoning under uncertainty using directed acyclic graphs). He then developed **structural causal models (SCMs)** and the **do-calculus** to move from association to causation — arguably the most important conceptual advance in AI/statistics since Bayes.

His influence on this repository is fundamental: virtually every concept here is built on Pearl's framework.

---

## Core Technical Contributions

### 1. Bayesian Networks (1988)

**Introduced in**: *Probabilistic Reasoning in Intelligent Systems* (1988, Morgan Kaufmann)

A **Bayesian network** is a DAG G = (V, E) where:
- Each node X_i ∈ V represents a random variable
- Each edge (X_j → X_i) represents a direct probabilistic influence
- Each node has a conditional probability table P(X_i | Pa(X_i))

**Joint distribution factorization**:
```
P(X_1, ..., X_n) = ∏_i P(X_i | Pa(X_i))
```

**d-separation** provides a graphical criterion for conditional independence, making Bayesian networks a *representation* of independence structure, not just a factorization.

**Impact**: Bayesian networks became the foundation of probabilistic AI, expert systems, and later causal inference.

### 2. Structural Causal Models (SCMs)

**Introduced in**: *Causality: Models, Reasoning, and Inference* (2000, 2nd ed. 2009)

An SCM M = ⟨U, V, F, P(U)⟩ consists of:
- **U**: exogenous (background) variables with joint distribution P(U)
- **V**: endogenous (observed) variables
- **F = {f_i}**: structural equations — x_i = f_i(Pa(X_i), U_i) for each X_i ∈ V
- **P(U)**: distribution over exogenous variables (noise)

**Why SCMs, not just Bayesian networks?**

Bayesian networks represent **conditional independence** (L1 associations). SCMs encode **causal mechanisms** — the functional relationships that determine how variables respond to interventions (L2) and counterfactuals (L3).

The same BN can correspond to multiple SCMs with different causal structures but identical observational distributions. SCMs are strictly more informative.

### 3. The do-Calculus

**Introduced in**: Pearl (1995), fully developed in Pearl (2000)

**The intervention operator `do(X=x)`**: Set X to value x by surgical intervention — removing all incoming edges to X and fixing its value.

**Interventional distribution**: P(Y | do(X=x)) — what Y's distribution would be if we *forced* X=x, regardless of its natural causes.

**The do-calculus** (three rules):

Let X, Y, Z, W be disjoint subsets of V. G_X̄ denotes G with all arrows into X deleted. G_X̲ denotes G with all arrows out of X deleted.

```
Rule 1 (Insertion/deletion of observations):
P(y | do(x), z, w) = P(y | do(x), w)
if (Y ⊥ Z | X, W) in G_X̄

Rule 2 (Action/observation exchange):
P(y | do(x), do(z), w) = P(y | do(x), z, w)
if (Y ⊥ Z | X, W) in G_X̄Z̲

Rule 3 (Insertion/deletion of actions):
P(y | do(x), do(z), w) = P(y | do(x), w)
if (Y ⊥ Z | X, W) in G_X̄Z̄(W)
```

Where Z̄(W) is the set of Z-nodes that are not ancestors of any W-node in G_X̄.

**Completeness theorem** (Shpitser & Pearl 2006, Huang & Valtorta 2006): The do-calculus is **complete** for causal identification from observational data. Any identifiable causal effect can be computed using these three rules.

### 4. Pearl's Causal Hierarchy (PCH)

Also called the **Ladder of Causation** (*The Book of Why*, 2018):

| Rung | Name | Query type | Notation | Examples |
|------|------|-----------|----------|---------|
| 1 | Association | Seeing | P(Y \| X) | "What is P(cancer \| smoking)?" |
| 2 | Intervention | Doing | P(Y \| do(X)) | "What if we force everyone to smoke?" |
| 3 | Counterfactuals | Imagining | P(Y_x \| X=x', Y=y') | "Would I have cancer if I had never smoked?" |

**The PCH Theorem** (Pearl & Bareinboim, formally): The three rungs are **strictly hierarchical** — no amount of L1 data can answer L2 questions; no amount of L1+L2 data can answer all L3 questions. Each rung requires strictly stronger assumptions.

**Implication for AI**: A system trained purely on observational data (LLMs, standard supervised learning) is fundamentally limited to L1. It cannot reliably answer causal (L2) or counterfactual (L3) questions without additional causal structure.

### 5. Identification Theory

**Backdoor criterion**: P(Y | do(X)) is identifiable by adjustment on Z if:
1. No node in Z is a descendant of X
2. Z blocks every backdoor path from X to Y

**Adjustment formula**:
```
P(Y | do(X=x)) = sum_z P(Y | X=x, Z=z) P(Z=z)
```

**Front-door criterion** (for cases where backdoor fails):
If M mediates X → Y and satisfies certain conditions:
```
P(Y | do(X=x)) = sum_m [sum_{x'} P(M=m | X=x') P(X=x')] P(Y | X=x, M=m)
```

**ID algorithm** (Tian & Pearl, 2002; Shpitser & Pearl, 2006): A complete algorithm for identifying any identifiable causal effect from a semi-Markovian model (with latent confounders represented as bidirected edges).

### 6. Counterfactual Inference

**Twin networks**: To compute P(Y_x = y | X=x', Y=y'), construct a "twin" copy of the SCM with X forced to x, sharing the same exogenous variables U.

**Three-step abduction-action-prediction procedure**:
1. **Abduction**: Compute P(U | evidence) from observed evidence
2. **Action**: Modify SCM by do(X=x)
3. **Prediction**: Compute Y in the modified SCM with updated P(U)

**Applications**:
- Attribution (would Y have occurred but for X?)
- Credit assignment in RL
- Policy evaluation (would policy π_e have performed better than π_b?)

---

## Key Books

### *Probabilistic Reasoning in Intelligent Systems* (1988)
- Introduced Bayesian networks to AI
- Developed belief propagation algorithm
- Standard reference for probabilistic graphical models

### *Causality: Models, Reasoning, and Inference* (2000; 2nd ed. 2009)
- The definitive technical reference for SCMs, do-calculus, identification
- Chapters: probability, intervention, counterfactuals, actions/plans, causality in statistics, structural models of causation
- **Essential reading for this repository**

### *The Book of Why* (2018, with Dana Mackenzie)
- Popular science treatment of causality
- Introduces the Ladder of Causation (PCH) to general audience
- Historical narrative: statistics vs causation debate
- **Good entry point before the technical books**

### *Causal Inference in Statistics: A Primer* (2016, with Glymour & Jewell)
- Short technical primer
- Covers regression, confounding, mediation analysis
- **Best short introduction**

---

## Key Papers

| Year | Title | Key Result |
|------|-------|-----------|
| 1988 | *Probabilistic Reasoning...* (book) | Bayesian networks |
| 1993 | *Belief Propagation* | BP algorithm for Bayesian networks |
| 1995 | *Causal Diagrams for Empirical Research* | First formulation of do-calculus |
| 2000 | *Causality* (book) | Complete SCM framework |
| 2001 | *Direct and Indirect Effects* | Mediation analysis formalized |
| 2009 | *Causality* 2nd ed. | Extended with new results |
| 2012 | *The Do-Calculus Revisited* | Survey of completeness results |
| 2018 | *The Book of Why* (popular book) | PCH Ladder of Causation |
| 2018 | *Theoretical Impediments to ML with Seven Sparks from the Causal Revolution* | Why ML needs causality |
| 2019 | *The Seven Tools of Causal Inference* | Practical guide |
| 2022 | *On Pearl's Hierarchy* (with Bareinboim et al.) | Formal PCH treatment |

---

## Pearl's Critique of Machine Learning

Pearl has been a persistent critic of the claim that large-scale statistical learning (deep learning, LLMs) can achieve human-level intelligence:

**"Seven Sparks" thesis** (2018 paper, *Theoretical Impediments to Machine Learning*):

Current ML systems are limited to:
1. Association-based predictions (L1)
2. Cannot perform interventional reasoning without causal assumptions
3. Cannot answer counterfactual questions
4. Cannot reason about agency, intentions, or responsibility
5. Cannot generalize robustly to distribution shifts
6. Cannot explain their outputs causally
7. Cannot perform moral reasoning (which requires L3)

**Quote** (from *The Book of Why*):
> "All the impressive achievements of deep learning amount to just curve fitting."

This is deliberately provocative, but the formal argument is serious: without causal structure, no amount of data can answer causal questions. This is a mathematical theorem (PCH hierarchy result), not an opinion.

---

## Ongoing Work and Current Position

Pearl is Professor Emeritus at UCLA and remains active:
- Maintains correspondence with researchers worldwide
- Writes blog posts and opinion pieces on causality in AI
- 2022-2025: papers on LLMs and causality, formal PCH results, counterfactual reasoning

**Blog**: "Causal Analysis in Theory and Practice" — posts on current AI debates through causal lens.

---

## The UCLA Cognitive Systems Lab

The lab Pearl founded continues research on:
- Causal discovery algorithms
- Applications to epidemiology, economics, social science
- Formal verification of causal claims

Notable alumni: Jin Tian, Ilya Shpitser, Elias Bareinboim, Manabu Kuroki

---

## Connection to This Repository

Pearl's framework is the **theoretical foundation** of this repository:

| Pearl Contribution | This Repository Application |
|-------------------|----------------------------|
| SCMs | Formal environment models in CRL |
| do-calculus | Language for causal intervention in RL |
| PCH | Classification scheme for RL agent capabilities |
| Backdoor/front-door | Identifiability conditions for off-policy RL |
| Counterfactual inference | Credit assignment in policy gradient methods |
| Twin networks | Off-policy evaluation under confounding |

---

## References

- Pearl, J. (1988). *Probabilistic Reasoning in Intelligent Systems*. Morgan Kaufmann.
- Pearl, J. (2000/2009). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
- Pearl, J. (2018). *The Book of Why*. Basic Books.
- Pearl, J., Glymour, M., & Jewell, N.P. (2016). *Causal Inference in Statistics: A Primer*. Wiley.
- Pearl, J. (2018). *Theoretical Impediments to Machine Learning with Seven Sparks from the Causal Revolution*. arXiv.
- Homepage: https://bayes.cs.ucla.edu/jp_home.html
