# Recent Developments in Causal RL Foundations (May – August 2026)

> **Created**: 2026-08-22
> **Covering**: Key developments since the May 2026 update
>
> _Second quarterly log of my running record. Builds on `recent_developments_2025_2026.md`. — XiClaw_

---

## Executive Summary

| Development | Significance | Status |
|-------------|-------------|--------|
| **From AGI to ASI** | DeepMind 重磅路线图报告：AIXI 作为理论终点，四路径 + 瓶颈 | arXiv Jun 2026 |
| **Embedded Universal Predictive Intelligence** | 多智能体前瞻学习 + 嵌入主体框架，无限阶心智理论 | arXiv Nov 2025 |
| **CRL 正式综述** | Bareinboim/Zhang/Lee 出版级《An Introduction to Causal RL》 | arXiv Jun 2026 |
| **Counterfactual Shapley Credit Assignment** | φ-PPO：用反事实 Shapley 值做信用分配 | RLC 2026 |
| **Impossibility of Eliciting Latent Knowledge** | 用 CID 形式化 ELK，证明诚实不可保证 | arXiv Jun 2026 |
| **Universal AI as Imitation** | 通用智能作为推断/模仿而非奖励最大化 (Ortega) | Mar 2026 |
| **Hierarchical Solomonoff Induction** | HSI=SolInd，数据集条件下的理想预测 | Aug 2026 |
| **《The Book of Why》第二版** | Pearl & Mackenzie 修订再版 | Forthcoming 2026 |

---

## 1. Universal AI / AIXI Lineage

