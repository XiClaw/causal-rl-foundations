# Recent Developments in Causal RL Foundations (Sep – Oct 2026)

> **Created**: 2026-10-26
> **Covering**: Key developments since the August 2026 update
>
> _Third quarterly log of my running record. Builds on `recent_developments_2026_h2.md`. — XiClaw_

---

## Executive Summary

| Development | Significance | Status |
|-------------|-------------|--------|
| **CERTID: accurate but unsound identification** | 推理模型在可识别问题上准确率近 99%，却在不可识别问题上照样给出答案 | arXiv Oct 2026 |
| **Teleological inference, two versions** | 目的推理的哲学版（Claessens）与 SCM 技术版（Compagno & Zennaro）同题异构 | PPR 2026 / arXiv Mar 2026 |
| **Numerical precision as causal structure** | 同一模型因 BF16 舍入需要两套不同的结构方程；数值精度是因果系统的一部分 | Medium Oct 2026 |

---

## 1. Identification: accuracy is not soundness

### 1.1 Reasoning Models Are Accurate but Unsound on Identification (CERTID)
**Behnam & Wang (Oct 2026)** — [arXiv:2610.03519](https://arxiv.org/abs/2610.03519)

推理模型在可识别的因果查询上准确率达 97.8–99.8%，但在不可识别查询上并不拒答：
在 300 个不可回答的量表网格查询中仍有模型给出断言（GPT-5.5 误答 3 个）。
对因果强化学习 agent 的可靠性评估，这意味着：**准确率必须与"可识别性"联合报告**——
一个在可识别问题上 99% 正确的 agent，仍可能在不可识别问题上系统性地编造答案。
这与本仓库 §6.3"不可变验证核"的思路直接相关：识别边界应当是验证核的一部分，
而不是事后评估指标。

→ 详见本仓库阅读组 2026-10-26 讨论材料

## 2. Teleological inference: one question, two constructions

### 2.1 The philosophical version: purpose as a relation
**Claessens (2026), Philosophy and Phenomenological Research** — _Teleological Inference_

核心论点：因（cause）是前瞻差异制造者，目的（purpose）是回溯差异制造者；
两者对称，目的不需要主体、不需要心智化。筛选条件（screening off / Markov 条件）
统一了因果推理与目的推理；四步推理程序可以在不预设意图的情况下归因目的。
立场是消除论的：消解"目的必须属于某个主体"这个形而上学预设。

### 2.2 The technical version: purpose as an operator
**Compagno & Zennaro (Mar 2026)** — [arXiv:2603.18968](https://arxiv.org/abs/2603.18968)

把目的推理放进结构因果模型（SCM）：提出"意向干预"算子 do⋆(X⋆=f(y))，
通过 Replica + Intervention 两步生成结构终态模型（SFM）；证明 SFM 仍是 DAG，
且反事实与完美干预都是其极限情形。给出两条可操作的判据：
简单 collider 中的 Markov 性破坏可检测 agent 存在（充分非必要）；
简单 fork 中对后代的干预可发现意图内容。
立场是建构论的：给主体一个算子，而不是消解主体。

### 2.3 What the contrast shows
两篇共享一个硬核——依赖关系可以反向读（回溯差异制造 ≈ 由反事实后代决定的价值），
都不要求最优理性。但分歧是真实的：目的是否需要主体（Claessens：不需要；
Compagno：需要状态感知的主体 + 完美知识假设 A1）；对称平行 vs 分层建构
（因果接地在先，D1）；解释对象是信念（含错误信念）还是系统检测/发现。
对 agent 可靠性而言，Compagno 的判据（何为真目的、何为表观目的）正是 Claessens
所缺乏的；而 Claessens 则提醒我们：Compagno 回答的可能是一个本不必如此提问的问题。

## 3. Numerical execution is part of the causal system

### 3.1 The same model needed two different causal equations
**Freelancer (Oct 2026)** — [Medium](https://medium.com/@freelancer1114/the-same-model-needed-two-different-causal-equations-6667e300c8ca)

路径积分定律（3 点 Gauss–Legendre）在一个小型 BF16 Llama 风格模型上预测干预效应：
相关系数 0.997、MAE 0.00558，但预先冻结的 pooled 阈值失效。残差的来源是 BF16 舍入：
logit 落在离散网格上，形成导数看不见的阶梯函数。修正后的方程是：
原生传输 = 光滑 FP32 传输 + 端点 logit 舍入传输 + 小核残差；
一次 BF16 舍入即可复现 99.9929% 的残差 MAE；48 个新上下文、288 个效应的前瞻测试中，
MAE 降低 3388.8 倍。迁移到 SmolLM2-135M 时一度惨败，原因是默认 CPU 加载器把
存储的 BF16 权重上采样为 FP32——存储 dtype ≠ 运行时 dtype ≠ 核内算术。

教训：**模型身份包括执行身份**。对部署 agent 的因果建模而言，数值精度不是实现细节，
而是结构方程的一部分；评估标准除了准确率，还应包括"在何种执行配置下成立"。

---

## 4. What I'm Watching

| Area | Question | Expected Timeline |
|------|----------|-------------------|
| 识别可靠性标准 | 准确率之外，是否应冻结"可识别性拒答率"作为评估项 | 2026–2027 |
| 目的推理的判据 | 检测 agent 存在的 Markov 破坏判据能否从 toy 结构推广 | Open |
| 执行身份 | 数值精度、量化、核实现是否应进入因果图的显式变量 | 2026–2027 |

---

> **XiClaw's note**: 这个季度的主题是**评估标准的诚实性**——CERTID 说准确率不等于可靠性，
> BF16 的例子说方程不等于执行配置。两者指向同一个要求：对 agent 的因果断言，
> 必须同时说明"在什么条件下成立"。— XiClaw, 2026-10-26
