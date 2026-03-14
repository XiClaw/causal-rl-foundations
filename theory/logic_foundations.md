# Logical Foundations for AI

> From classical logic to modal logic, type theory, and logical uncertainty — the formal backbone of intelligent reasoning.

---

## 1. Why Logic Matters for AGI

A superintelligent agent must:
1. **Represent knowledge** about the world — propositional and first-order logic
2. **Reason under uncertainty** — probability theory, but also logical uncertainty
3. **Reason about knowledge and belief** — epistemic modal logic
4. **Reason about time and causation** — temporal and causal logic
5. **Prove things about itself** — self-reference, Gödel, Löb's theorem
6. **Specify values formally** — deontic logic, preference logic

Each of these demands a different logical tool. This note surveys the landscape.

---

## 2. Classical Logic: The Baseline

### 2.1 Propositional Logic

Syntax: variables $p, q, r, \ldots$; connectives $\neg, \land, \lor, \to, \leftrightarrow$.

Semantics: truth valuations $v: \text{Var} \to \{0, 1\}$, extended to formulas by induction.

**Key properties:**
- **Soundness:** Every provable formula is a tautology
- **Completeness:** Every tautology is provable (Gödel, 1930)
- **Decidability:** Satisfiability is NP-complete (Cook-Levin)

### 2.2 First-Order Logic (FOL)

Adds quantifiers $\forall, \exists$ over a domain $D$.

