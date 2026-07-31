---
tags:
  - AI
  - GATE-DA
  - Quick-Revision
  - Formula-Sheet
  - Cheatsheet
aliases:
  - AI Quick Revision
  - GATE DA AI Formulas
  - Last Minute AI Notes
---

# ⚡ Artificial Intelligence — Quick Revision Sheet (GATE DA)

> **Last-minute revision** — All formulas, algorithms, and key concepts on one page. Print this!

---

## 🔍 SEARCH ALGORITHMS — COMPLEXITY & PROPERTIES

### Uninformed Search

| Algorithm         | Complete   | Optimal | Time          | Space         | When to Use                           |
| ----------------- | ---------- | ------- | ------------- | ------------- | ------------------------------------- |
| **BFS**           | ✅          | ✅*      | O(b^d)        | O(b^d)        | Shallow solution, uniform cost        |
| **UCS**           | ✅          | ✅       | O(b^(1+C*/ε)) | O(b^(1+C*/ε)) | **Non-uniform** costs, optimal needed |
| **DFS**           | ❌/✅        | ❌       | O(b^m)        | O(bm)         | Deep solutions, memory limited        |
| **DLS**           | ❌ (if ℓ<d) | ❌       | O(b^ℓ)        | O(bℓ)         | Depth limit known                     |
| **IDS**           | ✅          | ✅*      | O(b^d)        | **O(bd)**     | **Best general uninformed**           |
| **Bidirectional** | ✅          | ✅*      | O(b^(d/2))    | O(b^(d/2))    | Goal invertible, explicit goals       |

> *With equal step costs. C* = optimal cost, ε = minimum step cost

### Informed Search

| Algorithm | f(n) | Complete | Optimal | Notes |
|-----------|------|----------|---------|-------|
| **Greedy** | h(n) | ❌ | ❌ | Fast but incomplete |
| **A*** | g(n)+h(n) | ✅ (admissible h) | ✅ (admissible/consistent) | **Gold standard** |
| **IDA*** | g+h with cutoff | ✅ | ✅ | Memory-bounded A* |
| **Weighted A*** | g+w·h (w>1) | ✅ | ✅ (bounded by w) | Fast, suboptimal |

### Heuristic Properties

| Property | Definition | Implication |
|----------|------------|-------------|
| **Admissible** | h(n) ≤ h*(n) ∀n | Optimal on trees |
| **Consistent** | h(n) ≤ c(n,a,n') + h(n') | Optimal on graphs |
| **Dominance** | h₁(n) ≥ h₂(n) ∀n | h₁ expands ≤ nodes |
| **Composite** | max(h₁,h₂,...) | Admissible if all admissible |

### Common Admissible Heuristics

| Problem | Heuristic | Dominates |
|---------|-----------|-----------|
| 8-Puzzle | Misplaced tiles | — |
| 8-Puzzle | Manhattan distance | Misplaced tiles |
| 8-Puzzle | Gaschnig's | Manhattan |
| Grid (4-dir) | Manhattan | Euclidean |
| Grid (8-dir) | Chebyshev | Manhattan |
| TSP | MST cost | — |

---

## ⚔️ ADVERSARIAL SEARCH

### Minimax
```
MAX node: v = max(child values)
MIN node: v = min(child values)
Terminal: v = utility(state)
```

### Alpha-Beta Pruning
```
α = best value for MAX so far (lower bound)
β = best value for MIN so far (upper bound)

MAX node: α = max(α, v)    →  cutoff if α ≥ β
MIN node: β = min(β, v)    →  cutoff if β ≤ α
```

| Ordering | Time Complexity |
|----------|-----------------|
| Worst | O(b^m) |
| Random | O(b^(3m/4)) |
| **Perfect** | **O(b^(m/2))** |

### Move Ordering Techniques
1. **Best moves first** (eval, captures, checks)
2. **Killer moves** (caused cutoffs at same depth)
3. **Transposition table** (hash seen positions)
4. **Iterative deepening + aspiration windows**

### Expectiminimax (Chance Nodes)
```
Chance node: v = Σ P(outcome) × value(outcome)
```

---

## 📐 LOGIC — EQUIVALENCES & RULES

### Propositional Logic Equivalences

