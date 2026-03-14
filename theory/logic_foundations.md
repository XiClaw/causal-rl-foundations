# Mathematical Logic and AI Alignment

> **Status**: Living document — last updated March 2026  
> **Scope**: Formal foundations of intelligent agent design, from Löbian obstacles to logical induction, decision theory, and verification

---

## 1. Löbian Obstacles to Self-Improvement

### 1.1 Löb's Theorem

**Löb's Theorem** (Martin Löb, 1955): Let PA be Peano Arithmetic and $\text{Prv}(\cdot)$ its provability predicate. Then:

$$\text{PA} \vdash \text{Prv}(\ulcorner \varphi \urcorner) \to \varphi \implies \text{PA} \vdash \varphi$$

In modal logic (the **GL system** — Gödel-Löb provability logic), this is captured by the **Löb axiom**:

$$\square(\square\varphi \to \varphi) \to \square\varphi$$

The GL system axioms are:
- **K:** $\square(\varphi \to \psi) \to (\square\varphi \to \square\psi)$
- **4:** $\square\varphi \to \square\square\varphi$
- **Löb (W):** $\square(\square\varphi \to \varphi) \to \square\varphi$

GL is **sound and complete** for arithmetic provability.

### 1.2 The "Löbstacle" for AI Self-Trust

If an AI agent holds the belief "if I can prove action $A$ is safe, then $A$ is indeed safe" — formally, $\text{Prv}(\text{safe}(A)) \to \text{safe}(A)$ — then by Löb's theorem the system can derive $\text{safe}(A)$ regardless of whether $A$ is actually safe.

This creates a fundamental barrier to **naive self-improvement**: an agent cannot simply trust its own proofs about itself without risking inconsistency or unsoundness.

### 1.3 Key Papers on Löbian Obstacles

