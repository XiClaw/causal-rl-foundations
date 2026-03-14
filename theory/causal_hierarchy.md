# Pearl's Causal Hierarchy and the do-Calculus

> Judea Pearl, 2000–2018. The most complete formal theory of causation in statistical systems.

---

## 1. The Ladder of Causation

Pearl identifies three distinct levels of causal reasoning, which he calls the **Causal Hierarchy** (or Ladder of Causation):

| Level | Name | Question type | Example | Math |
|-------|------|--------------|---------|------|
| 1 | **Association** | What is? | How does seeing $X$ change my belief about $Y$? | $P(Y \mid X)$ |
| 2 | **Intervention** | What if I do? | What happens to $Y$ if I set $X = x$? | $P(Y \mid do(X=x))$ |
| 3 | **Counterfactual** | What if I had done? | What would $Y$ be if $X$ had been $x'$, given that $X$ was actually $x$? | $P(Y_{X=x'} \mid X=x)$ |

**Key insight:** Each level is strictly more expressive than the one below. No amount of observational data (Level 1) can answer Level 2 questions without causal assumptions.

---

## 2. Structural Causal Models (SCMs)

An SCM $\mathcal{M}$ is a tuple $\langle \mathbf{U}, \mathbf{V}, \mathcal{F}, P(\mathbf{U}) \rangle$ where:

- $\mathbf{U}$ — exogenous (background) variables, governed by $P(\mathbf{U})$
- $\mathbf{V}$ — endogenous (observed) variables
- $\mathcal{F} = \{f_i\}$ — structural equations: $V_i = f_i(\mathbf{PA}_i, U_i)$, where $\mathbf{PA}_i$ are the parents of $V_i$ in the causal graph

The **causal graph** $\mathcal{G}$ is a DAG where $V_j \to V_i$ iff $V_j \in \mathbf{PA}_i$.

### Example: Drug Treatment

$$T = U_T$$
$$R = f(T, U_R)$$

where $T$ is treatment, $R$ is recovery, $U_T, U_R$ are independent noise variables.

