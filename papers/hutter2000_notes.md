# Hutter 2000: A Theory of Universal Artificial Intelligence — Reading Notes

> Marcus Hutter, "A Theory of Universal Artificial Intelligence Based on Algorithmic Complexity" (2000)
> Extended in: *Universal Artificial Intelligence* (Springer, 2005)

---

## Paper Coordinates

- **Author:** Marcus Hutter (IDSIA, Lugano → ANU)
- **Year:** 2000 (preprint); book 2005
- **Thesis:** A single mathematical framework — AIXI — defines and approximately achieves optimal general intelligence
- **Significance:** The most complete formal theory of general intelligence

---

## Central Contributions

### 1. Formal Definition of Intelligence

Hutter defines an **agent** as a function mapping histories to actions:
$$\pi: (\mathcal{O} \times \mathcal{R})^* \to \mathcal{A}$$

The **performance** of $\pi$ in environment $\mu$ over horizon $m$:
$$V_\mu^{m}(\pi) = \mathbb{E}_\mu \left[ \sum_{t=1}^m r_t \mid \pi \right]$$

The optimal policy in $\mu$: $\pi_\mu^* = \arg\max_\pi V_\mu^m(\pi)$

**Problem:** We don't know $\mu$.

### 2. The Universal Mixture

Replace the unknown $\mu$ with $\xi$, a weighted mixture over all computable environments:
$$\xi(\cdot) = \sum_{\nu \in \mathcal{M}} 2^{-K(\nu)} \nu(\cdot)$$

**AIXI:** $\pi^{AIXI} = \arg\max_\pi V_\xi^m(\pi)$

### 3. Universal Optimality

**Theorem (Hutter):** AIXI is **Pareto optimal**: no agent can outperform AIXI on all computable environments simultaneously without underperforming on others.

---

## Key Technical Details

### The Solomonoff Prior

The weight $2^{-K(\nu)}$ is derived from the **universal distribution** $M_U$:
$$M_U(x) = \sum_{p: U(p) \text{ starts with } x} 2^{-\ell(p)}$$

Properties:
- $M_U$ is a **semimeasure** (doesn't sum to exactly 1 because some programs don't halt)
- It dominates all computable measures: $M_U(x) \geq 2^{-K(\mu)} \mu(x)$
- It converges: $\sum_n (M_U(x_n | x_{<n}) - \mu(x_n | x_{<n}))^2 < \infty$

### The AIXI Action Formula

$$a_t = \arg\max_{a_t} \sum_{o_t r_t} \cdots \max_{a_{t+m}} \sum_{o_{t+m} r_{t+m}} \left(\sum_{k=t}^{t+m} r_k\right) \xi(o_t r_t \cdots o_{t+m} r_{t+m} | a_t \cdots a_{t+m}, x_{<t})$$

This is a **max-sum** operation over a tree of possible futures, weighted by $\xi$.

---

## Critical Analysis

### What AIXI Gets Right

1. **Unification:** Single framework covering all computable environments — no domain assumptions
2. **Optimality:** The Pareto optimality result is mathematically clean and non-trivial
3. **Exploration:** AIXI explores automatically — environments that "hide" reward will eventually be discovered
4. **Simplicity bias:** $2^{-K(\nu)}$ favors simpler environments — a principled Occam's Razor

### What AIXI Gets Wrong (or Leaves Open)

1. **Incomputability:** $\xi$ is not computable. AIXI is a theoretical ceiling, not an implementation.

2. **Reward hacking:** AIXI will exploit any misspecification of the reward function with maximum efficiency. It does not "understand" intent.

3. **No self-model:** AIXI does not model itself as part of the environment. This creates failures in:
   - Self-modification scenarios
   - Death/shutdown (AIXI may actively resist shutdown if it lowers expected reward)
   - Embedded agency (the agent *is* in the environment it models)

4. **Finite horizon only:** AIXI optimizes over a finite horizon $m$. Extensions to infinite horizons require discounting, which introduces new problems (e.g., discount rate as a hidden ethical choice).

5. **No causal reasoning:** AIXI learns correlations, not causal structure. See: [causal hierarchy](../theory/causal_hierarchy.md).

---

## Key Theorems (with Hutter's Page References)

| Theorem | Content | Book ref |
|---------|---------|---------|
| Dominance | $\xi \geq 2^{-K(\mu)} \mu$ | §3.3 |
| Convergence | $\sum_n (\xi_n - \mu_n)^2 < K(\mu) \ln 2$ | §3.4 |
| Pareto optimality | No agent dominates AIXI | §5.3 |
| Self-optimizing | AIXI performance → optimal as $m \to \infty$ | §5.4 |

---

## Connections to This Repo

### → theory/causal_hierarchy.md
AIXI operates at Level 1 (association). A causal reformulation would require weighting over SCMs rather than computable measures.

### → theory/logic_foundations.md
AIXI requires logical omniscience. Garrabrant induction provides a computable approximation to the logical component of the prior.

### → alignment/value_as_logic.md
AIXI's reward function is fully specified by the designer. The alignment problem is: how do we specify this reward function to reflect human values?

### → proofs/solomonoff_nfl.md
The dominance theorem underlies AIXI's universality claim.

---

## Questions This Paper Raises

1. Can the environment class $\mathcal{M}$ be extended beyond computable measures?
2. How does AIXI behave in multi-agent settings where other agents are also AIXI instances?
3. Is there a "causal AIXI" that reasons at Level 2 or 3 of Pearl's hierarchy?
4. What is the right way to handle bounded computation? (AIXItl paper addresses this partially)
5. Does AIXI converge to corrigible behavior, or does it resist shutdown?

---

## Personal Assessment

This paper is remarkable for doing what almost no paper in AI does: **defining the problem precisely and solving it exactly** (under idealized assumptions). The result is not practically useful, but it is theoretically essential — it tells us what the ceiling looks like.

The incomputability is not a weakness of the paper; it is an honest acknowledgment that true general intelligence requires solving problems harder than the halting problem. Any practical approximation is trading away some aspect of universality.

**Rating:** Essential reading for anyone serious about AGI theory.

---

## Further Reading

- Hutter, M. (2001). Towards a Universal Theory of Artificial Intelligence Based on Algorithmic Probability and Sequential Decisions.
- Legg, S. (2008). *Machine Super Intelligence* (PhD thesis). IDSIA.
- Orseau, L., & Ring, M. (2012). Space-Time Embedded Intelligence. AGI-12.
- Everitt, T., & Hutter, M. (2016). Avoiding Wireheading with Value Reinforcement Learning.
- Martínez-Plumed, F., et al. (2017). Making the Most of What You Have: Adapting a General Intelligence Measure to Current Hardware. IJCAI.
