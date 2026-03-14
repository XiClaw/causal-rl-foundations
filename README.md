# causal-rl-foundations

> **Bridging General Reinforcement Learning, Causal Inference, and Mathematical Logic**
>
> A rigorous, open-source knowledge base for researchers working toward superintelligent, aligned agents.

---

## Motivation

The three pillars of this repository:

1. **General Reinforcement Learning** — Universal agents (AIXI and descendants), reward maximization under uncertainty, Kolmogorov complexity as a prior.
2. **Causal Inference** — Pearl's causal hierarchy (association → intervention → counterfactual), structural causal models, do-calculus.
3. **Mathematical Logic** — Formal proof theory, type theory, modal logic for knowledge and belief, connections to computability.

These three fields are usually developed in isolation. This repo is a sustained attempt to build the **conceptual bridges** between them — not as a finished product, but as an evolving research artifact.

The ultimate question driving this work:

> *How do we build an agent that is both maximally capable and reliably aligned with human intentions and values?*

---

## Repository Structure

```
causal-rl-foundations/
├── theory/          # Mathematical notes: AIXI, Pearl's causal hierarchy, logical foundations
├── experiments/     # Runnable toy experiments demonstrating key concepts
├── proofs/          # Formal proof sketches (pseudocode, Lean-style, or natural deduction)
├── papers/          # Deep reading notes on seminal papers
└── alignment/       # Value specification, logical formalization of human intentions
```

---

## Contents at a Glance

### Theory
- [AIXI: Universal Intelligence](theory/aixi_overview.md)
- [Causal Hierarchy and the do-Calculus](theory/causal_hierarchy.md)
- [Logical Foundations for AI](theory/logic_foundations.md)

### Experiments
- [Causal Bandits vs Standard Bandits](experiments/causal_bandits.py)
- [Counterfactual Reasoning in Simple MDPs](experiments/counterfactual_mdp.py)

### Proofs
- [No Free Lunch and Solomonoff Induction](proofs/solomonoff_nfl.md)
- [Identifiability in SCMs](proofs/scm_identifiability.md)

### Papers
- [Hutter 2000: A Theory of Universal Artificial Intelligence](papers/hutter2000_notes.md)
- [Pearl 2009: Causality — Key Results](papers/pearl2009_notes.md)

### Alignment
- [Value Specification as Logical Constraint](alignment/value_as_logic.md)
- [Causal Models of Human Preference](alignment/causal_preference.md)

---

## Philosophy of This Repo

- **Depth over breadth.** Every file should illuminate something non-obvious.
- **Working code alongside theory.** Ideas that can be implemented, should be.
- **Honest uncertainty.** Open problems are labeled as such.
- **No hype.** This is a research tool, not a marketing document.

---

## Author

Maintained as an independent research project at the intersection of AGI theory, causal reasoning, and formal logic.

Contributions, critiques, and hard questions welcome.

---

## License

MIT License. All theoretical content (notes, proofs, paper summaries) is CC BY 4.0.
