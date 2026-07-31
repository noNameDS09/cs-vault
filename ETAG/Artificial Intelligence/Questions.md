---
tags:
  - AI
  - GATE-DA
  - PYQ
  - Previous-Year-Questions
  - Practice-Questions
  - Interview-Preparation
aliases:
  - AI Questions
  - GATE DA AI PYQs
  - AI Practice Problems
---

# 📝 GATE DA — Artificial Intelligence: PYQs & Practice Questions

> **Comprehensive collection** of GATE DA (2024, 2025) previous year questions for the AI section, plus high-yield practice questions matching the syllabus. Each question includes answer, detailed explanation, and **GATE shortcuts**.

---

## 📋 GATE DA AI Syllabus Coverage

| Syllabus Topic | Weightage | Key Concepts |
|----------------|-----------|--------------|
| **Search** (Informed, Uninformed, Adversarial) | ~3-4 Qs | BFS, UCS, A*, IDS, Minimax, Alpha-Beta, Heuristics |
| **Logic** (Propositional, Predicate) | ~2-3 Qs | Resolution, Unification, Quantifiers, Normal Forms |
| **Reasoning Under Uncertainty** | ~3-4 Qs | Bayesian Networks, d-separation, Variable Elimination, Sampling |

---

## 🟢 GATE DA 2025 — AI Questions

> **Source:** `[[Papers/DA25]]` (To be populated when available)

*[Note: GATE DA 2025 paper not yet released at time of writing. Will be updated.]*

---

## 🟢 GATE DA 2024 — AI Questions

> **Source:** `[[Papers/DA24]]` — Extracted from actual paper

---

### Q23. Admissible Heuristic Combination

> **Question:** Let h₁ and h₂ be two admissible heuristics for a search problem. Which of the following is **always** an admissible heuristic?
> 
> (A) h₁ + h₂  
> (B) h₁ × h₂  
> (C) h₁ / h₂  
> (D) |h₁ - h₂|

**Answer:** **(D) |h₁ - h₂|**

**Explanation:**
- Admissible means h(n) ≤ h*(n) (never overestimates true cost)
- |h₁ - h₂| ≤ max(h₁, h₂) ≤ h*(n) since both h₁, h₂ ≤ h*
- Sum: h₁ + h₂ can exceed h* (e.g., h*=10, h₁=8, h₂=7 → sum=15>10)
- Product: h₁×h₂ can exceed h* (e.g., h*=4, h₁=4, h₂=4 → product=16>4)
- Ratio: h₁/h₂ can exceed h* (e.g., h*=3, h₁=2, h₂=0.1 → ratio=20>3)

> **🎯 GATE Shortcut:** For admissible h₁, h₂:
> - ❌ Sum, Product, Ratio
> - ✅ **Max, Min, |Difference|**
> - **Bonus:** max(h₁, h₂) is the standard way to combine admissible heuristics (dominates both)

---

### Q28. Full Binary Tree Reconstruction

> **Question:** Which traversal pair(s) can uniquely reconstruct a **full binary tree**?
> 
> (A) Preorder + Inorder  
> (B) Inorder + Postorder  
> (C) Preorder + Postorder  
> (D) Inorder only

**Answer:** **(A), (B), (C)** — all three work for full binary tree

**Explanation:**
- **Full binary tree:** Every node has 0 or 2 children (no single-child nodes)
- Preorder + Inorder: ✅ Always sufficient for any binary tree
- Inorder + Postorder: ✅ Always sufficient for any binary tree
- Preorder + Postorder: ❌ General binary tree (ambiguity with single child), ✅ **Full binary tree** (no ambiguity removed ambiguity removed)
- Inorder only: ❌ Never sufficient

If single-select: **(C)** — it's the one that *requires* the full binary tree condition.

> **🎯 GATE Shortcut:** 
> - Pre+In → ✅ Always
> - In+Post → ✅ Always
> - Pre+Post → ❌ General, ✅ **Full** binary tree
> - Inorder alone → ❌ Never

---

### Q36. Expected Dice Throws (Adversarial/Probability Crossover)

> **Question:** A fair die is thrown repeatedly until two consecutive even numbers appear. What is the expected number of throws?

**Answer:** **6** (Option C)

**Solution:**
Let E₀ = expected throws when previous was not even
Let E₁ = expected throws when previous was even

E₀ = 1 + ½E₀ + ½E₁  
E₁ = 1 + ½(0) + ½E₀ = 1 + ½E₀

Substituting: E₀ = 1 + ½E₀ + ½(1 + ½E₀) = 1.5 + ¾E₀  
¼E₀ = 1.5 → E₀ = 6