| Name | Equivalence |
|------|-------------|
| **Implication** | P → Q ≡ ¬P ∨ Q |
| **Contrapositive** | P → Q ≡ ¬Q → ¬P |
| **Biconditional** | P ↔ Q ≡ (P→Q) ∧ (Q→P) ≡ (P∧Q) ∨ (¬P∧¬Q) |
| **De Morgan** | ¬(P∧Q) ≡ ¬P ∨ ¬Q  \|  ¬(P∨Q) ≡ ¬P ∧ ¬Q |
| **Double Negation** | ¬¬P ≡ P |
| **Distributive** | P∧(Q∨R) ≡ (P∧Q)∨(P∧R)  \|  P∨(Q∧R) ≡ (P∨Q)∧(P∨R) |
| **Absorption** | P∧(P∨Q) ≡ P  \|  P∨(P∧Q) ≡ P |
| **Exportation** | P → (Q → R) ≡ (P ∧ Q) → R |

### Inference Rules

| Rule | Pattern |
|------|---------|
| **Modus Ponens** | P, P→Q ⊢ Q |
| **Modus Tollens** | ¬Q, P→Q ⊢ ¬P |
| **Resolution** | P∨Q, ¬P∨R ⊢ Q∨R |
| **Unit Resolution** | P, ¬P∨Q ⊢ Q |

### Normal Forms

| Form | Structure | Use |
|------|-----------|-----|
| **CNF** | ∧ of ∨ of literals | Resolution, SAT |
| **DNF** | ∨ of ∧ of literals | Models |
| **Horn** | ≤1 positive literal | Prolog, forward chaining |

### Resolution (Refutation Complete)
```
To prove KB ⊧ α:  Show KB ∧ ¬α is unsatisfiable
1. Convert KB ∧ ¬α to CNF
2. Apply resolution until empty clause or no new clauses
3. Empty clause → contradiction → α entailed
```

---

## 🧮 PREDICATE LOGIC (FOL)

### Quantifier Rules

| Rule | Pattern |
|------|---------|
| **∀-Elim** | ∀x P(x) ⊢ P(c) for any constant c |
| **∃-Elim** | ∃x P(x) ⊢ P(c) for **new** constant c |
| **∀-Intro** | P(c) ⊢ ∀x P(x) if c arbitrary |
| **∃-Intro** | P(c) ⊢ ∃x P(x) |

### Quantifier Equivalences

| Equivalence | |
|-------------|---|
| ¬∀x P(x) ≡ ∃x ¬P(x) | ¬∃x P(x) ≡ ∀x ¬P(x) |
| ∀x (P∧Q) ≡ ∀x P ∧ ∀x Q | ∃x (P∨Q) ≡ ∃x P ∨ ∃x Q |
| ∀x P ∨ ∀x Q ⊧ ∀x (P∨Q) | ∃x (P∧Q) ⊧ ∃x P ∧ ∃x Q |

> **⚠️ NOT equivalent:** ∀x (P∨Q) ⊭ (∀x P) ∨ (∀x Q)

### Unification

| Case | Result |
|------|--------|
| Variable + Term | {var/term} if var not in term |
| Same predicate | Unify arguments recursively |
| Occurs check | x & f(x) → **FAIL** |

### Skolemization
```
∃y ∀x P(x,y)  →  ∀x P(x, f())           (no ∀ before ∃)
∀x ∃y P(x,y)  →  ∀x P(x, f(x))          (∃ after ∀ → function of ∀ vars)
∀x ∃y ∀z P(x,y,z)  →  ∀x ∀z P(x, f(x), z)
```

---

## 🎲 BAYESIAN NETWORKS

### Joint Distribution
```
P(X₁..Xₙ) = Πᵢ P(Xᵢ | Parents(Xᵢ))
```

### d-Separation (Conditional Independence)

| Structure | B Unobserved | B Observed |
|-----------|--------------|------------|
| **Chain** A → B → C | A ⊥̸ C | **A ⊥ C \| B** |
| **Fork** A ← B → C | A ⊥̸ C | **A ⊥ C \| B** |
| **V-Structure** A → B ← C | **A ⊥ C** | **A ⊥̸ C \| B** |

> **🎯 MEMORIZE:** "Observed blocks chain/fork, **activates** V-structure (explaining away!)"

### Markov Blanket of X
```
MB(X) = Parents(X) ∪ Children(X) ∪ Parents(Children(X))
```
- X ⊥ all other nodes | MB(X)

---

## 🔬 INFERENCE IN BAYESIAN NETWORKS

### Variable Elimination (Exact)

```
For variable Z to eliminate:
1. Collect all factors containing Z
2. Multiply: φ = Π factors
3. Sum out: ψ = Σ_Z φ
4. Discard old factors, add ψ
```

**Complexity:** O(n · d^w) where w = treewidth (max factor size - 1)

### Sampling Methods (Approximate)