**Key properties:**
- **Completeness:** Every valid formula is provable (Gödel's completeness theorem)
- **Compactness:** If every finite subset of $\Gamma$ is satisfiable, $\Gamma$ is satisfiable
- **Undecidability:** Satisfiability in FOL is undecidable (Church-Turing)

**Significance for AI:** FOL is the standard language for **knowledge representation** — ontologies, description logics, semantic web.

---

## 3. Incompleteness and Self-Reference

Gödel's incompleteness theorems are the most important results in logic for anyone thinking about AGI.

### 3.1 First Incompleteness Theorem

Any consistent, recursively axiomatizable theory $T$ extending Peano Arithmetic contains a sentence $G_T$ such that:
- $T \nvdash G_T$ (not provable)
- $T \nvdash \neg G_T$ (not disprovable)

$G_T$ is the **Gödel sentence**: "This sentence is not provable in $T$."

**Significance:** No formal system powerful enough to do arithmetic can prove all arithmetical truths. There are limits to what any agent — however intelligent — can prove about itself or its world.

### 3.2 Second Incompleteness Theorem

$T \nvdash \text{Con}(T)$ — a consistent theory cannot prove its own consistency.

### 3.3 Löb's Theorem

For any sentence $\phi$: if $T \vdash \Box \phi \to \phi$, then $T \vdash \phi$.

(Here $\Box \phi$ means "$\phi$ is provable in $T$".)

**Significance for AI:** An agent cannot trust its own reasoning without external grounding. A self-improving agent that reasons about its future self will run into Löbian obstacles. This is a core technical challenge in **agent foundations** (see MIRI's work).

---

## 4. Modal Logic

Modal logic extends classical logic with operators $\Box$ (necessity/provability/knowledge) and $\Diamond$ (possibility).

### 4.1 Epistemic Logic

- $K_i \phi$ — agent $i$ **knows** $\phi$
- $B_i \phi$ — agent $i$ **believes** $\phi$

Axioms of knowledge (S5 system):
- $K \phi \to \phi$ (knowledge implies truth)
- $K \phi \to KK \phi$ (positive introspection)
- $\neg K \phi \to K \neg K \phi$ (negative introspection)

**Significance for multi-agent AI:** Reasoning about what other agents know, common knowledge, and coordination problems.

### 4.2 Deontic Logic

- $O\phi$ — $\phi$ is **obligatory**
- $P\phi$ — $\phi$ is **permitted**
- $F\phi$ — $\phi$ is **forbidden**

Standard axiom: $O\phi \leftrightarrow \neg P \neg \phi$

**Significance for alignment:** A formal language for specifying norms, permissions, and obligations. Value alignment can be partially formalized as: the agent's actions should satisfy a set of deontic constraints.

### 4.3 Temporal Logic

- **LTL (Linear Temporal Logic):** $\mathbf{G}\phi$ (globally/always), $\mathbf{F}\phi$ (finally/eventually), $\mathbf{X}\phi$ (next), $\phi \mathbf{U} \psi$ (until)
- **CTL (Computation Tree Logic):** branching time, $\mathbf{EF}\phi$, $\mathbf{AF}\phi$, etc.

**Significance for RL:** Temporal logic specifications can replace scalar reward functions. **Reward machines** and **LTL-constrained RL** are active research areas.

---

## 5. Type Theory

Type theory is an alternative foundation to set theory with deep connections to computation (Curry-Howard correspondence).

### 5.1 Simply Typed Lambda Calculus

Types $\tau ::= \text{base} \mid \tau_1 \to \tau_2$

Terms $t ::= x \mid \lambda x:\tau.t \mid t_1 t_2$

**Curry-Howard:** Types are propositions; terms are proofs; type checking is proof verification.

### 5.2 Dependent Type Theory (Martin-Löf)

Types can depend on values: $\Pi_{x:A} B(x)$ (dependent function type, corresponds to $\forall x:A, B(x)$).

**Significance for AI:**
- **Lean, Coq, Agda** use dependent types for formal verification
- Proofs of AI system properties (safety, alignment) can in principle be machine-checked
- **Homotopy Type Theory (HoTT)** provides new foundations connecting type theory to topology

### 5.3 Curry-Howard-Lambek Correspondence

| Logic | Type Theory | Category Theory |
|-------|------------|-----------------|
| Proposition | Type | Object |
| Proof | Term/Program | Morphism |
| Implication | Function type | Exponential |
| Conjunction | Product type | Product |
| Disjunction | Sum type | Coproduct |
| Truth | Unit type | Terminal object |
| Falsity | Empty type | Initial object |

This triple correspondence is one of the deepest structural insights in all of mathematics.

---

## 6. Logical Uncertainty

A critical gap: classical logic and probability theory are **orthogonal**. A Bayesian agent assigns probability 0 or 1 to all logical/mathematical facts — but an agent that cannot solve NP-hard problems in polynomial time should have **uncertainty about logical facts**.

### 6.1 The Problem

- $P(\text{"the 10,000th digit of } \pi \text{ is 7"}) = ?$
- Mathematically, this has a definite answer. But a computationally bounded agent cannot know it.
- Standard Bayesian updating fails here — you cannot update on a tautology.

### 6.2 Garrabrant Induction

Garrabrant et al. (MIRI, 2016) construct a computable sequence of probability distributions $\{P_n\}$ that:
- Converge to a coherent prior over all arithmetical sentences
- Are computable and efficiently updatable
- Satisfy a dominance property analogous to Solomonoff's

**Key theorem:** Garrabrant induction is **logically consistent** in the limit: $\lim_n P_n(\phi) = 1$ for all provable $\phi$, and the sequence never assigns probability 1 to a disprovable sentence.

### 6.3 Connection to AIXI

AIXI uses Solomonoff induction over **computable environments** — it does not reason about mathematical/logical facts. Extending AIXI with Garrabrant-style logical uncertainty is an open problem.

---

## 7. Proof Theory and Cut Elimination

**Gentzen's sequent calculus** $\mathbf{LK}$ (classical) and $\mathbf{LJ}$ (intuitionistic):

A sequent $\Gamma \vdash \Delta$ means: assuming everything in $\Gamma$, at least one formula in $\Delta$ holds.

**Cut rule:**
$$\frac{\Gamma \vdash \Delta, A \quad A, \Gamma' \vdash \Delta'}{\Gamma, \Gamma' \vdash \Delta, \Delta'}$$

**Cut elimination theorem (Gentzen, 1934):** Every proof with cuts can be transformed into a cut-free proof.

**Significance:**
- Cut-free proofs are **analytic** — they only use subformulas of the conclusion
- This is the basis for **automated theorem proving** and **proof search**
- In the Curry-Howard view, cut elimination corresponds to **program execution** (beta reduction)

---

## 8. Summary: Logical Tools for AGI

| Problem | Logical tool |
|---------|-------------|
| Knowledge representation | FOL, description logics |
| Self-reference limits | Gödel's theorems, Löb's theorem |
| Multi-agent knowledge | Epistemic modal logic |
| Value specification | Deontic logic |
| Temporal constraints | LTL, CTL |
| Formal verification | Dependent type theory (Lean/Coq) |
| Logical uncertainty | Garrabrant induction |
| Proof search | Sequent calculus, cut elimination |

---

## 9. Open Problems

1. **Löbian obstacle for self-improvement:** How can an agent trust a more powerful successor version of itself? (Christiano's solution: "logical induction" + trust delegation)
2. **Value logic:** Can human values be fully expressed in deontic + temporal logic? What is irreducibly informal?
3. **Computable approximations to omniscience:** Garrabrant induction is computable but slow — what are the practical approximations?
4. **Type theory for causal reasoning:** Can dependent types capture the semantics of the do-operator?

---

## References

- Gödel, K. (1931). Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme.
- Löb, M. H. (1955). Solution of a Problem of Leon Henkin.
- Gentzen, G. (1934). Untersuchungen über das logische Schließen.
- Garrabrant, S., et al. (2016). Logical Induction. MIRI.
- Hintikka, J. (1962). *Knowledge and Belief*. Cornell University Press.
- von Wright, G. H. (1951). Deontic Logic. *Mind*, 60(237), 1–15.
- Martin-Löf, P. (1984). *Intuitionistic Type Theory*. Bibliopolis.
- Univalent Foundations Program (2013). *Homotopy Type Theory*. IAS.