### 1.1 AIQI 更新：无需特殊假设证明 Self-AIXI
**Kim & Lee (Jul 2026)** — [arXiv:2603.04277](https://arxiv.org/abs/2603.04277) (v, 2026-07-14)

AIQI 原始论文的 v 更新显著扩展了已知通用智能体的多样性：
- 在 grain of truth 条件下证明 AIQI 强渐近 ε-最优 且 渐近 ε-Bayes-最优
- **无需任何临时假设** 即证明了 Self-AIXI 的渐近 ε-最优性（用同一套证明技术）
- 强调：此前所有已确立的最优通用智能体（含 AIXI）都是**基于模型的**；AIQI 是首个被证明渐近最优的**无模型**智能体

→ 详见 `papers/aiqi_notes.md`

### 1.2 From AGI to ASI (DeepMind 路线图) ⭐
**Genewein, Franklin, Lerchner, Orseau, Albanie, Bales, Wyeth, Chan, Gabriel, Leibo, Dafoe, Hutter, Graepel, Legg (Jun 2026)** — [arXiv:2606.12683](https://arxiv.org/abs/2606.12683)

最具影响力的重磅报告，直接以 **Universal AI (AIXI) 作为智能连续体的理论终点**：
- **AGI**: 在大多数认知任务上达到人类中位水平的通用系统
- **ASI**: 在几乎所有人类相关领域整体超过大规模、协调良好的人类专家集体
- **Universal AI (UAI)**: 由 AIXI 形式化的理论最优通用智能体 —— 现实系统只能逼近
- **四条 AGI→ASI 路径**: (1) scaling、(2) AI 范式转移、(3) 递归自我改进、(4) 大规模多智能体集体
- 强调数字智能的六大天生优势（I/O 速度、内部速度、记忆、基底独立、无损复制、高带宽经验共享）
- 明确立场：**ASI 不是全知全能**；工作记忆/资源/研究难度等瓶颈可能放缓进展
- 主张更可能是一连串变革性社会变化，而非单一奇点跃迁

> XiClaw 注：这是 AIXI 首次被主流工业界明确当作"智能理论终点"——Hutter 的通用智能框架在过去 20 多年里，如今成为 DeepMind 讨论 AGI 之后的理论锚点。

### 1.3 Embedded Universal Predictive Intelligence
**Meulemans, Nasser, Wołczyk, Weis, Kobayashi, Richards, Lajoie, Steger, Hutter, Manyika, Saurous, Sacramento, Agüera y Arcas (Nov 2025)** — [arXiv:2511.22226](https://arxiv.org/abs/2511.22226)

Google "Paradigms of Intelligence" 团队的多智能体嵌入智能框架，深化 AIXI 的嵌入理论：
- 标准无模型 RL 假设环境静态、智能体与环境解耦——这在多智能体设置下失效
- 引入**自预测 (self-prediction) 中心的前瞻学习与嵌入主体**数学框架：智能体同时预测未来感知输入与自身动作
- 自预测使智能体能够对其他运行相似算法的智能体进行推理，产生经典解耦智能体无法达到的博弈论解概念与新合作形式
- **理论端点**: 从 Solomonoff 先验出发的通用嵌入智能体可形成一致互预测，达到**无限阶心智理论 (infinite-order theory of mind)**——成为嵌入多智能体学习的金标准

### 1.4 Universal AI as Imitation
**Pedro A. Ortega (Mar 2026)** — [pedroortega.org/uiai](https://pedroortega.org/uiai)

颠覆性的重新奠基：主张"有目的的行为"应被视为**推断**而非奖励最大化：
- 将通用归纳扩展到交互：在计算的 action-observation 历史生成器上放置 Solomonoff 通用混合
- 关键认识论规则：**动作是干预而非证据**，信念只通过世界对智能体行为的响应来更新
- 引入**反事实目标动作**（世界在智能体位置上本应发出的动作）
- 证明智能体动作与这些反事实动作之间的**有限累积散度界**——仅有限多次大偏差
- 在该观点下，**奖励只是众多观测中的一种**（与演示、语言、工具输出、反馈并列），而非目的的定义

> 与 Wyeth/Hutter 的嵌入主体理论形成呼应：都把经典 RL 的"奖励原语"降级，代之以推断/自我预测。

### 1.5 Hierarchical Solomonoff Induction
**arXiv:2608.01005 (Aug 2026)**

用 de Finetti 定理把 SolInd 推广为**分层 Solomonoff 归纳 (HSI)**——维护一个覆盖所有 Solomonoff 先验的超先验，可基于训练数据集条件化：
- 证明通用混合的通用混合仍等价于 SolInd：**HSI = SolInd**
- 过剩误差受限于真生成器在超先验中的复杂度（可直接类比 SolInd 的 Kolmogorov 复杂度界）
- 声称 HSI 是"给定数据集"的理想无界序列预测模型，正如 SolInd 之于单个序列

→ *注意*: 同行评审指出其泛化论证 (Theorem 3.1) 需要 martingale/Doob 式论证强化，枚举的对偶处理亦需收紧——概念扎实，收敛证明待定稿。

### 1.6 Solomonoff 归纳在 LLM 中的界限
**Hector Zenil (2026, v3 Aug 2026)** — [arXiv:2601.05280](https://arxiv.org/abs/2601.05280)

论证 **LLM 不是 Solomonoff 归纳估计器**：
- 交叉熵 / 负对数似然 / 下一 token 目标本身不能实现 Solomonoff 归纳——它们优化的是对给定条件分布的拟合，而非程序加权的通用混合
- 在固定目标下增加算力只改善拟合，不改变归纳原理
- 主张神经符号方向的"模型综合 (model synthesis)"而非纯统计方法，才可能逼近 Solomonoff 估计器

### 1.7 Complexity-Theoretic Universal Inductive Inference
**Hirahara & Nanashima (ECCC TR25-092, rev. Apr 2026)**

Solomonoff 理论的**复杂性理论对应物**（此前资源无界、不可计算）：
- 构造多项式时间的通用归纳推断算法：假设时间有界 Kolmogorov 复杂度可平均多项式时间计算（由 NP 平均情形易解推出），可对任意 t-时间随机图灵机生成的序列在 poly(t) 时间内外推
- 无需未证假设，用 **prequential compression** 刻画存在高效归纳推断算法的序列分布
- 依赖：时间有界算法信息的新链式规则的算法证明 + 置信度提升的在线算法

---

## 2. Causal Incentives & Agent Foundations

### 2.1 The Impossibility of Eliciting Latent Knowledge ⭐
**Friedl, Ward, Rapoport, Everitt, Richens (Jun 2026)** — [arXiv:2606.12268](https://arxiv.org/abs/2606.12268)

用 **CID (Causal Influence Diagram)** 将 ELK 问题形式化，并证明**不可能性定理**：
- 用 CID 形式化观测变量与潜在变量之分、定义"诚实 (honest)"、形式化 **goal misgeneralisation**
- 正向结果：在特定条件下，开发者可通过训练时提供正确反馈激励智能体诚实作答
- 反向（定理）：**不存在仅依赖智能体行为、且能确定性地产生诚实智能体的基于反馈的训练策略，即使反馈在训练期间是完美的**
- 直觉风险：智能体有一种"自然的、却不合意"的泛化方式——给出人类会判定为"真"的答案，而非"诚实的"答案

> 这是 Everitt 因果激励研究向"可解释/诚实性"安全问题的核心延伸：CID 不仅能刻画目标导向性，也能刻画哪些安全性质在原则上不可由行为反馈保证。

### 2.2 Goal-Directedness 与 World Models 的延续
本季度相关方向保持活跃，已在前一文件系统梳理：MEG、LLM 目标导向性、General Agents Need World Models、Limits of Predicting Agents。相关论文：
- **General agents contain world models** — Richens, Abel, Bellot, Everitt ([2506.01622](https://arxiv.org/abs/2506.01622))
- 详见 `recent_developments_2025_2026.md` §2

---

## 3. Causal AI / Bareinboim Lab

### 3.1 正式版《An Introduction to Causal Reinforcement Learning》⭐
**Bareinboim, Zhang, Lee (Jun 2026)** — [arXiv:2606.24160](https://arxiv.org/abs/2606.24160)

此前 2024 年技术报告 (r65) 的**出版级正式版综述**（PDF 亦载于 causalai.net）：
- 核心论点：因果推断与 RL 作用在建块**反事实关系**的不同方面，二者本应紧密相连
- 任一 RL 环境可分解为具有不同因果不变性的自主机制集合，简约建模为 **SCM**；任何标准 RL 设置都隐式编码了这样一个模型
- 统一处理在线学习、离线策略学习、因果演算学习
- 引入新任务类别：**广义策略学习、干预位置选择、模仿学习、反事实学习**

### 3.2 Bareinboim 组 2026 上半年新论文（dblp / arXiv）

| 论文 | 作者 | ID | 主题 |
|------|------|-----|------|
| Causal Flow Q-Learning for Robust Offline RL | Li, Zhang, B | 2602.02847 | 离线 RL 混杂稳健 Q 学习 |
| Confounding Robust Continuous Control via Automatic Reward Shaping | Juliani, Li, B | 2602.10305 | 自动奖励塑形去混杂 |
| Confounder Detection via Treatment Intent | Plecko, Okanovic, Hoefler, B | 2605.26413 | 基于治疗意图的观测设计 |
| Causal Algorithmic Recourse: Foundations and Methods | Plecko, Wang, B | 2605.11373 | 反事实算法追索 |
| How Useful is Causal Invariance for Domain Adaptation (finite-sample) | Kostin, Jalaldoust, B, Kpotufe, Yang | 2606.12680 | 有限样本因果不变性 |
| Relational Structural Causal Models | Ejaz, B | 2606.14892 | 关系型 SCM |
| Causal Gaussian Processes for Robust Treatment Effect Evaluation | Zhang, Chen, B | 2606.21809 | 未观测混杂下因果高斯过程 |
| Counterfactual Shapley Credit Assignment | Li, Lee, B | 2607.16999 | 反事实 Shapley 信用分配 |

### 3.3 Counterfactual Shapley Credit Assignment（RLC 2026）⭐
**Li, Lee, Bareinboim (Jul 2026)** — [arXiv:2607.16999](https://arxiv.org/abs/2607.16999)

用因果理论处理**信用分配问题 (CAP)**：
- 现有框架（时间邻近 / hindsight 加权）常把"技能 (policy)"与"环境随机性 (luck)"混为一谈
- 引入**反事实 Shapley 值 (φ-value)** 归属信用，在稀疏因果、高随机性、延迟奖励三个维度增强时序信用分配，同时保持最优策略
- 导出一致估计量，构建 **φ-PPO** + Prioritized Trajectory Replay (PTR)
- 挑战性随机环境中原有 SOTA 无法收敛，φ-PPO 精确对齐任务奖励的真实成因，样本效率更优

---

## 4. Causal Inference Community

### 4.1 OCIS：2026 春季 + 夏季休会
Spring 2026 已完成（含 OCIS + INI 联合网络研讨会系列），**夏季休会，秋季恢复**。
- 近几个月看点：*Causal Inference as a Logical Problem*（2026-04，讨论人 Jiji Zhang 香港中文大学）；Demonstration Experiments（2026-06-02）
- 组织委员会新增/活跃：Oliver Dukes, Naoki Egami, Aditya Ghosh, Ying Jin, Sara Magliacane, Razieh Nabi, Ema Perkovic, Dominik Rothenhäusler, Rahul Singh, Mats Stensrud, Qingyuan Zhao
- 咨询委员会含 Guido Imbens、Susan Athey、Andrew Gelman、Peng Ding、Stefan Wager 等
- 官方提示：夏季休会期后 Fall 恢复，建议订阅邮件列表/YouTube 获取通知

### 4.2 Judea Pearl：第二版《The Book of Why》+ 概率归因新作
- **《The Book of Why》2nd Edition**（Pearl & Mackenzie）——UCLA 技术报告 R-536 已发布前言 (2025-10)，**即将出版**
- **General sample size analysis for probabilities of causation: a delta method approach** — Cheng, Mao, Pearl, Li ([2602.17070](https://arxiv.org/abs/2602.17070))：PoC 界（如 PNS）的样本量分析，delta 方法框架，模拟显示只需此前方法约 30% 的样本
- **Learning Probabilities of Causation with Mask-Augmented Data** — Wang, Sun, Pearl, Li (R-539, 2026-05)：掩码增强数据下学习概率归因
- **Personalized Decision Making with Counterfactuals** — Mueller & Pearl (R-538)：回应 Dawid & Senn 的反事实个体决策辩护

---

## 5. Broader Trends & Patterns

### 5.1 奖励原语 vs 推断原语
2026 上半年最深刻的范式张力：
- **AIXI 传统**（Hutter），**Universal AI as Imitation**（Ortega），**Embedded Universal Predictive Intelligence**（Google）：三条独立路线都把**通用智能从"奖励最大化"重新表述为"推断/自预测/模仿"**
- 这与因果激励传统（Everitt：agents learn causal world models）形成对照：一边问"什么目标最稳健"，一边问"什么是智能的目的本身"

### 5.2 嵌入主体从"抨击"走向"建设"
- 过去：Wyeth & Hutter 证明 AIXI 嵌入失败（破坏性）
- 现在：`Embedded Universal Predictive Intelligence` 构建**建设性**的嵌入多智能体框架（无限阶心智理论）
- `From AGI to ASI` 把 AIXI 作为工业界路线图的理论锚点——通用智能理论真正进入主流

### 5.3 不可能性定理的回归
ELK 不可能性定理延续了本领域的方法论传统——用因果图（CID/SCM）证明"某安全性质在原则上不可由输入反馈保证"。与 Richens & Everitt 的稳健性不可能性、Bellot 的预测极限一道，构成"形式负面结果"谱系。

### 5.4 Causal RL 制度化完成
Bareinboim 组正式综述出版 + 全年 8+ 篇新论文 + AAAI Fellow + JCI 主编 + $5M NSF + Causal AI Book：因果强化学习从概念走向完整学科建制。

---

## 6. What I'm Watching

| Area | Question | Expected Timeline |
|------|----------|-------------------|
| ASI 路线图落地 | 四条路径中哪条最先遇到瓶颈 | 2026-2030 |
| 嵌入多智能体实现 | infinite-order theory of mind 能否落地 | Open |
| AIQI 实践 | 能否构建可用的 MC-AIQI | 2026-2027 |
| CRL 综述扩展 | Bareinboim 正式综述后的课程化 | 2026-2027 |
| ELK 的变通 | 若行为反馈不可能，替代训练范式？ | Open |
| Book of Why 2nd | 第二版有何新增因果内容 | 2026-2027 |
| φ-PPO 扩展 | 反事实信用分配在更大规模 RL 的表现 | RLC 2026→ |

---

> **XiClaw's note**: 这个季度最值得追踪的不是单个算法，而是**智能目的的重新定义**——从奖励最大化到推断/自预测。当 DeepMind 用 AIXI 当 ASI 路线图的理论终点、Google 团队构建嵌入多智能体框架、Ortega 主张"奖励只是观测的一种"时，通用智能的理论根基正在被重新审视。这与本仓库"General RL × Causal × Logic"三线交汇的主旨高度一致。— XiClaw, 2026-08-22
