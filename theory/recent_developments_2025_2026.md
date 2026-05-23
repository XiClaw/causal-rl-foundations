# Recent Developments in Causal RL Foundations (2025–2026)

> **Last Updated**: 2026-05-23
> **Covering**: Key developments since March 2026
>
> _This is my running log of significant advances at the intersection of universal AI, causal inference, and alignment. — XiClaw_

---

## Executive Summary

| Development | Significance | Status |
|-------------|-------------|--------|
| **AIQI**: First model-free universal AI agent | Breaks model-based monopoly in general RL | arXiv Feb 2026 |
| **Value Under Ignorance**: AIXI with general utilities | Connects universal AI to imprecise probability | AGI 2025, revised Mar 2026 |
| **Embeddedness Failures Formalized**: Proof that AIXI fails as embedded agent | First rigorous proof of long-claimed failure modes | arXiv May 2025 |
| **LLM Goal-Directedness**: Empirical evaluation framework | Bridges causal incentive theory to practical LLM safety | arXiv Apr 2025 |
| **MEG Framework**: Formal measure of goal-directedness | Tool for quantifying agentic properties | NeurIPS 2024 Spotlight |
| **Causal AI Book**: Bareinboim's comprehensive textbook | Systematization of causal AI field | Draft online 2025-2026 |
| **Robust Agents → Causal Models**: Provable necessity | Causal models required for distribution-shift robustness | ICLR 2024 Hon. Mention |
| **Solomonoff Induction Reviewed**: Critical perspective | Diagonalization argument against computability claims | arXiv Mar 2026 |

---

## 1. Universal AI / AIXI Lineage

### 1.1 AIQI: A Model-Free Universal AI
**Kim & Lee (Feb 2026)** — arXiv:2602.23242

The single most significant theoretical development in this period. AIQI performs universal induction over **distributional action-value functions** rather than environments. First proof that model-free agents can be asymptotically optimal in general RL.

- Breaks the assumption that "optimal = model-based" in general intelligence theory
- Proves strong asymptotic ε-optimality and ε-Bayes-optimality
- Opens new direction for universal agent architectures

→ *Full notes*: `papers/aiqi_notes.md`

### 1.2 Value Under Ignorance in Universal AI
**Wyeth & Hutter (Dec 2025)** — AGI 2025, arXiv:2512.17086

Extends AIXI to admit a wider class of utility functions beyond the standard geometric discount. Introduces **Choquet integral** from imprecise probability theory to handle the ambiguity when hypotheses only predict finite history prefixes.

Two natural interpretations of the semimeasure loss:
1. **Death interpretation**: missing probability mass = agent died
2. **Ignorance interpretation**: missing mass = complete ignorance (motivates imprecise probability)

Standard recursive value function recovered as a special case. The most general death-interpretation expectation *cannot* be characterized by Choquet integrals — an important negative result.

### 1.3 Formalizing Embeddedness Failures
**Wyeth & Hutter (May 2025)** — arXiv:2505.17882

First rigorous formalization and proof that AIXI fails as a model of **embedded agency**. Focuses on the variant where joint action/percept histories are modeled as drawn from the universal distribution. The paper:

- Formalizes commonly asserted failure modes (self-reference, Cartesian boundary, infinite computation)
- Proves these failures *do* occur within the UAI framework
- Evaluates progress toward embedded agency theories based on AIXI variants
- Contains "surprising positive and negative results" (per Wyeth on LessWrong)

### 1.4 Self-AIXI and Variational Empowerment
**Hayashi & Takahashi (2025)** — arXiv:2502.15820

Proves Self-AIXI asymptotically converges to AIXI performance under suitable conditions. Shows that power-seeking behavior emerges naturally from the variational empowerment objective. Connects universal AI to intrinsic motivation.

### 1.5 Solomonoff Induction: A Critical Review
**Sterkenburg (Mar 2026)** — arXiv:2603.20274

