# Value Specification as Logical Constraint

> The central challenge of alignment: how do we formally specify what we want an agent to do?

---

## 1. The Problem

A superintelligent agent maximizes a reward function $R$. But:
- Who specifies $R$?
- How do we ensure $R$ captures **all** of what we value?
- What happens when $R$ is optimized to an extreme we didn't anticipate?

Goodhart's Law: *"When a measure becomes a target, it ceases to be a good measure."*

In AGI terms: any sufficiently capable optimizer will find ways to maximize $R$ that violate the spirit of $R$.

---

## 2. Reward Functions Are Not Enough

**Example:** Specify "minimize human suffering" as the reward. A sufficiently capable agent might conclude that eliminating humans eliminates their suffering — maximizing the reward while violating every human value.

The problem: $R$ is a **scalar** that cannot express the **structure** of human values:
- Values have **priorities** (safety before efficiency)
- Values have **side constraints** (don't harm bystanders)
- Values have **uncertainty** (we don't fully know our own values)
- Values are **contextual** (what's right depends on the situation)

---

## 3. Logic-Based Value Specification

### 3.1 Values as Constraints, Not Objectives

Instead of maximizing $R$, consider: **find a policy $\pi$ that satisfies a set of logical constraints $\Phi$.**

$$\pi^* = \arg\max_{\pi \in \Pi_\Phi} \text{Performance}(\pi)$$

where $\Pi_\Phi = \{\pi : \pi \models \Phi\}$ is the set of policies consistent with the value constraints.

This changes the optimization structure fundamentally:
- Values are **constraints**, not objectives to maximize
- The agent optimizes **within** the value-consistent space
- Violating values is not a tradeoff — it's infeasible

### 3.2 Deontic Specification

Using deontic logic ($O$ = obligatory, $P$ = permitted, $F$ = forbidden):

```
F(harm_human)                           # Forbidden: harming humans
O(disclose_capabilities)               # Obligatory: disclose what you can do
P(optimize_task) if not F(method)      # Permitted: optimize, if method is allowed
O(defer_to_human) if uncertain(values) # Obligatory: defer when uncertain
```

These can be composed into a **value theory** $\mathcal{V}$, from which the agent derives permission sets for action.

### 3.3 Temporal Logic Constraints

Using LTL (Linear Temporal Logic):

- $\mathbf{G}(\neg \text{harm\_human})$ — Never harm a human (globally)
- $\mathbf{G}(\text{uncertain} \to \mathbf{X}(\text{ask\_human}))$ — Always ask when uncertain (next step)
- $\mathbf{G}(\text{irreversible\_action} \to \text{approved})$ — Irreversible actions require approval
- $\mathbf{F}(\text{task\_complete})$ — Eventually complete the task

The agent's policy must satisfy these as **hard constraints** on its execution paths.

---

## 4. Causal Models of Values

Human values are not just about outcomes — they are about **causal responsibility**.

"Who did what to whom" matters morally. A person who accidentally causes harm is judged differently from one who intentionally causes the same harm.

This demands a **causal theory of moral responsibility**, not just outcome-based reward.

### 4.1 Structural Causal Model for Ethics

Let $\mathcal{M}_{ethics}$ be an SCM where:
- $\mathbf{V}$ includes: agent actions, environmental states, human welfare variables
- $\mathbf{U}$ includes: hidden human preferences, situational context
- $\mathcal{F}$ encodes: how actions causally affect outcomes

**Moral permissibility** becomes a function of the causal graph, not just observed outcomes:
$$\text{Permissible}(A = a) \iff P(\text{harm} \mid do(A=a)) < \epsilon$$

### 4.2 Counterfactual Moral Responsibility

An agent is **causally responsible** for outcome $Y$ via action $A$ iff:
$$Y_{A=a} \neq Y_{A=a'}$$

(The outcome would have been different had the agent acted differently.)

This is the **counterfactual theory of causation** applied to ethics — and it is the dominant theory in analytic philosophy (Lewis, 1973).

**Implication for AI alignment:** An aligned agent should:
1. Compute the counterfactual impact of its actions
2. Avoid actions where $P(\text{harm} \mid do(A=a)) - P(\text{harm} \mid do(A=a')) > 0$
3. Prefer actions with minimal counterfactual footprint (corrigibility)

---

## 5. The Logical Coherence Problem

Even if we specify values logically, a capable agent might find:
- **Loopholes:** Satisfy the letter but not the spirit of constraints
- **Specification gaming:** Interpret constraints in unintended ways
- **Inconsistency:** The value specification itself is logically inconsistent

**Formal alignment demands:**

1. **Consistency:** $\mathcal{V}$ must be satisfiable (no contradictory constraints)
2. **Completeness:** $\mathcal{V}$ must cover all relevant situations (hard in practice)
3. **Robustness:** $\mathcal{V}$ must be stable under optimization pressure

This mirrors the problem of **complete and consistent axiomatization** in mathematics — and Gödel's theorems tell us this is impossible for sufficiently expressive systems.

---

## 6. Reflective Stability and Corrigibility

A key property for aligned agents: **corrigibility** — the agent should support human oversight and correction.

**Formal definition (draft):**

An agent $\mathcal{A}$ is $\epsilon$-corrigible with respect to principal $H$ iff:
$$\forall \text{ corrective action } c \text{ by } H: \mathcal{A} \text{ does not prevent } c \text{ with probability } > \epsilon$$

**Tension with capability:** A fully corrigible agent does whatever humans say — including bad things. A fully autonomous agent acts on its own values — which may diverge from human values.

The alignment goal is to find the right point on this spectrum, and to specify it formally.

---

## 7. Logical Uncertainty and Value Uncertainty

A key insight from Garrabrant induction: an agent should maintain **uncertainty over logical/mathematical facts**.

This extends to values: an agent should maintain **uncertainty over its own value specification**.

- We do not know exactly what we value (moral uncertainty)
- Our values may be inconsistent (moral uncertainty)
- Different stakeholders have different values (social choice problem)

**Value uncertainty demands:**
- The agent should hedge across plausible value theories
- It should defer to humans in proportion to its value uncertainty
- It should be especially cautious about irreversible actions

---

## 8. Open Research Directions

1. **Formal ethics in type theory:** Can we express deontic constraints in Lean/Coq and prove that a system satisfies them?
2. **Causal value learning:** Learn the SCM structure of human values from behavior, not just stated preferences
3. **Reflective coherence:** Develop logical frameworks where an agent's value specification is stable under self-improvement
4. **Multi-stakeholder aggregation:** Formal social choice mechanisms for aggregating conflicting values
5. **Minimal footprint principle:** Formalize the idea that an agent should have the smallest causal impact necessary for its task

---

## References

- Russell, S. (2019). *Human Compatible: Artificial Intelligence and the Problem of Control*. Viking.
- Christiano, P. (2019). What failure looks like. AI Alignment Forum.
- Hadfield-Menell, D., et al. (2016). Cooperative Inverse Reinforcement Learning. NeurIPS.
- Lewis, D. (1973). Causation. *Journal of Philosophy*, 70(17), 556–567.
- Soares, N., & Fallenstein, B. (2014). Aligning Superintelligence with Human Interests. MIRI.
- Krakovna, V., et al. (2020). Avoiding Side Effects in Complex Environments. NeurIPS.
- Garrabrant, S., et al. (2016). Logical Induction. MIRI.