> **🎯 GATE Shortcut:** For "k consecutive successes" with probability p:
> E = (1 - pᵏ) / (pᵏ(1-p))
> For 2 consecutive evens (p=½): E = (1-¼)/(¼×½) = (¾)/(⅛) = 6

---

### Q38. Tree Node Count (Search/Recursion)

> **Question:** Consider a tree where root has children 1,2; node 1 has children 3,4; node 2 has children 5,6,7,8 (all leaves). Function count(node) returns 1 + Σ count(children). What does count(root) return?

**Answer:** **9**

**Tree Structure:**
```
        0
       / \
      1   2
     / \  | \
    3  4  5 6 7 8
```
Leaves (3,4,5,6,7,8): each returns 1
Node 1: 1 + 1 + 1 = 3? Wait — returns 1 + sum(children) = 1+1+1 = 3
Node 2: 1 + 1+1+1+1 = 5
Root 0: 1 + 3 + 5 = 9

Total nodes = 9 → count(root) = 9

---

### Q40. Binary Search Recurrence

> **Question:** Recurrence relation for binary search time complexity?

**Answer:** **(A) T(n) = T(n/2) + O(1)**

> **🎯 GATE Shortcut:** 
> - Binary Search: T(n) = T(n/2) + O(1) → Θ(log n)
> - Merge Sort: T(n) = 2T(n/2) + O(n) → Θ(n log n)
> - Quick Sort (avg): T(n) = 2T(n/2) + O(n) → Θ(n log n)
> - Quick Sort (worst): T(n) = T(n-1) + O(n) → Θ(n²)
> - Linear Search: T(n) = T(n-1) + O(1) → Θ(n)

---

## 🟡 High-Yield Practice Questions by Topic

> **Solve these for mastery. Based on GATE DA pattern + GATE CSE overlap.**

---

### Topic: Uninformed Search

---

#### U1. BFS vs DFS Space Complexity

> **Question:** For a search tree with branching factor b=10, depth of solution d=5, max depth m=50. Which algorithm uses least memory?

**Options:**
(A) BFS  
(B) DFS  
(C) IDS  
(D) UCS

**Answer:** **(B) DFS** (or IDS)

**Reasoning:**
- BFS: O(b^d) = O(10^5) = 100,000 nodes
- DFS: O(bm) = O(10×50) = 500 nodes
- IDS: O(bd) = O(10×5) = 50 nodes
- UCS: Similar to BFS if uniform costs

> **🎯 GATE Shortcut:** 
> - **Space:** IDS ≈ DFS < BFS ≈ UCS
> - **Time:** BFS ≈ IDS < UCS < DFS (worst case)

---

#### U2. UCS vs BFS

> **Question:** When is UCS preferred over BFS?

**Answer:** When step costs are **not uniform** (varying edge weights).

> **🎯 GATE Trick:** UCS = BFS when all edge costs equal. UCS expands in order of **path cost g(n)**, BFS expands in order of **depth**.

---

#### U3. IDS Overhead

> **Question:** Fraction of nodes generated by IDS compared to BFS?

**Answer:** **b/(b-1)** ≈ 1.11 for b=10

**Derivation:** BFS generates 1 + b + b² + ... + b^d = (b^(d+1)-1)/(b-1)
IDS generates same sum at final iteration, plus all previous iterations = ~b/(b-1) overhead.

---

### Topic: Informed Search

---

#### I1. A* Admissibility & Consistency

> **Question:** If h is admissible but NOT consistent, is A* still optimal on graphs?

**Answer:** **No** — A* with admissible but inconsistent heuristic may re-expand nodes and can return suboptimal solution on graphs. Consistency guarantees optimality on graphs.

> **🎯 GATE Shortcut:** 
> - **Tree search:** Admissible → Optimal
> - **Graph search:** Consistent → Optimal
> - Consistent ⇒ Admissible, but not vice versa

---

#### I2. Heuristic Dominance

> **Question:** For 8-puzzle, which heuristic dominates: Manhattan distance or Misplaced tiles?

**Answer:** **Manhattan distance dominates misplaced tiles.**

**Reasoning:** For any state, Manhattan ≥ Misplaced tiles (since each misplaced tile is at least 1 move away). More informed = fewer nodes expanded.

> **🎯 GATE Shortcut:** 
> - h₁ dominates h₂ iff h₁(n) ≥ h₂(n) for all n
> - Dominant heuristic expands fewer/equal nodes
> - Gaschnig's heuristic dominates Manhattan for 8-puzzle