- $P(R \mid T=1)$ — observational (confounded if there's selection bias)
- $P(R \mid do(T=1))$ — interventional (surgery on the graph: cut incoming edges to $T$)

---

## 3. The do-Operator

The **intervention** $do(X=x)$ is modeled by **graph surgery**:
- Remove all incoming edges to $X$ in $\mathcal{G}$
- Set $X = x$
- Compute the resulting distribution

Formally:
$$P(Y = y \mid do(X = x)) = \sum_{\mathbf{v}} P(Y = y \mid X = x, \mathbf{PA}_X = \mathbf{v}) \cdot P(\mathbf{PA}_X = \mathbf{v})$$

This is the **adjustment formula** (valid when $\mathbf{PA}_X$ blocks all backdoor paths).

---

## 4. The do-Calculus

Three rules for transforming interventional expressions into observational ones (when possible):

Let $\mathcal{G}_{\bar{X}}$ denote the graph with all incoming edges to $X$ removed, and $\mathcal{G}_{\underline{X}}$ with all outgoing edges removed.

**Rule 1 (Insertion/deletion of observations):**
$$P(y \mid do(x), z, w) = P(y \mid do(x), w) \quad \text{if } (Y \perp Z \mid X, W)_{\mathcal{G}_{\bar{X}}}$$

**Rule 2 (Action/observation exchange):**
$$P(y \mid do(x), do(z), w) = P(y \mid do(x), z, w) \quad \text{if } (Y \perp Z \mid X, W)_{\mathcal{G}_{\bar{X}\underline{Z}}}$$

**Rule 3 (Insertion/deletion of actions):**
$$P(y \mid do(x), do(z), w) = P(y \mid do(x), w) \quad \text{if } (Y \perp Z \mid X, W)_{\mathcal{G}_{\bar{X}\overline{Z(W)}}}$$

**Completeness theorem (Shpitser & Pearl, 2006):** The do-calculus is **complete** — any identifiable causal quantity can be reduced to an observational expression using these three rules.

---

## 5. Counterfactuals in SCMs

Counterfactuals are computed in three steps:

1. **Abduction:** Update $P(\mathbf{U})$ given observed evidence $E=e$ to get $P(\mathbf{U} \mid E=e)$
2. **Action:** Modify $\mathcal{M}$ by setting $X = x'$ (graph surgery)
3. **Prediction:** Compute $Y$ in the modified model under the posterior $P(\mathbf{U} \mid E=e)$

### Example: Firing Squad

Two soldiers ($A$, $B$) fire simultaneously. Prisoner dies ($D$). Would the prisoner have survived if $A$ had not fired?

Without SCM structure, this is unanswerable. With an SCM:
- If $B$ fires regardless: $D_{A=0} = 1$ (prisoner still dies — $A$'s action was not the actual cause)
- Actual causation requires that $A$'s action made a difference **in the actual world**

This connects to debates about **actual causation** in philosophy and legal liability.

---

## 6. Connections to Reinforcement Learning

This is the critical bridge for this repository.

### 6.1 Standard RL is Level 1

A standard RL agent learns $Q(s, a) \approx \mathbb{E}[R \mid S=s, A=a]$ — this is **associational**. The agent acts, but it does not have an explicit model of **why** actions lead to rewards.

### 6.2 Causal RL aims for Level 2+

A causally-aware RL agent should learn:
$$Q^{causal}(s, a) = \mathbb{E}[R \mid do(A=a), S=s]$$

The difference matters when:
- **Confounders exist:** A hidden variable causes both the agent's behavior policy and the reward signal
- **Off-policy learning:** Data was collected under a different policy — causal reasoning is needed to correctly estimate what a new policy would achieve
- **Transfer learning:** The causal structure generalizes across environments; correlations do not

### 6.3 Causal Bandits

The simplest testbed: a bandit where pulling arm $a$ produces reward $r$, but the reward is also influenced by an unobserved confounder $C$.

Observationally: $\mathbb{E}[R \mid A=a]$ is biased.
Causally: $\mathbb{E}[R \mid do(A=a)]$ is what we want.

If the causal graph is known, the do-calculus may allow us to compute the causal quantity from observational data alone.

---

## 7. Connections to Mathematical Logic

Pearl's framework is **algebraic** — the do-calculus is a set of syntactic transformation rules. This invites a logical reading:

- **Causal models as theories:** An SCM specifies axioms about the world (structural equations). Causal queries are theorems derivable from these axioms.
- **Interventional logic:** Modal operators $do(\cdot)$ can be given a possible-worlds semantics. $P(Y \mid do(X=x))$ is the probability of $Y$ in the "intervention world" where $X$ is forced to $x$.
- **Halpern's causal logic:** A formal logic for actual causation, built on SCMs with a syntax and proof theory.

> **Open question:** Can we build a **causal type theory** where proofs correspond to causal derivations, and programs correspond to interventions?

---

## 8. Summary

| Concept | Formal Object |
|---------|--------------|
| Causal model | SCM $\langle \mathbf{U}, \mathbf{V}, \mathcal{F}, P(\mathbf{U}) \rangle$ |
| Causal graph | DAG $\mathcal{G}$ over $\mathbf{V}$ |
| Intervention | Graph surgery + do-operator |
| Counterfactual | Abduction → Action → Prediction |
| Identifiability | Existence of observational expression for causal query |
| do-Calculus | Complete set of transformation rules |

---

## 9. Open Problems Relevant to AGI

1. **Non-Markovian SCMs:** Most of RL is Markovian; causal models with latent confounders are not.
2. **Online causal discovery:** Learning the causal graph from interaction, not just passive observation.
3. **Causal representation learning:** Learning latent causal variables from raw observations (images, text).
4. **Counterfactual credit assignment:** Using counterfactuals to assign credit to actions in long-horizon RL.
5. **Causal alignment:** Specifying human values as causal constraints, not just reward functions.

---

## References

- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.
- Pearl, J., Glymour, M., & Jewell, N. P. (2016). *Causal Inference in Statistics: A Primer*. Wiley.
- Pearl, J. (2018). *The Book of Why*. Basic Books.
- Shpitser, I., & Pearl, J. (2006). Identification of Joint Interventional Distributions in Recursive Semi-Markovian Causal Models.
- Lattimore, F., Lattimore, T., & Reid, M. D. (2016). Causal Bandits: Learning Good Interventions via Causal Inference.
- Halpern, J. Y. (2016). *Actual Causality*. MIT Press.
