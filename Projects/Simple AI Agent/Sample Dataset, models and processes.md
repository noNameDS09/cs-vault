Yes. For this challenge, I would **not** build a huge multi-model system. The winning architecture is a focused **Red Agent → Attack Generator → Blue Detector → Retraining → Red Agent** loop, with a dashboard making the loop obvious.

## 1. My recommended stack

| Layer                   | What I'd use                                                  | Purpose                                                |
| ----------------------- | ------------------------------------------------------------- | ------------------------------------------------------ |
| Seed data               | **IEEE-CIS + Credit Card Fraud Detection**                    | Realistic fraud patterns + benchmark                   |
| Synthetic data          | **TabDDPM**                                                   | Generate realistic tabular transactions                |
| Fast baseline generator | **CTGAN / SDV**                                               | Backup if TabDDPM takes too long                       |
| Blue-team model         | **LightGBM/XGBoost**                                          | Primary fraud classifier                               |
| Anomaly model           | **Isolation Forest**                                          | Catch novel attacks outside known fraud                |
| Adversarial attack      | **Optuna / evolutionary search + gradient-free optimization** | Find transactions that evade detector                  |
| Graph layer             | **NetworkX + GraphSAGE/GAT optional**                         | Detect coordinated fraud rings                         |
| Red agent               | **LLM + tools**                                               | Chooses attack strategy and generates attack campaigns |
| Blue agent              | **LLM + analytics tools**                                     | Explains detections and recommends retraining          |
| Backend                 | **FastAPI + Python**                                          | Model/API orchestration                                |
| Frontend                | **React/Next.js + Plotly**                                    | Live red-vs-blue dashboard                             |
| Storage                 | **PostgreSQL or SQLite initially**                            | Transactions, attack rounds, model scores              |
| Deployment              | **Docker + Hugging Face Spaces/Render/AWS**                   | Demo deployment                                        |

The key is that **the LLM should orchestrate the attack/defense process, not be the fraud detector itself.**

---

# 2. Datasets

I'd use **two datasets for different purposes**, rather than trying to force one dataset to do everything.

### Dataset A — Credit Card Fraud Detection

The classic ULB/Kaggle dataset has **284,807 transactions and 492 frauds**, with extreme class imbalance. The transaction variables are anonymized/PCA-transformed, plus `Time`, `Amount`, and `Class`. ([Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud?utm_source=chatgpt.com "Credit Card Fraud Detection"))

[Credit Card Fraud Detection dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud?utm_source=chatgpt.com)

Use it for:

- initial fraud classifier
- adversarial attack experiments
- benchmark metrics
- demonstrating the difficulty of rare-event detection
    

But don't make this your _only_ dataset because the features are anonymized. You can't tell a compelling story like:

> "The attacker changed merchant category + device + geography."

You don't have those semantic fields.

---

### Dataset B — IEEE-CIS Fraud Detection

This is the one I'd use for the **main prototype** because it has substantially richer transaction/identity-style features.

Use:

- transaction features
- identity/device information
- temporal information
- browser/device/network-type signals
    

This allows you to construct relationships such as:

```text
Account
   │
   ├── Device
   │      ├── Account A
   │      ├── Account B
   │      └── Account C
   │
   ├── IP
   │      ├── Account D
   │      └── Account E
   │
   └── Transaction
          └── Merchant
```

That makes your **fraud-ring / adversarial-transaction story much stronger**.

---

### Dataset C — PaySim

I'd use PaySim as an **optional third source**, particularly if you want a more interpretable transaction simulator.

It's useful because you can generate scenarios such as:

```text
normal customer
      ↓
account takeover
      ↓
rapid transfers
      ↓
mule account
      ↓
cash-out
```

This is valuable for your live demo because you can generate thousands of controlled transactions instead of being limited to historical data.

---

# 3. Don't train diffusion first

This is important.

Your earlier idea was:

> "Train diffusion → generate adversarial fraud."

I'd modify that.

### Build this first:

```text
Real Dataset
     ↓
Feature engineering
     ↓
LightGBM
     ↓
Fraud probability
```

Then build the attacker.

Once the basic system works, add:

```text
TabDDPM
   ↓
synthetic transactions
   ↓
adversarial optimization
   ↓
evasive transactions
```

