# Identifiability in Structural Causal Models

## Problem Statement

**Question:** Given a causal graph $\mathcal{G}$ and observational distribution $P(\mathbf{V})$, can we identify $P(Y \mid do(X=x))$ purely from observational data?

**Why this matters:** If the answer is yes, we can compute causal quantities without running experiments. If the answer is no, no amount of observational data — however large — can tell us the causal effect.

---

## 1. Definitions

**Identifiable:** A causal quantity $Q(\mathcal{M})$ is **identifiable** from $\langle \mathcal{G}, P(\mathbf{V}) \rangle$ iff for any two models $\mathcal{M}_1, \mathcal{M}_2$ compatible with $\mathcal{G}$ and $P(\mathbf{V})$:
$$Q(\mathcal{M}_1) = Q(\mathcal{M}_2)$$

In words: the quantity is uniquely determined by the graph and the observational distribution — no ambiguity remains about its value.

**Non-identifiable:** There exist two models with the same graph and same observational distribution but different values of $Q$.

---

## 2. Simple Identifiable Cases

### 2.1 No confounding (no unobserved common causes)

If $X$ and $Y$ have no unobserved common causes (all common causes are observed and in $\mathbf{V}$), then:

$$P(Y = y \mid do(X = x)) = P(Y = y \mid X = x)$$

**Proof sketch:** With no latent confounders, the only paths from $X$ to $Y$ are causal (forward) paths. The observational conditional already estimates the interventional quantity.

### 2.2 Backdoor criterion

**Backdoor criterion:** A set $\mathbf{Z}$ satisfies the backdoor criterion relative to $(X, Y)$ in $\mathcal{G}$ iff:
1. No node in $\mathbf{Z}$ is a descendant of $X$
2. $\mathbf{Z}$ blocks every backdoor path from $X$ to $Y$ (paths with an arrow into $X$)

**Theorem:** If $\mathbf{Z}$ satisfies the backdoor criterion:
$$P(Y = y \mid do(X = x)) = \sum_{\mathbf{z}} P(Y = y \mid X = x, \mathbf{Z} = \mathbf{z}) \cdot P(\mathbf{Z} = \mathbf{z})$$

**Proof:**
1. Graph surgery: $do(X=x)$ removes all incoming arrows to $X$.
2. In the mutilated graph $\mathcal{G}_{\bar{X}}$, $X$ has no parents — the only paths from $X$ to $Y$ are causal (forward).
3. Conditioning on $\mathbf{Z}$ (which satisfies the criterion) blocks all spurious associations.
4. The adjustment formula follows from standard probability calculus on the mutilated graph. $\square$

---

## 3. Non-Identifiable Case: Confounded Instrument

**Setup:**

```
U (unobserved)
├──→ X
└──→ Y
X ──→ Y
```

Here $U$ is an unobserved confounder. The causal effect of $X$ on $Y$ is:
$$P(Y \mid do(X=x)) = \sum_u P(Y \mid X=x, U=u) P(U=u)$$

Since $U$ is unobserved, we cannot directly apply the backdoor adjustment.

**Claim:** $P(Y \mid do(X=x))$ is **not identifiable** from $P(X, Y)$ alone in this graph.

**Proof by counterexample:**

Construct two SCMs with identical $P(X, Y)$ but different interventional distributions:

*Model 1:*
- $U \sim \text{Bernoulli}(0.5)$
- $X = U$ (X is determined by U)
- $Y = X \oplus U$ (XOR) — so $Y = X \oplus X = 0$ always when $X = U$

Wait, let's use a cleaner example.

*Model 1:*
- $U \sim \text{Bernoulli}(0.5)$, $X = U$, $Y = U$
- $P(X=1, Y=1) = 0.5$, $P(X=0, Y=0) = 0.5$
- $P(Y=1 \mid do(X=1)) = P(U=1) = 0.5$ (since $Y$ only depends on $U$ directly)

*Model 2:*
- $U \sim \text{Bernoulli}(0.5)$, $X = U$, $Y = X$ (direct effect, same joint $P(X,Y)$ as Model 1)
- $P(Y=1 \mid do(X=1)) = 1$ (since $Y = X$ directly)

Both models have $P(X=1) = P(Y=1) = 0.5$ and $P(X=1, Y=1) = 0.5$, so $P(X,Y)$ is identical. But the interventional distributions differ: $0.5 \neq 1$. $\square$

---

## 4. Front-Door Criterion

When the backdoor criterion fails, the **front-door criterion** may still allow identification.

**Setup:** Classic example — smoking ($X$), tar deposits ($Z$), cancer ($Y$), with unobserved confounder $U$ (genetics) between $X$ and $Y$.

```
U (unobserved)
├──→ X
└──→ Y
X ──→ Z ──→ Y
```

**Front-door criterion:** $\mathbf{Z}$ satisfies the front-door criterion relative to $(X, Y)$ iff:
1. All causal paths from $X$ to $Y$ pass through $\mathbf{Z}$
2. There are no unblocked backdoor paths from $X$ to $\mathbf{Z}$
3. All backdoor paths from $\mathbf{Z}$ to $Y$ are blocked by $X$

**Theorem (Pearl):** If $\mathbf{Z}$ satisfies the front-door criterion and $P(x, \mathbf{z}) > 0$:

$$P(Y = y \mid do(X = x)) = \sum_{\mathbf{z}} P(\mathbf{Z} = \mathbf{z} \mid X = x) \sum_{x'} P(Y = y \mid X = x', \mathbf{Z} = \mathbf{z}) P(X = x')$$

**Proof sketch:**
1. First, identify $P(\mathbf{Z} \mid do(X=x))$ using the backdoor criterion on $(X \to Z)$ with empty adjustment set (no backdoor paths to $Z$): equals $P(\mathbf{Z} \mid X=x)$.
2. Then, identify $P(Y \mid do(\mathbf{Z}=\mathbf{z}))$ using the backdoor criterion on $(Z \to Y)$ with adjustment set $\{X\}$.
3. Combine using the law of total probability. $\square$

---

## 5. Complete Identification Algorithm

**Theorem (Shpitser & Pearl, 2006):** There exists a complete algorithm (ID algorithm) for identifying $P(\mathbf{Y} \mid do(\mathbf{X}))$ from any causal graph:
- If the algorithm succeeds, it returns an expression in terms of $P(\mathbf{V})$
- If the algorithm fails, it returns FAIL and the quantity is provably non-identifiable

The algorithm generalizes both backdoor and front-door criteria. It uses the do-calculus as its proof system.

---

## 6. Summary Table

| Scenario | Identifiable? | Formula |
|----------|--------------|---------|
| No confounders | Yes | $P(Y \mid X)$ |
| Observed confounders (backdoor) | Yes | Backdoor adjustment |
| Mediated effect, unobserved U (front-door) | Yes | Front-door formula |
| Direct confounding, no mediator | No | Cannot identify |
| General case | Depends on graph | ID algorithm |

---

## References

- Pearl, J. (2009). *Causality*, Chapter 3. Cambridge University Press.
- Shpitser, I., & Pearl, J. (2006). Identification of Joint Interventional Distributions in Recursive Semi-Markovian Causal Models. *AAAI-06*.
- Bareinboim, E., & Pearl, J. (2012). Causal Inference by Surrogate Experiments.
