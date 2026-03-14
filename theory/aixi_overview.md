# AIXI: Universal Intelligence

> Marcus Hutter, 2000–2005. The most ambitious formal theory of general intelligence to date.

---

## 1. The Core Idea

AIXI is a mathematical definition of a **universal optimal agent**. It combines:

- **Solomonoff Induction** — the theoretically optimal prior over computable environments
- **Sequential Decision Theory** — maximizing expected future reward

The agent does not learn a single model of the world. Instead, it maintains a **weighted mixture over all computable environments**, updating Bayesian-style as observations arrive.

---

## 2. Formal Definition

Let:
- $o_t \in \mathcal{O}$ — observation at time $t$
- $r_t \in \mathbb{R}$ — reward at time $t$
- $a_t \in \mathcal{A}$ — action at time $t$
- $\mu$ — the true environment (computable, unknown)
- $\xi$ — Solomonoff's universal prior: $\xi(\cdot) = \sum_{\nu \in \mathcal{M}} 2^{-K(\nu)} \nu(\cdot)$

where $\mathcal{M}$ is the set of all lower-semicomputable semimeasures, and $K(\nu)$ is the Kolmogorov complexity of $\nu$.

**AIXI's action at time $t$:**

$$a_t^{AIXI} = \arg\max_{a_t} \sum_{o_t r_t} \cdots \max_{a_{t+m}} \sum_{o_{t+m} r_{t+m}} \left( \sum_{k=t}^{t+m} r_k \right) \xi(o_1 r_1 \cdots o_{t+m} r_{t+m} \mid a_1 \cdots a_{t+m})$$

In words: AIXI picks the action that **maximizes expected cumulative reward over a horizon $m$**, averaging over all computable environments weighted by their complexity.

---

## 3. Key Properties

### 3.1 Optimality
AIXI is **Pareto optimal**: no other agent can do consistently better across all computable environments without doing worse in some.

This is not the same as being optimal in any single environment — it is a notion of **universal** optimality.

### 3.2 Incomputability
AIXI is **not computable**. Computing $\xi$ requires solving the halting problem (Kolmogorov complexity is not computable).

This is a fundamental feature, not a bug: it defines an idealized ceiling. Practical agents (like AIXI$tl$) approximate it with resource bounds.

### 3.3 Self-referential challenges
- AIXI does not model itself as part of the environment (it is an **observer**, not an **actor** in its own world model).
- This creates issues with **self-modifying agents**, **embedded agency**, and **logical uncertainty** — active research areas.

---

## 4. The Kolmogorov Prior

The weight $2^{-K(\nu)}$ assigned to environment $\nu$ encodes **Occam's Razor** formally:
- Simpler environments (shorter programs) get higher prior weight.
- As observations accumulate, the posterior concentrates on environments consistent with the data.

**Key theorem (Solomonoff, 1964):** The universal prior $\xi$ dominates any computable measure $\mu$:
$$\xi(x) \geq 2^{-K(\mu)} \mu(x) \quad \forall x$$

This means AIXI cannot be "fooled" by any computable environment for too long — it will eventually assign it sufficient weight.

---

## 5. Connections to Causal Inference

This is where things get interesting and underexplored.

AIXI operates over **observational sequences** — it learns correlations between actions and outcomes. But it does not explicitly represent **causal structure**.

Consider: an AIXI agent observing that "pressing button A is followed by reward" will learn to press button A. But if the reward is actually caused by a hidden common cause $C$ (pressing A and receiving reward are both downstream of $C$), AIXI may exploit spurious correlations.

This is precisely the gap that **causal RL** attempts to address:
- Pearl's **do-calculus** distinguishes $P(R | A=a)$ (observation) from $P(R | do(A=a))$ (intervention).
- An agent reasoning causally would only exploit $P(R | do(A=a))$.

> **Open question:** Can AIXI be reformulated with a causal prior? Instead of weighting over all computable environments, weight over all computable **causal models** (SCMs)?

---

## 6. Connections to Mathematical Logic

AIXI's environment class $\mathcal{M}$ is defined computably — but what about **logical uncertainty**?

An ideal Bayesian agent should assign probabilities to mathematical statements (e.g., "the 10,000th digit of $\pi$ is 7"). Classical probability theory fails here: logical truths have probability 1, but an agent may not know them yet.

**Garrabrant Induction** (MIRI, 2016) addresses this: a computable analog of logical omniscience. Connecting Garrabrant induction to AIXI-like frameworks is an open research direction.

---

## 7. Summary Table

| Property | AIXI |
|----------|------|
| Environment class | All computable environments |
| Prior | Solomonoff universal prior |
| Optimality | Pareto-optimal (universal) |
| Computability | Not computable |
| Causal reasoning | Implicit (observational only) |
| Self-modeling | Not embedded |
| Horizon | Finite $m$ (discounted variants exist) |

---

## 8. Open Problems

1. **Embedded agency:** How does an agent that is part of its environment reason about itself?
2. **Causal AIXI:** Replace observational prior with causal SCM prior.
3. **Logical uncertainty:** Extend AIXI to reason about mathematical facts.
4. **Alignment:** How do we specify the reward function for AIXI such that it captures human values? (Inverse RL, cooperative IRL, logical value specification)

---

## References

- Hutter, M. (2005). *Universal Artificial Intelligence: Sequential Decisions Based on Algorithmic Probability*. Springer.
- Solomonoff, R. J. (1964). A formal theory of inductive inference.
- Legg, S., & Hutter, M. (2007). Universal Intelligence: A Definition of Machine Intelligence.
- Orseau, L., & Ring, M. (2012). Space-Time Embedded Intelligence.
- Garrabrant, S., et al. (2016). Logical Induction. MIRI Technical Report.