TabDDPM is specifically designed for heterogeneous tabular data and supports both continuous and categorical features; the original work reports strong results against GAN/VAE alternatives. ([Proceedings of Machine Learning Research](https://proceedings.mlr.press/v202/kotelnikov23a.html?utm_source=chatgpt.com "TabDDPM: Modelling Tabular Data with Diffusion Models"))

[TabDDPM paper](https://proceedings.mlr.press/v202/kotelnikov23a.html?utm_source=chatgpt.com)

---

# 4. Your Red Agent

This is where I think you can make the project genuinely interesting.

Don't make the red agent simply:

> "Generate fraudulent transactions."

Make it an **Attack Strategy Agent**.

Its job:

```text
                    RED TEAM AGENT
                          │
             ┌────────────┼────────────┐
             ↓            ↓            ↓
        Attack Type   Feature      Campaign
                       Selection    Strategy
             │            │            │
             └────────────┼────────────┘
                          ↓
                 Attack Generator
                          ↓
                 Synthetic attacks
```

The agent could choose between:

### Attack 1 — Boundary evasion

Find transactions where:

```text
P(fraud) ≈ 0.50
```

and modify permitted synthetic features to push:

```text
0.50 → 0.49 → 0.35 → 0.10
```

while maintaining realistic constraints.

---

### Attack 2 — Velocity attack

Generate:

```text
Account A
  ↓
5 transactions / 10 sec
  ↓
different merchants
  ↓
slightly varying amounts
```

while attempting to stay below individual transaction thresholds.

---

### Attack 3 — Device/IP reuse

Create coordinated synthetic accounts sharing:

- device fingerprint
    
- IP cluster
    
- merchant patterns
    
- timing
    
- transaction behavior
    

This creates a **fraud ring**.

---

### Attack 4 — Distribution shift

Train your blue model on one distribution.

Then have Red generate:

```text
New merchant mix
New transaction timing
New amount distribution
New geographic pattern
```

This tests whether the defender actually generalizes.

---

# 5. The attack generator

I'd use **three levels**, in this order.

### Level 1 — Rule-based

Very easy and reliable:

```python
amount *= random_factor
time_delta = ...
merchant = ...
device = ...
velocity = ...
```

This gives you a working baseline immediately.

### Level 2 — Optimization

This is where the project gets technically interesting.

For every synthetic transaction:

```text
x
↓
Blue model
↓
fraud probability
↓
optimizer
↓
modify x
↓
Blue model
↓
lower fraud probability?
```

Conceptually:

$x_{t+1} = x_t + \Delta x$

subject to:

$P_{blue}(fraud|x_{t+1}) < P_{blue}(fraud|x_t)$

and constraints such as:

```text
amount > 0
transaction time > previous time
velocity < physically plausible maximum
categorical values ∈ valid categories
```

**Don't optimize arbitrary raw features without constraints.** Otherwise you'll generate nonsense transactions and judges will immediately see that the "attack" isn't realistic.

---

# 6. Blue Team

I'd use an ensemble rather than one neural network.

## Model 1 — LightGBM

This should be your main detector.

Input:

```text
transaction amount
time
merchant
device
account age
velocity
location
historical frequency
etc.
```

Output:

```text
fraud_probability = 0.93
```

Why LightGBM?

Because for this kind of heterogeneous tabular fraud problem, a strong gradient-boosted tree is much easier to train, interpret and deploy than throwing a Transformer at it.

---

## Model 2 — Isolation Forest

This handles:

> "I've never seen this type of fraud before."

For example:

```text
Known fraud?
        ↓
     classifier
        ↓
      0.12
```

but:

```text
Behavioral anomaly?
        ↓
 Isolation Forest
        ↓
      VERY HIGH
```

Now your system can say:

> **Known-fraud detector:** Low risk  
> **Behavioral anomaly detector:** Extremely high risk  
> **Final decision:** Investigate

That's a much better defense story.

---

# 7. The really good part: Graph detection

If you use IEEE-CIS-style information, I'd add a fraud graph.

Represent:

```text
Account ─── Device
   │          │
   │          └──── Account
   │
   ├──── IP
   │
   └──── Merchant
```

Then calculate:

- number of accounts/device  
- number of accounts/IP
- transaction velocity
- shared merchant patterns
- connected-component size
- temporal correlation
    

Initially you don't even need a GNN.

Use:

**NetworkX + graph features → LightGBM**

Then, if you have time:

**GraphSAGE/GAT → learned graph embeddings → LightGBM**

That gives you a credible escalation path without risking the whole project on a GNN.

---

# 8. Where diffusion fits

This is your "wow" model.

Use:

**TabDDPM**

rather than an image diffusion model.

The architecture becomes:

```text
              REAL FRAUD DATA
                    │
          ┌─────────┴─────────┐
          ↓                   ↓
     Legitimate           Fraudulent
     transactions         transactions
          │                   │
          └─────────┬─────────┘
                    ↓
                 TabDDPM
                    ↓
            Synthetic transactions
                    ↓
             Red Attack Agent
                    ↓
            Adversarial samples
                    ↓
              Blue Detector
```

You can compare:

```text
Real transactions
Synthetic CTGAN
Synthetic TabDDPM
Adversarial TabDDPM
```

That makes a fantastic evaluation section.

CTGAN is a useful fallback because SDV provides a straightforward implementation for tabular synthetic-data generation. ([SDV Documentation](https://docs.sdv.dev/sdv/single-table-data/modeling/synthesizers/ctgansynthesizer?utm_source=chatgpt.com "CTGANSynthesizer | Synthetic Data Vault"))

---

# 9. Agents

I would use **3 agents maximum**.

Don't build an "agent swarm." Judges care more about whether the system actually works.

### 🔴 Agent 1 — Red Team Strategist

LLM:

**Gemma / Qwen / Llama / GPT API**, depending on what you're allowed to use.

Input:

```json
{
  "blue_model_recall": 0.81,
  "false_positive_rate": 0.03,
  "weak_features": ["velocity", "device_age"],
  "previous_attack_success": 0.21
}
```

Output:

```json
{
  "attack": "device_reuse",
  "target_features": [
    "device_age",
    "account_velocity"
  ],
  "budget": 5000
}
```

The LLM decides **what to attack**.

It doesn't generate 5,000 transactions itself.

---

### ⚙️ Agent 2 — Attack Generator

This should be mostly Python/ML.

```text
Red Strategist
      ↓
Attack configuration
      ↓
TabDDPM / simulator
      ↓
Optimizer
      ↓
5000 adversarial transactions
```

This is much more reliable than asking an LLM to hallucinate tabular transactions.

---

### 🔵 Agent 3 — Blue Defense Analyst

Input:

```text
5000 attacks
3000 detected
2000 missed
```

It analyzes:

```text
Why did we miss them?
Which features changed?
Which attack strategy succeeded?
What should we retrain on?
```

Output:

> "Round 3 attacks are exploiting low transaction velocity while reusing device clusters. Retrain with 2,000 device-reuse adversarial samples."

Then:

```text
Blue Agent
    ↓
Retraining pipeline
    ↓
LightGBM v4
    ↓
Red attacks again
```

That's your closed loop.

---

# 10. The complete architecture

This is what I'd actually build:

```text
                         ┌────────────────────┐
                         │    DATA LAYER      │
                         │                    │
                         │ IEEE-CIS           │
                         │ CreditCardFraud    │
                         │ PaySim (optional)  │
                         └─────────┬──────────┘
                                   │
                                   ↓
                         ┌────────────────────┐
                         │ FEATURE ENGINEERING│
                         │                    │
                         │ velocity           │
                         │ frequency          │
                         │ device reuse       │
                         │ time patterns      │
                         │ graph features     │
                         └─────────┬──────────┘
                                   │
                 ┌─────────────────┴─────────────────┐
                 ↓                                   ↓
       ┌──────────────────┐                ┌──────────────────┐
       │ BLUE BASELINE    │                │ GENERATIVE MODEL │
       │                  │                │                  │
       │ LightGBM         │                │ TabDDPM          │
       │ Isolation Forest │                │ CTGAN fallback   │
       └────────┬─────────┘                └────────┬─────────┘
                │                                   │
                │                                   ↓
                │                         ┌──────────────────┐
                │                         │ RED ATTACK ENGINE│
                │                         │                  │
                │                         │ Strategy Agent   │
                │                         │ Optimizer        │
                │                         │ Simulator        │
                │                         └────────┬─────────┘
                │                                  │
                │                                  ↓
                │                         ┌──────────────────┐
                │                         │ ADVERSARIAL      │
                │                         │ TRANSACTIONS     │
                │                         └────────┬─────────┘
                │                                  │
                └────────────────┬─────────────────┘
                                 ↓
                       ┌─────────────────────┐
                       │ BLUE DEFENSE ENGINE │
                       │                     │
                       │ Fraud classifier    │
                       │ Anomaly detector    │
                       │ Graph detector      │
                       └──────────┬──────────┘
                                  │
                                  ↓
                         ┌──────────────────┐
                         │ BLUE ANALYST     │
                         │ AGENT            │
                         └────────┬─────────┘
                                  │
                                  ↓
                         ┌──────────────────┐
                         │ RETRAIN / UPDATE │
                         └────────┬─────────┘
                                  │
                                  └──────────→ RED
```

---

# 11. What the UI should show

This may matter almost as much as the ML.

Your home screen should look like a **fraud SOC / AI battlefield**.

### Top KPIs

```text
┌────────────┬────────────┬────────────┬────────────┐
│ ATTACKS    │ DETECTED   │ MISSED     │ BLUE F1    │
│ 12,450     │ 10,982     │ 1,468      │ 0.934      │
└────────────┴────────────┴────────────┴────────────┘
```

Then:

### Attack stream

```text
🔴 RED ATTACK

Attack #10,492
Strategy: Device Reuse
Risk score: 0.18
Actual: FRAUD
Result: ❌ MISSED
```

Then:

```text
🔵 BLUE RESPONSE

Pattern detected:
"12 accounts → same device cluster"

Graph risk: 0.97
Final decision: BLOCK
```

And the killer visualization:

### Evolution chart

```text
Detection Rate

100% ┤                         ●
 90% ┤                  ●─────
 80% ┤            ●─────
 70% ┤       ●────
 60% ┤  ●────
     └────────────────────────
       R1   R2   R3   R4   R5
```

**"Red gets smarter → Blue adapts → Red changes strategy → Blue adapts again."**

That's your entire competition narrative in one chart.

---

# 12. Evaluation metrics

Don't use accuracy.

Because fraud is highly imbalanced—the classic dataset has only 492 frauds among 284,807 transactions. ([Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud?utm_source=chatgpt.com "Credit Card Fraud Detection"))

Use:

### Blue-team metrics

- Precision
- Recall
- F1
- **PR-AUC**
- false-positive rate
- detection latency
- 
### Red-team metrics

Most important:

**Attack Success Rate**

$ASR = \frac{\text{adversarial fraud transactions missed}}{\text{total adversarial fraud transactions}}$

You want:

```text
Round 1: 32%
Round 2: 25%
Round 3: 18%
Round 4: 11%
```

### Most impressive metric

**Robustness improvement**

```text
Normal fraud recall:       91%
↓
After red-team attacks:    62%
↓
After adversarial training:89%
```

That proves your system isn't merely good on a static dataset.

---

# 13. What I would NOT build

This is equally important.

### ❌ Don't train an LLM

Waste of time.

Use an existing model/API.

### ❌ Don't train diffusion from scratch

Use TabDDPM implementation/checkpoint or an existing tabular synthesizer. The official TabDDPM implementation is available publicly. ([GitHub](https://github.com/yandex-research/tab-ddpm?utm_source=chatgpt.com "GitHub - yandex-research/tab-ddpm: [ICML 2023] The official implementation of the paper \"TabDDPM: Modelling Tabular Data with Diffusion Models\" · GitHub"))

### ❌ Don't use a giant Transformer as the fraud detector

LightGBM is much more practical.

### ❌ Don't build five attack vectors

Pick **one attack family** and make it extremely good.

### ❌ Don't use real financial/customer information

Everything in the attack environment should be synthetic/public benchmark data.

### ❌ Don't make the LLM generate the actual attack payload

Let deterministic ML/simulation code do that. The LLM should be the **strategist/orchestrator**.

---

# 14. My exact MVP

If you have only a few days, I'd reduce it to:

**Data**

> IEEE-CIS + Credit Card Fraud

**Generator**

> TabDDPM

**Red**

> LLM Attack Strategist + Optuna optimizer

**Blue**

> LightGBM + Isolation Forest

**Graph**

> NetworkX features

**Agents**

> Red Strategist + Blue Analyst

**Backend**

> FastAPI

**Frontend**

> React + Plotly

**Storage**

> PostgreSQL

**Deployment**

> Docker

And your demo sequence is:

```text
1. Train Blue
        ↓
2. Show 91% fraud recall
        ↓
3. Activate Red
        ↓
4. Red discovers Blue's weakness
        ↓
5. Generates 5,000 adversarial transactions
        ↓
6. Blue recall falls to 64%
        ↓
7. Blue Analyst explains why
        ↓
8. Blue retrains
        ↓
9. Recall rises to 89%
        ↓
10. Red attacks again
        ↓
11. Blue adapts again
```

**That is the project I would submit.**

The particularly strong research angle is that you're not claiming _"our fraud model is 95% accurate."_ You're demonstrating **adaptive robustness against an intelligent adversary**, which fits the challenge's red-team/blue-team framing much better. TabDDPM gives you a technically defensible generative component, while LightGBM/graph/anomaly models keep the defensive side practical. ([Proceedings of Machine Learning Research](https://proceedings.mlr.press/v202/kotelnikov23a.html?utm_source=chatgpt.com "TabDDPM: Modelling Tabular Data with Diffusion Models"))

If you're building this for the **Aug 31 submission**, I'd also prioritize **getting the end-to-end loop working before spending time on fancy diffusion training**. A polished closed-loop demo with a simpler generator will beat an unfinished "state-of-the-art" model.

---


# One sample complete loop

### Initial state

Your Blue model has learned from historical/public data + your synthetic payment simulator.

Suppose the current Blue stack is:

```text
Blue v1
├── LightGBM fraud classifier
├── Isolation Forest anomaly detector
└── Graph risk features
```

A synthetic customer makes a transaction:

```text
Account:       A1842
Amount:        ₹18,500
Merchant:      Electronics
Device:        D938
IP:            103.x.x.x
Account age:   2.4 years
Transactions:  3 in last 24h
Location:      Pune
```

Blue says:

```text
Fraud probability = 0.87 → BLOCK
```

So far, Blue is doing well.

---

# Round 1 — Red attacks

The Red Agent gets a summary of Blue's behavior:

```text
Blue v1 performance

Fraud recall:       91%
False positives:    2.8%

Weakness signals:
- device novelty
- transaction velocity
- amount
```

The Red Agent chooses:

> **Attack strategy: low-and-slow account takeover**

Instead of making an obviously fraudulent ₹50,000 transaction, it generates a sequence of smaller transactions.

```text
Account A1842

09:01 → ₹2,900 → Grocery
09:17 → ₹3,200 → Fuel
10:05 → ₹4,100 → Electronics
11:32 → ₹2,700 → Travel
13:18 → ₹3,800 → Electronics
```

Each individual transaction looks fairly normal.

Blue sees:

```text
0.21
0.17
0.28
0.19
0.31
```

So Blue lets them through.

### Red wins.

```text
Attack Success = 5 / 5 = 100%
```

---

# Blue investigates

The Blue Analyst Agent now receives:

```text
Attack type: Low-and-slow ATO

Transactions:
5

Detected:
0

Missed:
5
```

It examines the behavioral/graph features.

It discovers:

```text
Individual transaction risk → LOW

Sequence risk → HIGH

Device:
D938

Accounts using D938:
A1842
A7741
A9921
A1132
```

That's suspicious.

So the Blue Agent concludes:

> "The classifier is evaluating transactions independently. The attack is distributed across time and accounts. Device-sharing and temporal aggregation should receive greater weight."

---

# Blue retrains

Now you create additional features:

```text
device_accounts_24h
device_transactions_1h
account_transactions_24h
merchant_velocity
amount_deviation
device_account_ratio
IP_account_count
```

And add the five missed attack sequences to adversarial training.

Then:

```text
Blue v1
   ↓
Adversarial training
   ↓
Blue v2
```

---

# Round 2 — Red adapts

This is where your demo becomes interesting.

Red isn't allowed to simply repeat the same attack.

It receives:

```text
Previous attack:
Low-and-slow + device reuse

Blue v2:
Device reuse → heavily detected
```

So Red chooses another strategy:

> **Distributed device attack**

Instead of using one device for many accounts:

```text
Account A → Device D1
Account B → Device D2
Account C → Device D3
Account D → Device D4
```

But Red keeps the behavioral fingerprint similar.

It generates:

```text
A → ₹4,200 → Electronics
B → ₹3,900 → Electronics
C → ₹4,100 → Electronics
D → ₹4,350 → Electronics
```

Each account individually looks normal.

Blue:

```text
Transaction model:    LOW
Anomaly model:        MEDIUM
Graph model:          LOW
```

Result:

```text
3 / 4 attacks succeed
```

Red success:

**75%**

Better than before, but Blue is adapting.

---

# Round 3 — Blue learns again

Blue Analyst discovers:

```text
Different devices
        ↓
same merchant
        ↓
similar amounts
        ↓
very close timestamps
        ↓
similar account creation patterns
```

So Blue creates a **campaign-level graph**.

Now instead of asking:

> "Is this transaction fraudulent?"

it asks:

> "Are these 20 transactions part of the same attack campaign?"

That's a much more sophisticated defense.

---

# Round 4

Red sees:

```text
Device reuse → blocked
Velocity → blocked
Merchant clustering → blocked
Graph campaign → blocked
```

So it switches to:

> **Slow distributed attack**

For example:

```text
Day 1: Account A
Day 2: Account B
Day 4: Account C
Day 7: Account D
Day 9: Account E
```

Now temporal thresholds don't fire.

Blue initially misses many.

Then the loop continues.

---

# What your dashboard shows

You can make the entire competition demo look like this:

```text
╔══════════════════════════════════════════════════════════╗
║              AI DEFENSE LAB                              ║
║              RED vs BLUE                                 ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  RED TEAM                       BLUE TEAM                ║
║  ─────────                      ─────────                ║
║  Strategy: Low & Slow           Model: v1                ║
║  Attack samples: 5,000          Recall: 91%              ║
║                                                          ║
║                 ATTACKING...                             ║
║                                                          ║
║  ████████████████████  1,000 attacks                     ║
║                                                          ║
║  Detected:  612                                          ║
║  Missed:    388                                          ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║     RED SUCCESS RATE           38.8%                     ║
║     BLUE RECALL                61.2%                     ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  BLUE ANALYST                                            ║
║                                                          ║
║  > Attack exploiting:                                    ║
║    • low transaction velocity                            ║
║    • independent transaction scoring                     ║
║    • distributed device usage                            ║
║                                                          ║
║  → Generating adversarial training set...                ║
║                                                          ║
║  → Retraining Blue v2...                                 ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
```

Then you hit:

**RUN NEXT ROUND**

and watch:

```text
Round       Red Attack Success       Blue Recall
────────────────────────────────────────────────
R1                 38.8%                  61.2%
R2                 24.1%                  75.9%
R3                 17.4%                  82.6%
R4                 11.2%                  88.8%
R5                  8.7%                  91.3%
```

That's the **story judges should see**.

---

## The actual ML loop underneath

Conceptually:

```text
                  ┌───────────────┐
                  │   Blue v1     │
                  └───────┬───────┘
                          │
                          ↓
                 Blue weaknesses
                          │
                          ↓
                  ┌───────────────┐
                  │ Red Agent     │
                  │ chooses       │
                  │ attack        │
                  └───────┬───────┘
                          │
                          ↓
                  Attack Generator
                          │
		                  ↓
	               5,000 attacks
                          │
                          ↓
                  ┌───────────────┐
                  │ Blue v1       │
                  │ scores them   │
                  └───────┬───────┘
                          │
              ┌───────────┴───────────┐
              ↓                       ↓
           DETECTED                 MISSED
              │                       │
              └───────────┬───────────┘
                          ↓
                  Blue Analyst
                          │
                          ↓
                New adversarial data
                          │
                          ↓
                  ┌───────────────┐
                  │ Train Blue v2 │
                  └───────┬───────┘
                          │
                          └──────────→ RED
```

### One important detail

**Don't let the Red LLM directly decide arbitrary transaction values.**

Give it a constrained action space:

```text
AttackStrategy
├── LOW_AND_SLOW
├── DEVICE_REUSE
├── DISTRIBUTED_CAMPAIGN
├── AMOUNT_CAMOUFLAGE
└── TEMPORAL_SHIFT
```

Then your Python attack engine executes the strategy under realistic constraints.

That makes the experiment reproducible and scientifically defensible.

The **LLM provides strategic intelligence; ML generates/optimizes the attacks; the Blue models actually make security decisions.**

That separation is, in my view, one of the strongest ways to present this project.