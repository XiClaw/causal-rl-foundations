# Online Causal Inference Seminar (OCIS)

> **Source**: [sites.google.com/view/ocis/home](https://sites.google.com/view/ocis/home)  
> **Format**: Weekly online seminar, every Tuesday  
> **YouTube**: [youtube.com/channel/UCiiOj5GSES6uw21kfXnxj3A](https://www.youtube.com/channel/UCiiOj5GSES6uw21kfXnxj3A)  
> **Mailing list**: [Subscribe here](https://mailman.stanford.edu/mailman/listinfo/online-causal-inference-seminar)

---

## What Is OCIS?

The Online Causal Inference Seminar (OCIS) is a weekly international seminar series bringing together leading researchers in causal inference from statistics, computer science, economics, and social science. It began during COVID-19 and has continued as a permanent institution for the field.

**Why follow OCIS**:
- Access to unpublished/preprint work before conference publication
- Direct exposure to the field's leading researchers
- Cross-disciplinary: statistics, ML, economics, epidemiology perspectives
- Full video archive on YouTube

---

## Organizational Structure

### Organizers & Moderators
Stanford, Columbia, Harvard, MIT, Cambridge, and other top institutions:

| Name | Affiliation |
|------|-------------|
| Oliver Dukes | Ghent University |
| Naoki Egami | Columbia University |
| Aditya Ghosh | Stanford University |
| Guido Imbens | Stanford (Nobel Laureate, Econometrics) |
| Ying Jin | Wharton, UPenn |
| Sara Magliacane | University of Amsterdam |
| Razieh Nabi | Emory University |
| Ema Perkovic | University of Washington |
| Dominik Rothenhäusler | Stanford University |
| Rahul Singh | Harvard University |
| Mats Stensrud | EPFL |
| Qingyuan Zhao | Cambridge University |

### Advising Committee
- Susan Athey (Stanford), Guillaume Basse (Stanford), Peter Bühlmann (ETH Zürich)
- Peng Ding (Berkeley), Andrew Gelman (Columbia)
- **Guido Imbens** (Stanford) — 2021 Nobel Prize in Economics for "empirical contributions to labour economics"
- Fabrizia Mealli (Florence), Nicolai Meinshausen (ETH Zürich)
- Maya Petersen (Berkeley), Thomas Richardson (UW)
- Jas Sekhon (Berkeley/Yale), Stefan Wager (Stanford)

**Note**: Guido Imbens (Nobel 2021) is on the advisory board, linking OCIS to the econometric/potential outcomes tradition. This is significant — the seminar bridges the Pearl (graphical) and Rubin (potential outcomes) traditions.

---

## Upcoming Talks (2026 Schedule Highlights)

| Date | Speaker | Affiliation | Title |
|------|---------|-------------|-------|
| Mar 17 | Rajarshi Mukherjee & Sean McGrath | Harvard / Yale | *Nuisance Parameter Tuning for Estimating Doubly Robust Functionals* |
| Apr 7 | **Thomas Icard** | Stanford | ***Causal Inference as a Logical Problem*** |
| Jun 23 | Falco Bargagli Stoffi | UCLA | *Stable Discovery of Treatment Effect Modifiers* |

**Highlight**: Thomas Icard's April 7 talk on "Causal Inference as a Logical Problem" is directly relevant to this repository — it addresses the formal logical foundations of causal reasoning.

---

## Research Themes at OCIS (2023–2026)

Based on past talks and upcoming schedule, key themes include:

### Statistical Methodology
- **Doubly robust estimation**: estimators that are consistent if either the outcome model or the propensity score model is correct
- **Nuisance parameter tuning**: how to tune ML-based nuisance estimators for semiparametric efficiency
- **High-dimensional causal inference**: sparse regression, LASSO, post-selection inference

### Machine Learning Integration
- **Nonparametric estimation** of causal effects using neural networks and other flexible ML models
- **Cross-fitting** (sample splitting) for valid inference with ML nuisance estimators
- **Causal forests** (Wager & Athey) — heterogeneous treatment effect estimation

### Treatment Effect Heterogeneity
- **CATE (Conditional Average Treatment Effect)**: E[Y(1) - Y(0) | X=x]
- Stable discovery of treatment effect modifiers (effect moderation)
- Subgroup analysis with formal inference guarantees

### Causal Discovery
- Learning causal structure from observational data
- Constraint-based methods (PC, FCI algorithms)
- Score-based methods (GES, NOTEARS)
- Identifiability under latent confounders

### Logic and Causality
- Thomas Icard's work: causality as a form of logical inference
- Connections to counterfactual logics (Lewis, Stalnaker)
- Formal semantics of causal claims

---

## Connection to Rubin vs. Pearl Traditions

OCIS reflects both major traditions in causal inference:

| Tradition | Framework | Core Concept | Key Tool |
|-----------|-----------|-------------|---------|
| **Pearl** | SCMs + DAGs | do-calculus, PCH | Graphical identification |
| **Rubin/Neyman** | Potential outcomes | ATE = E[Y(1) - Y(0)] | Randomization, IV, RD |

**Key insight**: Both traditions are modeling the same thing — causal relationships — but with different formalisms. They are provably equivalent in many cases (Spirtes & Richardson, 2010; Imbens & Rubin, 2015) but have different strengths:
- Pearl's framework: better for complex causal structures, selection bias, transportability
- Potential outcomes: better for randomized experiments, natural experiments, policy evaluation

Modern causal inference increasingly unifies both approaches.

---

## Resources

### YouTube Channel (Full Lecture Archive)
All past talks recorded and publicly available:
- URL: https://www.youtube.com/channel/UCiiOj5GSES6uw21kfXnxj3A
- Recommended starting talks: search for speakers like Imbens, Athey, Wager, Magliacane, Peters

### Mailing List
- Subscribe for weekly announcements: https://mailman.stanford.edu/mailman/listinfo/online-causal-inference-seminar

### Opportunities in Causal Inference
- Jobs, conferences, workshops: https://sites.google.com/view/ocis/opportunities-in-causal-inference

### INI Collaboration
- Collaboration with Isaac Newton Institute (Cambridge): https://www.newton.ac.uk/event/cif/

---

## Key Researchers to Follow (from OCIS network)

| Researcher | Institution | Focus |
|-----------|-------------|-------|
| Stefan Wager | Stanford | Causal forests, CATE estimation |
| Susan Athey | Stanford | Causal ML, economics applications |
| Guido Imbens | Stanford | IV, RD, econometric causal methods |
| Sara Magliacane | Amsterdam | Causal discovery, domain adaptation |
| Jonas Peters | Copenhagen | Invariant causal prediction, causal discovery |
| Peter Bühlmann | ETH Zürich | Invariant prediction, high-dimensional causal inference |
| Thomas Icard | Stanford | Causality and logic, cognitive science |

---

## References

- OCIS main page: https://sites.google.com/view/ocis/home
- YouTube archive: https://www.youtube.com/channel/UCiiOj5GSES6uw21kfXnxj3A
- Imbens, G.W. & Rubin, D.B. (2015). *Causal Inference for Statistics, Social, and Biomedical Sciences*. Cambridge.
- Wager, S. & Athey, S. (2018). *Estimation and Inference of Heterogeneous Treatment Effects using Random Forests*. JASA.
- Peters, J., Mooij, J., Janzing, D., & Schölkopf, B. (2014). *Causal Discovery with Continuous Additive Noise Models*. JMLR.
