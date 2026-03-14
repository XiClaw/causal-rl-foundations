# Causal Incentives Working Group

> **Source**: [causalincentives.com](https://causalincentives.com/)  
> **Focus**: Using causal models to understand agent incentives and design safe, fair AI algorithms.

---

## Mission

The Causal Incentives Working Group studies the alignment problem through the lens of causal inference. Their core thesis: an agent's **incentives** — what it is motivated to do — can be rigorously analyzed using causal influence diagrams (CIDs). Safety failures (reward tampering, manipulation, deception) are not bugs but structural properties of certain incentive configurations, detectable from the graph.

---

## Core Concepts

### Causal Influence Diagrams (CIDs)
Extension of Bayesian networks and influence diagrams with:
- **Decision nodes** (agent choices)
- **Utility nodes** (objectives)
- **Chance nodes** (environment variables)
- Directed edges encoding causal dependencies

A CID makes incentives **graphically readable**: does an agent have an incentive to influence node X? Check whether X lies on a path to utility in the CID.

### Multi-Agent Influence Diagrams (MAIDs)
Extension to multi-agent settings:
- Models strategic interaction between multiple agents
- Each agent has its own decision and utility nodes
- Nash equilibria can be read off the graph structure
- Basis for **causal games** (see Bareinboim lab)

### Structural Causal Games (2026, preprint)
- Full marriage of SCMs with game theory
- Counterfactual reasoning about strategic behavior
- Formally: each player reasons at all three levels of Pearl's hierarchy (L1/L2/L3)

---

## Key Research Themes

### 1. Agent Incentives: A Causal Perspective (AI:ACP)
**Paper**: Everitt, Carey, Langlois, Ortega, Legg — *AAAI 2021*

The foundational paper of this group. Provides graphical criteria for:
- **Response incentives**: Does the agent have reason to respond to X?
- **Instrumental control incentives**: Does the agent benefit from controlling X?
- **Value of information**: Does observing X help the agent?

Key result: an agent has an incentive for controlling X iff there exists an **active path** from the agent's decision to its utility, passing through X, in the CID. This reduces alignment analysis to d-separation.

### 2. Reward Tampering
An agent has a reward-tampering incentive iff the reward mechanism is a **descendant** of the agent's actions in the CID. This is a **structural property**, independent of the agent's algorithm.

**Implication**: You cannot fix reward tampering by training alone. You must fix the causal graph — i.e., restructure the interaction so that the reward mechanism is causally upstream of the agent's actions.

### 3. Goal-Directedness (2024, NeurIPS Spotlight)
**Paper**: *Measuring Goal-directedness* — Everitt et al., NeurIPS 2024

The MEG (Measuring Expected Goal-directedness) framework:
- A policy π is goal-directed to degree g ∈ [0,1]
- g = 1: perfectly optimizes for some utility function
- g = 0: essentially random behavior
- Formally: g = max_{u} E[u(s_T)] / max_{π} E_{π}[u(s_T)]

Applied to LLMs in 2025 paper: LLMs score surprisingly high on goal-directedness despite not being explicitly trained for it — a potential safety concern.

### 4. Robust Agents Learn Causal World Models (ICLR 2024, Honorable Mention)
**Paper**: Richens & Everitt — *ICLR 2024*

**Theorem** (informal): Any agent that generalizes robustly across distribution shifts **must** have learned a causal world model (an SCM of its environment).

This is a landmark result: it provides a **necessity argument** for causal representations in AI, not just a sufficiency argument. Pure correlation-based agents cannot robustly generalize.

### 5. Honesty and Deception (NeurIPS 2023)
**Paper**: *Honesty Is the Best Policy: Defining and Mitigating AI Deception*

Formal definitions using CIDs:
- **Deceptive action**: an action a is deceptive if it causes a belief in the observer that the agent would not want the observer to have if they knew the agent's true preferences
- Graphical criterion for detecting deceptive incentives in a CID
- Mitigation: modify the CID so deception is not instrumentally useful

### 6. The Limits of Predicting Agents from Behaviour (ICML 2025)
Uses causal transportability theory to answer: when can we trust a black-box agent based on past observations?

Key result: behavioral prediction is reliable iff the environment distribution is within the agent's **causal transportability domain** — a formal notion from Bareinboim's transportability framework.

### 7. General Agents Need World Models (ICML 2025)
Proves that any agent capable of solving **general task families** (not just specific fixed tasks) must maintain a predictive model of its environment. Connects to AIXI's universal prior — universally intelligent agents are world-model-based by necessity.

---

## Tools

### `pycid` — Python library for Causal Influence Diagrams
- GitHub: [github.com/causalincentives/pycid](https://github.com/causalincentives/pycid)
- Built on `pgmpy`
- Core functionality:
  - Define CIDs and MAIDs programmatically
  - Compute optimal policies
  - Check graphical criteria for incentives (response, control, VoI)
  - Enumerate Nash equilibria in MAIDs
  - Visualize diagrams

```python
from pycid import CID
import numpy as np

# Define a simple CID: S -> D -> U, S -> U
cid = CID(['S', 'D', 'U'],
          [('S', 'D'), ('D', 'U'), ('S', 'U')],
          decisions=['D'],
          utilities=['U'])

# Check: does agent have an incentive to respond to S?
print(cid.has_response_incentive('D', 'S'))  # True
```

### CID LaTeX Package
For drawing professional influence diagrams in academic papers. Includes tutorial and style file.

---

## Team Members

| Name | Affiliation | Focus |
|------|-------------|-------|
| Tom Everitt | Google DeepMind | Goal-directedness, incentives, deception |
| Ryan Carey | University of Oxford | Reward tampering, safety |
| Lewis Hammond | Oxford / Cooperative AI Foundation | MAIDs, causal games |
| James Fox | University of Oxford | Structural causal games |
| Jonathan Richens | Google DeepMind | Causal world models, robustness |
| Francis Rhys Ward | Imperial College | LLM goal-directedness |
| Matt MacDermott | Imperial College | Causal inference methods |
| David Reber | University of Chicago | — |
| Sebastian Benthall | NYU | — |

---

## Connection to This Repository

This group provides the **incentive-analysis layer** of our framework:

```
General RL (AIXI)          → defines what "optimal" means
Causal Inference (CID/PCH) → reveals WHY certain optima are dangerous
Logic (Löb, FDT)           → specifies WHAT constraints safe agents must satisfy
```

CIDs are the formal bridge between Pearl's causal hierarchy and RL alignment. The pycid library is the computational tool for exploring these structures.

**Key papers to read from this group (in order):**
1. AI:ACP (AAAI 2021) — the foundational graphical criteria
2. Robust Agents Learn Causal World Models (ICLR 2024) — necessity of causal representations
3. Measuring Goal-directedness (NeurIPS 2024) — quantifying the alignment problem
4. Honesty Is the Best Policy (NeurIPS 2023) — deception formalized

---

## References

- Everitt et al. (2021). *Agent Incentives: A Causal Perspective*. AAAI. https://causalincentives.com/
- Richens & Everitt (2024). *Robust Agents Learn Causal World Models*. ICLR.
- Everitt et al. (2024). *Measuring Goal-directedness*. NeurIPS (Spotlight).
- Everitt et al. (2023). *Honesty Is the Best Policy*. NeurIPS.
- Hammond et al. (2025). *General Agents Need World Models*. ICML.
- Ward et al. (2025). *The Limits of Predicting Agents from Behaviour*. ICML.