| Method | Evidence Handling | Efficiency | Convergence |
|--------|-------------------|------------|-------------|
| **Prior Sampling** | None | Fast | Exact (∞ samples) |
| **Rejection Sampling** | Reject if ¬E | **Bad for rare E** | Exact |
| **Likelihood Weighting** | Fix E, weight by P(E\|parents) | Good for rare E | Asymptotic |
| **Gibbs Sampling (MCMC)** | Sample from P(X\|MB(X)) | Good | Asymptotic |

### Likelihood Weighting Algorithm
```
weight = 1
For each node in topo order:
  If node in evidence:
    weight *= P(evidence_value | parents)
  Else:
    sample from P(node | parents)
Return (sample, weight)
```

---

## 📊 PROBABILITY QUICK REFERENCE

### Core Rules
| Rule | Formula |
|------|---------|
| **Product** | P(A,B) = P(A\|B)P(B) = P(B\|A)P(A) |
| **Sum** | P(A) = Σ_b P(A, B=b) |
| **Bayes** | P(A\|B) = P(B\|A)P(A) / P(B) |
| **Chain** | P(X₁..Xₙ) = Π P(Xᵢ\|X₁..Xᵢ₋₁) |
| **Cond Indep** | X ⊥ Y \| Z ⇔ P(X,Y\|Z) = P(X\|Z)P(Y\|Z) |

### Common Distributions

| Distribution | PMF/PDF | Mean | Variance |
|--------------|---------|------|----------|
| **Bernoulli(p)** | p^x(1-p)^(1-x) | p | p(1-p) |
| **Binomial(n,p)** | C(n,x)p^x(1-p)^(n-x) | np | np(1-p) |
| **Poisson(λ)** | e^{-λ}λ^x/x! | λ | λ |
| **Uniform(a,b)** | 1/(b-a) | (a+b)/2 | (b-a)²/12 |
| **Normal(μ,σ²)** | ... | μ | σ² |
| **Exponential(λ)** | λe^{-λx} | 1/λ | 1/λ² |

---

## ⏱️ COMPLEXITY QUICK LOOKUP

| Algorithm | Time | Space |
|-----------|------|-------|
| BFS | O(b^d) | O(b^d) |
| UCS | O(b^(C*/ε)) | O(b^(C*/ε)) |
| DFS | O(b^m) | O(bm) |
| IDS | O(b^d) | **O(bd)** |
| A* | Exp (admissible) | Exp |
| α-β (perfect) | O(b^(m/2)) | O(m) |
| VE (BN) | O(n·d^w) | O(d^w) |
| Gibbs | O(N) per sample | O(n) |

---

## 🎯 GATE DA AI — HIGH-YIELD PATTERNS

### Must-Know Shortcuts

| Pattern | Answer |
|---------|--------|
| **Best uninformed search** | IDS (O(b^d) time, O(bd) space) |
| **A* on graphs optimal if** | Consistent heuristic |
| **Admissible combo** | max(h₁,h₂) ✅, sum ❌ |
| **Alpha-beta perfect ordering** | O(b^(m/2)) |
| **V-structure observed** | Causes become DEPENDENT |
| **d-sep: Chain/Fork** | Observed = Independent |
| **d-sep: V-structure** | Observed = Dependent |
| **Resolution proves** | KB ⊧ α iff KB ∧ ¬α unsat |
| **Quantifier negation** | ¬∀ ≡ ∃¬, ¬∃ ≡ ∀¬ |
| **Skolem function args** | Universally quantified vars before ∃ |
| **Rejection sampling bad for** | Rare evidence |
| **LW fixes** | Rare evidence (weights by likelihood) |
| **Markov blanket** | Parents + Children + Co-parents |

---

## 📝 COMMON GATE QUESTION TYPES

### Search
1. Compare BFS/DFS/IDS/UCS — space/time
2. A* admissibility/consistency check
3. Heuristic dominance question
4. Alpha-beta cutoff condition
5. Expectiminimax computation

### Logic
1. Convert to CNF / resolution proof
2. FOL translation ("Every student..." → ∀x(S(x)→∃y...))
3. Quantifier negation / Skolemization
4. Unification / MGU
5. Horn clause identification

### Bayesian Networks
1. Joint probability factorization
2. d-separation (chain/fork/V-structure)
3. Variable elimination order/variable elimination complexity
4. Sampling method comparison
5. Markov blanket identification

### Adversarial
1. Minimax value propagation
2. Alpha-beta pruning condition
3. Move ordering impact
4. Expectiminimax with chance nodes

---

## 🏷️ Tags

```yaml
tags:
  - AI
  - GATE-DA
  - Quick-Revision
  - Formula-Sheet
  - Cheatsheet
  - Search
  - Logic
  - Bayesian-Networks
  - Inference
  - Adversarial-Search
```