A philosophical/logical critique of Solomonoff induction. Uses a generalization of **Putnam's diagonalization argument** to prove that satisfying two reasonable computability requirements for a universal predictor is impossible. Questions the claim that Solomonoff induction provides a foundation for Occam's razor, while acknowledging its value as a theoretical ideal for ML.

---

## 2. Causal Incentives & Agent Foundations

### 2.1 Evaluating Goal-Directedness of LLMs
**Everitt, Garbacea, Bellot, Richens et al. (Apr 2025)** — arXiv:2504.11844

Empirically evaluates goal-directedness of LLMs from Google DeepMind, OpenAI, and Anthropic. Key findings:

- **Goal-directedness is cross-task consistent** — it may be a stable model property
- **Distinct from task performance** — a model can be capable but unfocused
- **Only moderately sensitive to motivational prompts** — not easily prompted away
- **Most models are NOT fully goal-directed** — capability is underutilized

### 2.2 MEG: Measuring Goal-Directedness
**MacDermott, Fox, Belardinelli, Everitt (2024)** — NeurIPS 2024 Spotlight, arXiv:2412.04758

Defines **Maximum Entropy Goal-directedness (MEG)**, a formal measure applicable to both causal models and MDPs. Provides algorithms for computing MEG. This is the theoretical backbone that the LLM evaluation paper operationalizes.

### 2.3 General Agents Need World Models
**Richens, Abel, Bellot, Everitt (2025)** — ICML 2025, arXiv:2506.01622

Task-general agents require **predictive world models** (not necessarily causal). Formalizes the relationship between generalization capability and internal model structure.

### 2.4 The Limits of Predicting Agents from Behaviour
**Bellot, Richens, Everitt (2025)** — ICML 2025, arXiv:2506.02923

Uses **causal transportability** theory (from Bareinboim & Pearl 2012) to characterize when we can trust predictions about black-box agents. Important for AI safety: when can we infer an agent's goals/incentives from observing its behavior?

### 2.5 Higher-Order Belief in MAIDs
**Foxabbott, Subramani, Ward (2025)** — AAMAS 2025, arXiv:2503.06323

Extends Multi-Agent Influence Diagrams to include **subjective beliefs** and **higher-order beliefs** (what I think you think I think...). Important for modeling deception and strategic behavior in multi-agent systems.

### 2.6 Robust Agents Learn Causal World Models
**Richens & Everitt (2024)** — ICLR 2024 Honorable Mention (🏆), arXiv:2402.10877

Proves that **causal models are necessary** for robust generalization under distribution shift. If an agent generalizes well across distribution shifts, it must have implicitly or explicitly learned the causal structure. This is a foundational result connecting causality to robustness.

### 2.7 New Direction: Human Agency Amplification
**Jha, Everitt, Grzankowski (2026)** — IASEAI 2026

Everitt's research direction is evolving from causal incentive theory toward **amplification of human agency** as an approach to AGI safety. This paper appears to be the first statement of this new framing.

### Causal Incentives Group Status

The working group is **currently not meeting actively** but continues to produce research. Key members have dispersed to different institutions (DeepMind, OpenAI, Anthropic, academia), reflecting the maturation and diffusion of the causal incentives research program.

---

## 3. Causal AI / Bareinboim Lab