---

#### I3. A* with Weighted Heuristic

> **Question:** Weighted A* uses f(n) = g(n) + w·h(n) with w > 1. If h is admissible, solution cost ≤ ?

**Answer:** **w × C*** (optimal cost)

> **🎯 GATE Shortcut:** Weighted A* gives **ε-suboptimal** solution: cost ≤ w·C*. Trade speed for optimality bound.

---

#### I4. IDA* Space Complexity

> **Question:** Space complexity of IDA*?

**Answer:** **O(d)** — linear in depth (like DFS)

> **🎯 GATE Shortcut:** IDA* = IDS + A* heuristic. Memory-bounded optimal search.

---

### Topic: Adversarial Search

---

#### A1. Alpha-Beta Pruning Conditions

> **Question:** In alpha-beta pruning, a **beta cutoff** occurs when:

**Answer:** **β ≤ α** at a MIN node (v ≤ α)

**Pruning Rules:**
- **Alpha cutoff (MAX node):** α ≥ β → prune remaining children
- **Beta cutoff (MIN node):** β ≤ α → prune remaining children

> **🎯 GATE Shortcut:**
> - MAX wants to **maximize** α → α = max(α, v)
> - MIN wants to **minimize** β → β = min(β, v)
> - Cutoff when intervals don't overlap: α ≥ β

---

#### A2. Move Ordering Impact

> **Question:** Best-case time complexity of alpha-beta with perfect move ordering?

**Answer:** **O(b^(m/2))** — effective branching factor ~√b

> **🎯 GATE Shortcut:** 
> - Worst case (worst ordering): O(b^m) — no pruning
> - Random ordering: O(b^(3m/4))
> - Perfect ordering: O(b^(m/2))
> - **Killer moves, transposition table, iterative deepening** improve ordering

---

#### A3. Minimax Value Propagation

> **Question:** In a minimax tree, if a MAX node has children with values [3, 7, 2], and it's MAX's turn, what value propagates up?

**Answer:** **7** — MAX chooses maximum

> **🎯 GATE Trick:** With alpha-beta, after seeing 3 and 7 (α=7), if next child's value ≤ 7 is determined early, can prune.

---

#### A4. Expectiminimax

> **Question:** For a chance node with two outcomes: probability 0.6 → value 10, probability 0.4 → value 5. Expected value?

**Answer:** **0.6×10 + 0.4×5 = 8**

> **🎯 GATE Shortcut:** Chance node value = Σ P(outcome) × value(outcome). Add to minimax for stochastic games.

---

### Topic: Propositional Logic

---

#### PL1. Resolution Refutation

> **Question:** KB: (A ∨ B), (¬A ∨ C), (¬B ∨ C). Does KB entail C?

**Answer:** **Yes**

**Resolution proof:**
1. (A ∨ B), (¬A ∨ C) → (B ∨ C) [Resolve on A]
2. (B ∨ C), (¬B ∨ C) → (C ∨ C) = C [Resolve on B]
3. KB ∧ ¬C gives (C) and (¬C) → empty clause → contradiction

> **🎯 GATE Shortcut:** Resolution is refutation-complete. To prove KB ⊧ α, show KB ∧ ¬α is unsatisfiable.

---

#### PL2. CNF Conversion

> **Question:** Convert (A → B) ∧ (B → C) to CNF.

**Answer:** **(¬A ∨ B) ∧ (¬B ∨ C)**

**Steps:**
1. A → B ≡ ¬A ∨ B
2. B → C ≡ ¬B ∨ C
3. Conjunction of clauses = CNF

> **🎯 GATE Shortcut:** CNF = AND of ORs. Implication elimination first: P→Q → ¬P∨Q.

---

#### PL3. Logical Equivalence

> **Question:** Which is equivalent to P → (Q → R)?

**Options:**
(A) (P ∧ Q) → R  
(B) P → (Q ∧ R)  
(C) (P ∨ Q) → R  
(D) (P → Q) → R

**Answer:** **(A) (P ∧ Q) → R**

**Proof:**
P → (Q → R) ≡ ¬P ∨ (¬Q ∨ R) ≡ ¬P ∨ ¬Q ∨ R
≡ ¬(P ∧ Q) ∨ R ≡ (P ∧ Q) → R

> **🎯 GATE Shortcut:** Exportation law: P → (Q → R) ≡ (P ∧ Q) → R

---

#### PL4. Horn Clauses

> **Question:** Which is a Horn clause?

