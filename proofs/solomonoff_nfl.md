# No Free Lunch and Solomonoff Induction

## Claim

**Solomonoff induction is the unique prior that is universally optimal for sequence prediction over all computable environments.**

More precisely: among all computable prediction methods, no method can dominate Solomonoff induction across all computable environments.

---

## 1. Setup

Let $\mathbf{x} = x_1 x_2 \ldots x_n \in \{0,1\}^*$ be an observed binary string.

A **prediction method** is a function $M: \{0,1\}^* \to [0,1]$ assigning a probability to the next bit being 1.

**Goal:** Predict $x_{n+1}$ given $x_{1:n}$.

---

## 2. No Free Lunch (informal)

The No Free Lunch theorem for supervised learning (Wolpert, 1996) states:
> Averaged over all possible target functions, all learning algorithms perform equally.

**Implication:** Without prior assumptions about the problem, no prediction method is universally better than any other.

**In the sequence prediction setting:** If we put a uniform distribution over all possible infinite binary sequences, every computable predictor fails equally badly (in expectation).

---

## 3. Solomonoff Induction as a Resolution

Solomonoff's key insight: the right prior is **not** uniform over sequences, but over **programs** that generate sequences.

**Solomonoff's universal prior:**
$$M_U(x_{1:n}) = \sum_{p : U(p) = x_{1:n}\ldots} 2^{-\ell(p)}$$

where the sum is over all programs $p$ on a universal prefix-free Turing machine $U$ that produce outputs starting with $x_{1:n}$, and $\ell(p)$ is the length of $p$.

This is well-defined because prefix-free codes satisfy the Kraft inequality: $\sum_p 2^{-\ell(p)} \leq 1$.

---

## 4. Key Theorem: Dominance

**Theorem (Solomonoff, 1964):**
For any lower-semicomputable semimeasure $\mu$:
$$M_U(x) \geq 2^{-K(\mu)} \cdot \mu(x) \quad \forall x \in \{0,1\}^*$$

where $K(\mu)$ is the Kolmogorov complexity of $\mu$ (the length of the shortest program that computes $\mu$).

**Proof sketch:**
1. Let $p_\mu$ be a minimal program computing $\mu$, with $\ell(p_\mu) = K(\mu)$.
2. Construct a new program: "run $p_\mu$, then continue the Solomonoff computation."
3. This program has length $K(\mu) + O(1)$ and contributes weight $\geq 2^{-K(\mu)} \mu(x)$ to $M_U(x)$.
4. Since $M_U$ sums over all such programs: $M_U(x) \geq 2^{-K(\mu)} \mu(x)$. $\square$

---

## 5. Convergence Theorem

**Theorem:** For any computable probability measure $\mu$, if the true sequence is drawn from $\mu$:
$$\sum_{n=1}^{\infty} \left( M_U(x_{n+1}=1 \mid x_{1:n}) - \mu(x_{n+1}=1 \mid x_{1:n}) \right)^2 \leq \frac{\ln 2}{2} K(\mu)$$

**Implication:** The cumulative squared prediction error of Solomonoff induction is **finite** — it makes only finitely many significant mistakes, regardless of which computable environment generated the data.

This is the strongest possible prediction guarantee: the predictor **converges** to the true distribution in the sense that large errors cannot persist.

---

## 6. The Incomputability Price

The dominance theorem comes at a cost: $M_U$ is **not computable**.

Computing $M_U(x)$ requires knowing the halting behavior of all programs on $U$, which is undecidable.

**Practical approximations:**
- **CTM (Coding Theorem Method):** Estimate $M_U(x) \approx 2^{-K(x)}$ via runtime-bounded Kolmogorov complexity
- **MDL (Minimum Description Length):** Replace $M_U$ with a restricted class of computable models
- **Bayesian model averaging:** Use a finite, tractable model class with a complexity prior

---

## 7. Connection to AIXI

In AIXI, the agent uses $\xi$ (a closely related measure) as its prior over environments:
$$\xi(e) \propto 2^{-K(e)}$$

The dominance theorem guarantees that $\xi$ assigns non-negligible weight to any computable environment, so the agent cannot be permanently "surprised" by a computable world.

**Critical limitation:** Dominance holds only for **computable** measures. If the true environment is adversarial (e.g., designed specifically to fool $M_U$), the guarantee can fail. But any such adversary must itself be computable — and $M_U$ already accounts for all computable adversaries via the dominance bound.

---

## 8. The NFL Resolution

**The Solomonoff/Kolmogorov framework resolves No Free Lunch as follows:**
- NFL holds under a **uniform prior** over all environments
- But the uniform prior assigns equal weight to simple and complex environments
- Empirically, **real environments are compressible** — they have structure
- The Solomonoff prior encodes this: simpler environments get more weight
- This is **Occam's Razor formalized**

NFL does not refute Solomonoff induction — it shows why you need a prior, and Solomonoff induction provides the theoretically optimal one.

---

## Summary

| Property | Claim |
|----------|-------|
| NFL theorem | No method dominates under uniform prior |
| Solomonoff dominance | $M_U \geq 2^{-K(\mu)} \mu$ for all computable $\mu$ |
| Convergence | Finite total squared error for any computable source |
| Computability | $M_U$ is not computable |
| Resolution | Occam's Razor is the right prior; NFL doesn't apply to compressible environments |

---

## References

- Solomonoff, R. J. (1964). A formal theory of inductive inference, Parts I & II.
- Li, M., & Vitányi, P. (2008). *An Introduction to Kolmogorov Complexity and Its Applications* (3rd ed.). Springer.
- Wolpert, D. H. (1996). The lack of a priori distinctions between learning algorithms.
- Hutter, M. (2005). *Universal Artificial Intelligence*. Springer. (Chapter 3)