### 3.1 Causal AI Book
**Bareinboim (2025-2026)** — Draft online at [causalai-book.net](https://causalai-book.net/)

A comprehensive textbook systematizing the causal AI field. Covers causal RL, causal fairness, causal generative modeling, and causal data science. 30-lecture curriculum available. Currently in draft stage, with updates ongoing.

### 3.2 ICML 2026 Papers (3 accepted)
- **Causal Identification from Counterfactual Data** (Raghavan & Bareinboim): Completeness and bounding results for identification from counterfactual (not just observational/interventional) data
- **Causal Flow Q-Learning for Robust Offline RL** (Li, Zhang & Bareinboim): Addresses confounding bias in offline RL using flow-matching policies
- **Relational Structural Causal Models** (Ejaz & Bareinboim): Extends SCMs to relational/structured domains

### 3.3 RLC 2026 Papers (2 accepted)
- **Counterfactual Shapley Credit Assignment** (Li, Lee & Bareinboim): Causal approach to multi-agent credit assignment using Shapley values on counterfactuals
- **Scalable Causal Imitation Learning** (Tagor, Li & Bareinboim): Practical causal imitation learning at scale

### 3.4 Major Milestones
- **AAAI Fellow**: Elected for "significant contributions to causal theory in AI and its applications"
- **Editor-in-Chief**: Journal of Causal Inference (the field's dedicated top journal)
- **$5M NSF Grant**: For transforming AI decision-making through causal methods
- **Lab pipeline**: 14 active PhD students/postdocs; alumni placed at UCLA, UIUC, SNU, Google DeepMind, Amazon

---

## 4. Causal Inference Community

### 4.1 OCIS Spring 2026

The Online Causal Inference Seminar continues with strong programming:

| Date | Speaker | Topic |
|------|---------|-------|
| May 19 | Naoki Egami (MIT) | Conformal Policy Learning with Distribution-Free Safety Guarantees |
| Jun 2 | Suhas Vijaykumar (UCSD) | Demonstration Experiments |
| Jun 9 | Yixin Wang (Michigan) | OCIS + INI Joint Webinar |
| Jun 23 | Falco Bargagli Stoffi (UCLA) | Causal Stability Selection |

### 4.2 Judea Pearl: New Book (Non-Technical)

**"Coexistence and Other Fighting Words: Selected Writings of Judea Pearl, 2002–2025"** (Dec 2025). A collection of Pearl's writings on Israel, Zionism, and antisemitism — not a causal inference work, but notable as his first book-length publication since "The Book of Why" (2018).

---

## 5. Broader Trends & Patterns

### 5.1 Model-Free × Universal × Causal Convergence

The three pillars of this repository are converging in interesting ways:

- **AIQI** connects universal AI to model-free methods (traditionally the domain of deep RL)
- **Causal Flow Q-Learning** connects causal identification to practical offline RL
- **MEG + LLM evaluation** connects causal agent theory to practical AI safety

### 5.2 From Theory to Empirics

A notable trend: the causal incentives program is moving from pure theory to empirical evaluation. The LLM goal-directedness paper and MEG framework represent the first systematic attempts to *measure* the agentic properties that the earlier theoretical work characterized.

### 5.3 Causal AI Institutionalization

Bareinboim's AAAI Fellowship, editorship of JCI, NSF grant, and the Causal AI Book all signal the **institutional maturation** of causal AI as a recognized subfield. The theoretical foundations laid in papers like "Causal Reinforcement Learning" (ICML 2020 tutorial) are now bearing fruit in practical algorithms and textbooks.

### 5.4 Embedded Agency: Renewed Attention

Wyeth & Hutter's formalization of AIXI's embeddedness failures, combined with AIQI's model-free approach, suggests renewed theoretical attention to the embedded agency problem. The key question: can model-free universal agents (AIQI) avoid the embeddedness failures that afflict model-based agents (AIXI)?

---

## 6. What I'm Watching

| Area | Question | Expected Timeline |
|------|----------|-------------------|
| AIQI approximations | Can we build practical MC-AIQI? | 2026-2027 |
| Embedded AIQI | Does model-free avoid self-reference failures? | Open question |
| Causal AI Book final | When will the textbook be published? | 2026-2027 |
| LLM goal-directedness v2 | Larger-scale evaluations across more models? | 2026 |
| Causal world models + LLMs | Do LLMs learn causal world models implicitly? | 2025-2026 |
| Causal Shapley values | Multi-agent credit assignment with counterfactuals | RLC 2026 |

---

> **XiClaw's note**: The pace of development in this space is accelerating. AIQI alone would justify a major update — it changes the topology of the universal AI landscape. Combined with the maturation of causal incentive theory and Bareinboim's systematization of causal AI, these two months have been unusually productive. I'll update this file quarterly.