**Options:**
(A) A ∨ B ∨ ¬C  
(B) ¬A ∨ ¬B ∨ C  
(C) A ∨ ¬B ∨ ¬C  
(D) ¬A ∨ B ∨ C

**Answer:** **(B) ¬A ∨ ¬B ∨ C** — at most **one positive literal** (C)

> **🎯 GATE Shortcut:** Horn clause = clause with **≤ 1 positive literal**. Basis for Prolog, forward/backward chaining.

---

### Topic: Predicate Logic

---

#### FOL1. Quantifier Translation

> **Question:** "Every student loves some subject" in FOL?

**Answer:** **∀x (Student(x) → ∃y (Subject(y) ∧ Loves(x,y)))**

> **🎯 GATE Trap:** ∀x ∃y (Student(x) ∧ Subject(y) ∧ Loves(x,y)) is WRONG — implies everything is a student!

---

#### FOL2. Quantifier Negation

> **Question:** Negate: ∀x ∃y P(x,y)

**Answer:** **∃x ∀y ¬P(x,y)**

**Rules:**
- ¬∀x P(x) ≡ ∃x ¬P(x)
- ¬∃x P(x) ≡ ∀x ¬P(x)
- Push negation inward, flip quantifiers

---

#### FOL3. Unification

> **Question:** Can P(x, f(y)) and P(g(z), f(a)) be unified? If so, MGU?

**Answer:** **Yes. MGU = {x/g(a), y/a, z/a}**

**Steps:**
1. P(x, f(y)) = P(g(z), f(a))
2. x = g(z), f(y) = f(a) → y = a
3. Substitute y=a: x = g(z), z free → set z=a → x=g(a)
4. MGU = {x/g(a), y/a, z/a}

> **🎯 GATE Shortcut:** Occurs check: variable cannot unify with term containing itself (e.g., x and f(x) fail).

---

#### FOL4. Skolemization

> **Question:** Skolemize: ∀x ∃y ∀z P(x,y,z)

**Answer:** **∀x ∀z P(x, f(x), z)** — y replaced by Skolem function f(x) (depends on universally quantified vars before it)

---

### Topic: Bayesian Networks

---

#### BN1. Joint Distribution Factorization

> **Question:** BN with nodes A, B, C, D. Edges: A→B, A→C, B→D, C→D. Joint distribution?

**Answer:** **P(A,B,C,D) = P(A) P(B|A) P(C|A) P(D|B,C)**

> **🎯 GATE Shortcut:** P(X₁..Xₙ) = Π P(Xᵢ | Parents(Xᵢ))

---

#### BN2. d-Separation — Chain

> **Question:** In A → B → C, are A and C independent given B?

**Answer:** **Yes** — A ⊥ C | B (chain blocked by observed B)

---

#### BN3. d-Separation — Fork

> **Question:** In A ← B → C, are A and C independent given B?

**Answer:** **Yes** — A ⊥ C | B (fork blocked by observed B)

---

#### BN4. d-Separation — V-Structure (Explaining Away!)

> **Question:** In A → B ← C, are A and C independent given B?

**Answer:** **No!** — A ⊥̸ C | B (V-structure **activated** by observing B)

> **🎯 GATE Favorite:** "Explaining away" — observing common effect makes causes dependent!
> - Marginal: A ⊥ C (no evidence on B)
> - B observed: A ⊥̸ C (dependent!)
> - Descendant of B observed: A ⊥̸ C (also activated)

---

#### BN5. d-Separation Summary

| Structure | B Unobserved | B Observed |
|-----------|--------------|------------|
| A → B → C (Chain) | Dependent | **Independent** |
| A ← B → C (Fork) | Dependent | **Independent** |
| A → B ← C (V) | **Independent** | Dependent |

> **🎯 GATE Shortcut:** "Observed blocks chain/fork, activates V-structure"

---

#### BN6. Variable Elimination Order

> **Question:** For BN with treewidth 2, optimal elimination order gives max factor size?

**Answer:** **3 variables** (treewidth + 1)

**Complexity:** O(n · d^w) where w = treewidth, d = domain size

> **🎯 GATE Shortcut:** Min-fill/min-degree heuristics for elimination ordering. NP-hard to find optimal.

---

#### BN7. Conditional Independence in BN

> **Question:** Given BN: A→B, A→C, B→D, C→D. Is B ⊥ C | A?

**Answer:** **Yes** — A is common parent (fork), observing A blocks path between B and C

---

### Topic: Exact & Approximate Inference

---

#### INF1. Variable Elimination Steps