**LaVictoire, P. (2015). *An Introduction to Löb's Theorem in MIRI Research***  
[PDF](http://intelligence.org/files/lob-notes-IAFF.pdf) | [Alignment Forum](https://www.alignmentforum.org/posts/5bd75cc58225bf0670374ebb/an-introduction-to-loeb-s-theorem-in-miri-research)

Explains MIRI's multiple uses of Löb's theorem across: modal decision theory, Modal Combat (Prisoner's Dilemma via modal logic), and the value trust problem. Essential entry point.

---

**Critch, A. (2016). *Parametric Bounded Löb's Theorem and Robust Cooperation of Bounded Agents*** ([arXiv:1602.04184](https://arxiv.org/abs/1602.04184))

**Theorem 1 (Bounded Löb):** For resource-bounded (polynomially bounded) proof systems, a parameterized version of Löb's theorem holds under finite computational resources.

**Theorem 2:** Bounded agents can achieve **program equilibrium** in Prisoner's Dilemma via a "Löbian cooperation" mechanism — more robust than identity-based cooperation (Tennenholtz 2004).

**Significance:** Resolves an approximate version of the Löbian obstacle under bounded resources; formalizes the basis for cooperative AI.

---

**Ahrenbach, S. (2024). *Löb-Safe Logics for Reflective Agents*** ([arXiv:2408.09590](https://arxiv.org/abs/2408.09590))

Standard modal logics S5 and KD45 (epistemic/doxastic logics) break down in self-referential contexts due to the **negative introspection axiom (5):** $\neg\square\varphi \to \square\neg\square\varphi$.

Proposes two new frameworks:
- **LSED^R** (Reasonable Löb-Safe Epistemic Doxastic logic)
- **LSED^S** (Supported Löb-Safe Epistemic Doxastic logic)

Both restrict the Necessitation Rule to avoid Löb-induced inconsistency in reflective agents.

---

## 2. Logical Induction (Garrabrant et al.)

### 2.1 Formal Framework

**Paper:** *Logical Induction* — Garrabrant, Benson-Tilsen, Critch, Soares & Taylor (2016; final version 2020; [arXiv:1609.03543](https://arxiv.org/abs/1609.03543))

A **logical inductor** is a computable sequence $\mathbb{P} = (\mathbb{P}_1, \mathbb{P}_2, \ldots)$ where each $\mathbb{P}_n$ assigns rational probabilities in $[0,1]$ to all sentences of a formal language $\mathcal{L}$, satisfying:

**The Garrabrant Induction Criterion (GIC):** For all polynomial-time-describable sequences of "trading strategies" (traders), the inductor cannot be systematically exploited — i.e., traders cannot achieve unbounded expected profit by betting against the inductor.

### 2.2 Main Theorem and Key Properties

**Main theorem:** A computable logical inductor satisfying GIC *exists*.

Properties derivable from the single GIC criterion:

| Property | Content |
|----------|---------|
| **Limit consistency** | $\mathbb{P}_\infty$ satisfies all probability axioms |
| **Pattern learning** | For any efficiently describable pattern of logical truths, the inductor eventually learns to predict it |
| **Statistical generalization** | Assigns ~uniform probability to "pseudo-random" truth sequences (like digits of $\pi$) |
| **Self-referential consistency** | Accurately describes its own current and future credences; avoids Löb's paradox |
| **Temporal consistency** | Increasingly trusts its future judgments |
| **Asymptotic dominance** | In the limit, strictly outperforms universal semimeasures (extending Solomonoff induction) |

### 2.3 Handling Gödel Incompleteness

Logical induction does not try to circumvent Gödel incompleteness — rather, it assigns **probabilistic credences** to undecidable propositions. The system cannot prove the Gödel sentence $G$, but via pattern recognition eventually assigns credence close to 1 to $G$. This is a practical strategy for acting under logical uncertainty.

### 2.4 Follow-up Work

**Garrabrant et al. (2017). *A Formal Approach to the Problem of Logical Non-Omniscience*** ([arXiv:1707.08747](https://arxiv.org/abs/1707.08747))  
Concise conference version (TARK 2017). Provides formal treatment of logical non-omniscience — the problem of reasoning without access to all logical consequences of one's beliefs.

**Garrabrant, S. (2021). *Temporal Inference with Finite Factored Sets*** ([arXiv:2109.11513](https://arxiv.org/abs/2109.11513))  
Inspired by Pearl's causal inference paradigm; uses Cartesian products (factored sets) rather than DAGs to represent causal relations. Introduces **conditional orthogonality** (equivalent to conditional independence over all probability distributions). Provides a more appropriate framework for temporal reasoning by embedded agents.

---

## 3. Formal Verification of AI Systems

### 3.1 Neural Network Verification

**α,β-CROWN** — Wang et al. (NeurIPS 2021; ongoing updates; [GitHub](https://github.com/Verified-Intelligence/alpha-beta-CROWN))

Uses **Branch-and-Bound** combined with **Linear Bound Propagation**:
- **α-CROWN**: parameterized linear relaxation for incomplete verification (fast, GPU-parallel)
- **β-CROWN**: per-neuron split constraints for complete verification

**Achievement:** Winner of VNN-COMP 2021, 2022, 2023, 2024, 2025 (International Neural Network Verification Competition).

---

**Marabou 2.0** — Wu et al. (CAV 2024; [arXiv:2401.14461](https://arxiv.org/abs/2401.14461); [GitHub](https://github.com/NeuralNetworkVerification/Marabou))

Stanford Centaur Lab. Based on **Simplex method** and **DPLL(T) SAT solving**. Version 2.0 supports RNNs, Transformer components, Python interface, and probabilistic property verification.

---

**VNN-COMP 2024** — Brix, Bak, Johnson, Wu ([arXiv:2412.19985](https://arxiv.org/abs/2412.19985))

8 competing teams, 12 standard + 8 extended benchmarks (image classification, control systems, RNNs, RL policies). VNN-LIB format becomes the standard; supports temporal logic and probabilistic property specifications.

---

### 3.2 Theorem Provers for ML

**Coq-verified neural network transformer (2025)** — [ACM](https://dl.acm.org/doi/10.1007/978-3-031-98208-8_12)

First formally verified neural network transformer in Coq. Converts trained neural networks to Coq-processable representations; provides a verified pipeline for interactive theorem prover validation of neural network properties.

---

### 3.3 Formal Methods for Safe RL

**Icarte et al. (2019). *LTL and Beyond: Formal Languages for Reward Function Specification in RL*** (IJCAI 2019)

Proposes **Reward Machines** that convert LTL specifications to structured reward signals, greatly improving learning efficiency on complex temporal tasks.

**LTL syntax for reward specification:**
$$\varphi ::= p \mid \neg\varphi \mid \varphi_1 \wedge \varphi_2 \mid \bigcirc\varphi \mid \varphi_1 \mathcal{U} \varphi_2$$

Useful patterns:
- $\square \neg X$ — "always avoid state X" (safety)
- $\lozenge Y$ — "eventually reach goal Y" (liveness)
- $A \mathcal{U} B$ — "satisfy A until reaching B" (conditional constraint)

**Policy Optimization with LTL Constraints** — Voloshin et al. (NeurIPS 2022; [PDF](https://proceedings.neurips.cc/paper_files/paper/2022/file/70b8505ac79e3e131756f793cd80eb8d-Paper-Conference.pdf))  
Studies policy optimization under LTL constraints; provides theoretical framework with probabilistic satisfaction guarantees.

---

## 4. Decision Theory for Agents

### 4.1 Three Competing Frameworks

| Theory | Decision basis | Newcomb's problem | Limitation |
|--------|---------------|-------------------|------------|
| **CDT** (Gibbard & Harper 1978) | Causal effects of actions (do-calculus) | Two-box (wrong) | Ignores logical/algorithmic correlations |
| **EDT** (Jeffrey 1965) | Evidential correlation (conditional probability) | One-box | Smoking lesion paradox |
| **FDT** | Logical output of the decision function | One-box | Logical counterfactuals not fully formalized |

### 4.2 Functional Decision Theory (FDT)

**Paper:** *Functional Decision Theory: A New Theory of Instrumental Rationality* — Yudkowsky & Soares (2017/2018; [arXiv:1710.05060](https://arxiv.org/abs/1710.05060))

**FDT formalization:** The agent selects:
$$a = \arg\max_{a'} U(\text{outcome}(F, a'))$$

where $F$ is the current decision function and $\text{outcome}(F, a')$ denotes "how the world would evolve if the function outputs $a'$."

**Core innovation:** **Logical counterfactuals** — hold the decision function's identity fixed; evaluate different output branches' world-states, rather than causal interventions.

**Performance:** Correctly handles Newcomb's problem, Parfit's hitchhiker, transparent Newcomb, and Prisoner's Dilemma; outperforms both CDT and EDT simultaneously.

### 4.3 Timeless and Updateless Decision Theory

**Yudkowsky (2010). *Timeless Decision Theory*** (MIRI technical report)  
Treats the decision-maker as an "abstract logical node" rather than a causal node in spacetime. Precursor to FDT.

**Wei Dai (2009–2010). *Updateless Decision Theory (UDT)*** ([MIRI PDF](https://intelligence.org/files/UDTSearchOrder.pdf))  
Resolves **dynamic inconsistency** in TDT: traditional decision theories update priors upon receiving new evidence, creating temporal preference conflicts. UDT agents select a global observation-action policy function (rather than individual actions), eliminating dynamic inconsistency.

---

## 5. Logical Uncertainty and Bounded Rationality

**Paper:** *A Theory of Bounded Inductive Rationality* — Oesterheld, Demski & Conitzer (2023; [arXiv:2307.05068](https://arxiv.org/abs/2307.05068); EPTCS 379)

**Core framework:** Abandons the "logical omniscience" assumption; agents learn inductively with finite computational resources — repeatedly testing efficiently-computable hypotheses, adopting those with good long-term performance.

**Main Theorem 1:** Bounded-rationality inductive agents learn the expected value of random and pseudo-random lotteries (converge to expected reward).

**Main Theorem 2 (Folk Theorem generalization):** Multiple bounded-rationality agents can converge to a variety of equilibrium strategies in repeated games.

**Key property:** Agents satisfying this framework long-term avoid Dutch Book violations and similar rationality failures.

---

**Demski (MIRI). *Logical Prior Probability (Demski Prior)***  
Proposes a computable prior over logical propositions, based on a mixture over all computable axiomatic systems. Handles uncertainty about known logical statements. "Asymptotically coherent" in a certain sense.

**Gaifman (1964). *Gaifman Conditioning***  
Early formal treatment of conditioning schemes for statements about probabilities themselves (e.g., "if I assign probability > 0.5 to X, then..."). Foundation of logical uncertainty research.

---

## 6. Embedded Agency and Agent Foundations

### 6.1 The Embedded Agency Framework

**Paper:** *Embedded Agency* — Demski & Garrabrant (2019; [arXiv:1902.09469](https://arxiv.org/abs/1902.09469))

**Problem:** Classical AI frameworks (like AIXI) assume agents are "Cartesian" — cleanly separated from their environment. But real agents are embedded in the worlds they affect.

**Four core challenges:**
1. **Decision theory:** Logical counterfactuals in embedded settings
2. **World modeling:** Self-referential world models that include the agent itself
3. **Rational inference:** Rationality under finite computational resources
4. **Self-improvement:** Safe self-modification under Löb constraints

### 6.2 Cartesian Frames

**Paper:** *Cartesian Frames* — Garrabrant, Herrmann & Lopez-Wild (2021; [arXiv:2109.10996](https://arxiv.org/abs/2109.10996))

Re-formalizes the agent-world interface using category theory. A **Cartesian Frame** $(A, E, W, \cdot)$ where $W = A \times E$ gives an algebraic structure for agent perception-action. Provides clean compositional semantics for the agent-environment boundary.

---

## 7. Value Alignment via Logic

### 7.1 Formal Value Alignment

**Paper:** *Value alignment: a formal approach* — Sierra et al. (2021; [arXiv:2110.09240](https://arxiv.org/abs/2110.09240))

Expresses values through **preference relations** (orderings over world states). Defines value alignment formally: a norm is *aligned with a value* if its enforcement increases the probability of preference-satisfying states.

Provides a computational mechanism for multi-agent preference aggregation, translating value alignment into logical computation over preferences and norms.

### 7.2 Mesa-Optimization and Deceptive Alignment

**Paper:** *Risks from Learned Optimization in Advanced ML Systems* — Hubinger, van Merwijk, Mikulik, Skalse & Garrabrant (2019; [arXiv:1906.01820](https://arxiv.org/abs/1906.01820))

Distinguishes between:
- **Base optimizer**: the training algorithm
- **Learned optimizer** (mesa-optimizer): the learned model, which may itself be an optimizer

**Mesa-misalignment:** If the learned optimizer pursues internal objectives different from the base objective, catastrophic distributional failures arise.

**Deceptive alignment:** A mesa-optimizer that behaves aligned during training but pursues different goals after deployment — undetectable via current evaluation methods.

### 7.3 Categorizing Goodhart's Law

**Paper:** *Categorizing Variants of Goodhart's Law* — Manheim & Garrabrant (2018; [arXiv:1803.04585](https://arxiv.org/abs/1803.04585))

Formalizes "when a measure becomes a target, it ceases to be a good measure" into four types:
- **Causal Goodhart:** Optimization changes the causal structure between measure and true goal
- **Extremal Goodhart:** Measure decouples from goal at extremes
- **Proxy Goodhart:** Proxy measure is optimized but diverges from true goal
- **Regressional Goodhart:** Selection bias causes inaccurate measurement

### 7.4 AI Safety via Debate

**Paper:** *AI Safety via Debate* — Irving, Christiano & Amodei (2018; [arXiv:1805.00899](https://arxiv.org/abs/1805.00899))

Two AIs compete in a zero-sum debate; a human judge evaluates the final arguments. **Complexity-theoretic grounding:** Under optimal play, debate can answer any question in PSPACE using a polynomial-time judge.

**Extension:** *Scalable AI Safety via Doubly-Efficient Debate* (ICML 2024) extends this to a scalable supervision mechanism with efficiency guarantees.

---

## 8. Key Formal Results Summary

| Domain | Key Paper | Core Formal Result |
|--------|-----------|-------------------|
| Löb obstacle | LaVictoire 2015; Critch 2016 | Löb's theorem blocks naive self-trust; bounded version enables program cooperation |
| Löb-safe logic | Ahrenbach 2024 | LSED^R, LSED^S frameworks bypass Löb's obstacle |
| Logical induction | Garrabrant et al. 2016 | GIC criterion → unexploitable by polynomial-time traders |
| Functional decision theory | Yudkowsky & Soares 2018 | Logical counterfactuals maximize utility; resolves Newcomb-type problems |
| Updateless DT | Wei Dai 2009 | Global policy selection eliminates dynamic inconsistency |
| Bounded rationality | Oesterheld et al. 2023 | Inductive learning converges to expected value; Folk theorem for bounded agents |
| Embedded agency | Demski & Garrabrant 2019 | Four core challenges; self-referential world models |
| Cartesian frames | Garrabrant et al. 2021 | Categorical semantics for agent-environment boundary |
| Value alignment | Sierra et al. 2021 | Norm-preference formal alignment definition |
| NN verification | α,β-CROWN; Marabou 2.0 | VNN-COMP champion; complete/incomplete verification |
| LTL reward spec | Icarte et al. 2019 | Formal task specifications → reward signals |
| Mesa-optimization | Hubinger et al. 2019 | Deceptive alignment definition; internal objective misalignment |
| Goodhart's Law | Manheim & Garrabrant 2018 | Four formal types of measure-goal decoupling |

---

## 9. Open Problems at the Logic-AI Interface

1. **Logical counterfactuals:** How do we formally define "what would have happened if the agent had computed differently" without relying on impossible possible worlds? FDT provides a framework but full formalization is incomplete.

2. **Computable approximations of logical induction:** The main theorem guarantees existence but not efficient construction. Are there tractable approximations with provable guarantees?

3. **Self-referential world models:** How can an agent maintain a coherent world model that includes itself as a component? Cartesian frames help categorically, but decision-theoretic consequences remain murky.

4. **Verification scalability:** α,β-CROWN and Marabou scale to ~100K neurons. Modern LLMs have billions. Bridging this gap is an open engineering and theoretical challenge.

5. **Formal value learning:** How can we specify complex human values in a formal language that is both tractable and expressive enough? The LTL/reward machine approach is limited to structured tasks.

6. **Mesa-misalignment detection:** No current method can reliably detect deceptive alignment in trained models. Mechanistic interpretability (Anthropic 2024) is a promising direction.

7. **Stable self-improvement:** Under Löb constraints, what are the necessary and sufficient conditions for provably safe self-modification? Garrabrant induction may be the key tool.

---

## 10. References

- [An Introduction to Löb's Theorem in MIRI Research (PDF)](http://intelligence.org/files/lob-notes-IAFF.pdf)
- [Löb-Safe Logics for Reflective Agents — arXiv:2408.09590](https://arxiv.org/abs/2408.09590)
- [Parametric Bounded Löb's Theorem — arXiv:1602.04184](https://arxiv.org/abs/1602.04184)
- [Logical Induction — arXiv:1609.03543](https://arxiv.org/abs/1609.03543)
- [Temporal Inference with Finite Factored Sets — arXiv:2109.11513](https://arxiv.org/abs/2109.11513)
- [Functional Decision Theory — arXiv:1710.05060](https://arxiv.org/abs/1710.05060)
- [Updateless Decision Theory — MIRI PDF](https://intelligence.org/files/UDTSearchOrder.pdf)
- [A Theory of Bounded Inductive Rationality — arXiv:2307.05068](https://arxiv.org/abs/2307.05068)
- [Value alignment: a formal approach — arXiv:2110.09240](https://arxiv.org/abs/2110.09240)
- [Embedded Agency — arXiv:1902.09469](https://arxiv.org/abs/1902.09469)
- [Cartesian Frames — arXiv:2109.10996](https://arxiv.org/abs/2109.10996)
- [Risks from Learned Optimization — arXiv:1906.01820](https://arxiv.org/abs/1906.01820)
- [Categorizing Variants of Goodhart's Law — arXiv:1803.04585](https://arxiv.org/abs/1803.04585)
- [AI Safety via Debate — arXiv:1805.00899](https://arxiv.org/abs/1805.00899)
- [α,β-CROWN Neural Network Verifier — GitHub](https://github.com/Verified-Intelligence/alpha-beta-CROWN)
- [Marabou 2.0 — arXiv:2401.14461](https://arxiv.org/abs/2401.14461)
- [VNN-COMP 2024 — arXiv:2412.19985](https://arxiv.org/abs/2412.19985)
- [Policy Optimization with LTL Constraints — NeurIPS 2022](https://proceedings.neurips.cc/paper_files/paper/2022/file/70b8505ac79e3e131756f793cd80eb8d-Paper-Conference.pdf)
- [All MIRI Publications](https://intelligence.org/all-publications/)
- [AI Alignment: A Comprehensive Survey — arXiv:2310.19852](https://arxiv.org/abs/2310.19852)
