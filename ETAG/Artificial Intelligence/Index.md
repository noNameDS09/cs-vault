---
tags:
  - AI
  - GATE-DA
  - Index
  - MOC
aliases:
  - AI Index
  - Artificial Intelligence Index
  - GATE DA AI Map
---

# 🤖 Artificial Intelligence — Index (GATE DA)

> **Map of Contents** for the GATE DA AI section. Navigate to any topic below.

---

## 🗂️ Core Files

| File                        | Purpose                                                                | Size  |
| --------------------------- | ---------------------------------------------------------------------- | ----- |
| [[Theory]]                  | **Complete theory** — Search, Logic, BN, Inference (29 KB)             | 29 KB |
| [[ETAG/Artificial Intelligence/Questions]]               | **PYQs + Practice** — GATE DA 2024/25 + high-yield practice (18 KB)    | 18 KB |
| [[Quick Revision]]          | **Formula sheet** — All algorithms, rules, shortcuts on 1 page (10 KB) | 10 KB |
| [[Artificial Intelligence]] | Syllabus overview & topic map                                          | 3 KB  |

---

## 📚 Theory Modules (in [[Theory]])

| Module | Topic | Key Content |
|--------|-------|-------------|
| **0** | Foundations | Agents, PEAS, problem formulation, evaluation criteria |
| **1** | Uninformed Search | BFS, UCS, DFS, DLS, **IDS**, Bidirectional |
| **2** | Informed Search | Greedy, **A***, IDA*, heuristics (admissible/consistent/dominance) |
| **3** | Adversarial Search | **Minimax**, **Alpha-Beta**, Expectiminimax, MCTS |
| **4** | Propositional Logic | Syntax, equivalences, CNF/DNF, Resolution, inference rules |
| **5** | Predicate Logic | Quantifiers, unification, Skolemization, FOL resolution |
| **6** | Reasoning Under Uncertainty | **Bayesian Nets**, d-separation, **Variable Elimination**, Sampling |
| **7** | Decision Theory (Bonus) | Utility, MEU, Value Iteration, VOI |
| **8** | Cross-References | Links, learning sequence, 3-week plan |

---

## 🎯 Practice Categories (in [[ETAG/Artificial Intelligence/Questions]])

| Category | Questions | Source |
|----------|-----------|--------|
| **GATE DA 2024** | 5 actual PYQs | `[[Papers/DA24]]` |
| **Uninformed Search** | 3 practice | BFS/DFS/IDS comparison |
| **Informed Search** | 4 practice | A*, heuristic dominance, IDA* |
| **Adversarial Search** | 4 practice | α-β cutoffs, move ordering, expectiminimax |
| **Propositional Logic** | 4 practice | Resolution, CNF, equivalences |
| **Predicate Logic** | 4 practice | Quantifiers, unification, Skolemization |
| **Bayesian Networks** | 7 practice | d-separation, VE, Markov blanket |
| **Inference/Sampling** | 5 practice | Rejection, LW, Gibbs, convergence |

---

## ⚡ Quick Revision Coverage (in [[Quick Revision]])

| Section | What's Included |
|---------|-----------------|
| **Search Table** | Complete algorithm comparison (complete/optimal/time/space) |
| **Heuristics** | Admissible/consistent/dominance rules, common heuristics |
| **Alpha-Beta** | Pruning rules, complexity by ordering |
| **Logic** | All equivalences, inference rules, normal forms, quantifier rules |
| **Unification** | MGU algorithm, occurs check, Skolemization |
| **Bayesian Nets** | Factorization, d-separation table (chain/fork/V), VE steps |
| **Sampling** | Rejection vs LW vs Gibbs comparison |
| **Probability** | Core rules, common distributions |
| **GATE Shortcuts** | 20+ one-line patterns |

---

## 🔗 Cross-Domain Links

```dataview
LIST
FROM "ETAG"
WHERE contains(file.name, "Probability") OR contains(file.name, "Machine") OR contains(file.name, "Logic") OR contains(file.name, "Search")
SORT file.name ASC
```

---

## 📅 Recommended Study Plan

| Week | Focus | Files | Daily Target |
|------|-------|-------|--------------|
| **1** | Search (Modules 1-3) | `[[Theory]]` + `[[Questions]]` Search section | 2 hrs theory + 1 hr coding |
| **2** | Logic (Modules 4-5) | `[[Theory]]` + `[[Questions]]` Logic section | 1.5 hrs theory + 1 hr practice |
| **3** | Uncertainty (Module 6) | `[[Theory]]` + `[[Questions]]` BN section | 2 hrs theory + 1 hr inference problems |
| **Pre-exam** | Quick Revision | `[[Quick Revision]]` (print it!) | 30 min daily review |

---

## 🏷️ Tags

```yaml
tags:
  - AI
  - GATE-DA
  - Index
  - MOC
  - Search
  - Logic
  - Bayesian-Networks
  - Adversarial-Search
  - Inference
```