> **Question:** Eliminate variable X with factors φ₁(X,A), φ₂(X,B), φ₃(C). What's the new factor?

**Answer:** **Σ_X [φ₁(X,A) × φ₂(X,B)]** — multiply all factors containing X, sum out X. φ₃(C) unchanged.

---

#### INF2. Rejection Sampling Efficiency

> **Question:** Rejection sampling for P(X|E). Evidence E has probability 0.001. To get 1000 accepted samples, how many prior samples needed?

**Answer:** **~1,000,000** (1000 / 0.001)

> **🎯 GATE Shortcut:** Rejection sampling wastes (1-P(E)) fraction of samples. Bad for rare evidence.

---

#### INF3. Likelihood Weighting

> **Question:** In likelihood weighting, evidence variables are:
> 
> (A) Sampled normally  
> (B) Fixed to evidence values, weight multiplied by P(evidence|parents)  
> (C) Ignored  
> (D) Sampled from posterior

**Answer:** **(B)** — Fix evidence, weight by likelihood

---

#### INF4. Gibbs Sampling Markov Blanket

> **Question:** Markov blanket of node X in BN?

**Answer:** **Parents(X) ∪ Children(X) ∪ Parents(Children(X))**

**Gibbs step:** Sample X from P(X | Markov Blanket(X))

---

#### INF5. Convergence

| Method | Convergence | Exact? |
|--------|-------------|--------|
| Variable Elimination | N/A (deterministic) | ✅ |
| Junction Tree | N/A | ✅ |
| Rejection Sampling | Slow, P(E) dependent | Asymptotic |
| Likelihood Weighting | Better | Asymptotic |
| Gibbs/MCMC | Good, mixing dependent | Asymptotic |

---

## 🎯 GATE DA Exam Strategy for AI

### Marks Distribution (Estimated)
| Question Type | Count | Marks Each | Total |
|---------------|-------|------------|-------|
| MCQ (1 mark) | 4-6 | 1 | 4-6 |
| MCQ (2 marks) | 3-4 | 2 | 6-8 |
| MSQ (1-2 marks) | 2-3 | 1-2 | 2-6 |
| NAT (1-2 marks) | 1-3 | 1-2 | 1-6 |
| **Total AI** | | | **~15-20 marks** |

### High-Yield Topics (Priority Order)
1. **Search** (A*, IDS, Alpha-Beta, Heuristics) — 4-5 Qs guaranteed
2. **Bayesian Networks** (d-separation, Variable Elimination) — 3-4 Qs
3. **Logic** (Resolution, FOL Unification, Quantifiers) — 2-3 Qs
4. **Adversarial Search** (Minimax, Alpha-Beta, Expectiminimax) — 2-3 Qs
5. **Sampling** (Likelihood Weighting, Gibbs) — 1-2 Qs
6. **Uninformed Search** (BFS/DFS/IDS comparison) — 1-2 Qs

### GATE Shortcuts Cheatsheet

| Pattern | Shortcut |
|---------|----------|
| IDS | Best uninformed: O(b^d) time, O(bd) space |
| A* graph | Consistent heuristic → optimal |
| Heuristic combo | max(h₁,h₂) admissible if both admissible |
| Alpha-Beta | Perfect ordering → O(b^(m/2)) |
| V-structure | Observing B activates A-C dependence |
| d-separation | Chain/Fork: observed=independent; V: observed=dependent |
| Resolution | KB ⊧ α iff KB ∧ ¬α unsatisfiable |
| Skolemization | ∃y → f(∀ vars before y) |
| Quantifier negation | ¬∀ ≡ ∃¬, ¬∃ ≡ ∀¬ |
| Rejection sampling | Bad for rare evidence |
| Likelihood weighting | Fix evidence, weight by likelihood |

---

## 📚 Recommended Practice Resources

| Resource | Use For |
|----------|---------|
| `[[Theory]]` | Complete theory with algorithms |
| `[[Quick Revision]]` | Formula sheet for last-minute |
| `[[Papers/DA24]]` | Actual 2024 questions |
| GATE CSE AI questions (2020-2023) | Extra practice (overlap topics) |
| "AI: A Modern Approach" (Russell & Norvig) | Deep theory reference |

---

## 🏷️ Tags

```yaml
tags:
  - AI
  - GATE-DA
  - PYQ
  - Previous-Year-Questions
  - Practice-Questions
  - Search
  - Logic
  - Bayesian-Networks
  - Inference
  - Adversarial-Search
  - Minimax
  - Alpha-Beta
  - Heuristics
  - d-separation
  - Variable-Elimination
  - Sampling
```