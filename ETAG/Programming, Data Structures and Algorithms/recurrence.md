---
tags:
  - DSA
  - GATE-DA
  - GATE-CS
  - Recurrence-Relations
  - Divide-and-Conquer
  - Dynamic-Programming
  - Algorithm-Analysis
  - Master-Theorem
  - Time-Complexity
aliases:
  - Recurrence Relations Cheatsheet
  - Master Theorem Reference
  - Algorithm Recurrences
---

# 📐 Recurrence Relations — GATE DA & CS/IT Master Reference

> **Complete reference** for all recurrence relations appearing in **GATE DA** (Section 4) and **GATE CS/IT** algorithms syllabus. Includes algorithm mapping, Master Theorem application, and GATE-specific shortcuts.

---


## 🎯 MODULE 0: MASTER THEOREM QUICK REFERENCE

### Standard Form
$$T(n) = aT\left(\frac{n}{b}\right) + f(n) \quad \text{where } a \ge 1, b > 1$$

| Case | Condition | Solution |
|------|-----------|----------|
| **1** | $f(n) = O(n^{\log_b a - \epsilon})$ for some $\epsilon > 0$ | $\Theta(n^{\log_b a})$ |
| **2** | $f(n) = \Theta(n^{\log_b a} \log^k n)$ for $k \ge 0$ | $\Theta(n^{\log_b a} \log^{k+1} n)$ |
| **3** | $f(n) = \Omega(n^{\log_b a + \epsilon})$ and $af(n/b) \le cf(n)$ for $c < 1$ | $\Theta(f(n))$ |

> **🎯 GATE Shortcut:** Compare $f(n)$ with $n^{\log_b a}$
> - $f(n)$ **polynomially smaller** → Case 1 → $n^{\log_b a}$
> - $f(n)$ **equal** (up to log factors) → Case 2 → $n^{\log_b a} \log^{k+1} n$
> - $f(n)$ **polynomially larger** + regularity → Case 3 → $f(n)$

### Common $\log_b a$ Values

| a | b | $\log_b a$ | $n^{\log_b a}$ |
|---|---|------------|----------------|
| 1 | 2 | 0 | 1 |
| 2 | 2 | 1 | n |
| 2 | 4 | 0.5 | $\sqrt{n}$ |
| 3 | 2 | $\log_2 3 \approx 1.585$ | $n^{1.585}$ |
| 4 | 2 | 2 | $n^2$ |
| 7 | 2 | $\log_2 7 \approx 2.807$ | $n^{2.807}$ |
| 8 | 2 | 3 | $n^3$ |

---

## 🟢 MODULE 1: GATE DA SYLLABUS RECURRENCES

> **Directly from GATE DA 2025/2026 Section 4: "Divide and conquer: Mergesort, Quicksort"**

### 1.1 Binary Search
```
T(n) = T(n/2) + O(1)
```
- **Algorithm:** Binary search on sorted array
- **Master Theorem:** a=1, b=2, f(n)=1 → $\log_b a = 0$, $f(n) = \Theta(n^0)$
- **Case:** 2 (k=0) → **$\Theta(\log n)$**
- **GATE DA 2024 Q40:** Answer T(n) = T(n/2) + O(1)

### 1.2 Merge Sort
```
T(n) = 2T(n/2) + Θ(n)
```
- **Algorithm:** Divide array into 2 halves, merge takes O(n)
- **Master Theorem:** a=2, b=2, f(n)=n → $\log_b a = 1$, $f(n) = \Theta(n^1)$
- **Case:** 2 (k=0) → **$\Theta(n \log n)$**

### 1.3 Quick Sort (Average Case)
```
T(n) = 2T(n/2) + Θ(n)
```
- **Assumption:** Pivot splits array evenly on average
- **Same as Merge Sort** → **$\Theta(n \log n)$**

### 1.4 Quick Sort (Worst Case)
```
T(n) = T(n-1) + Θ(n)
```
- **Assumption:** Pivot is always smallest/largest (already sorted + last element pivot)
- **Expansion:** $T(n) = T(n-1) + n = T(n-2) + (n-1) + n = ... = \sum_{i=1}^n i = \frac{n(n+1)}{2}$
- **Result:** **$\Theta(n^2)$**
- **GATE DA 2024 Q30:** Already sorted + last pivot → **0 swaps (minimum)** but max comparisons

### 1.5 Selection Sort / Bubble Sort / Insertion Sort
```
T(n) = T(n-1) + Θ(n)
```
- **Pattern:** Reduce problem by 1, do O(n) work
- **Result:** **$\Theta(n^2)$**

---

## 🔵 MODULE 2: GATE CS/IT EXTENDED DIVIDE & CONQUER

### 2.1 Strassen's Matrix Multiplication
```
T(n) = 7T(n/2) + Θ(n²)
```
- **Algorithm:** 7 multiplications of n/2 × n/2 matrices
- **Master Theorem:** a=7, b=2, f(n)=n² → $\log_b a = \log_2 7 \approx 2.807$
- **Compare:** $n^{2.807}$ vs $n^2$ → $f(n)$ polynomially smaller
- **Case:** 1 → **$\Theta(n^{\log_2 7}) \approx \Theta(n^{2.807})$**

### 2.2 Closest Pair of Points (2D)
```
T(n) = 2T(n/2) + Θ(n)
```
- **Divide:** Split by x-coordinate median
- **Conquer:** Recursive on left/right
- **Combine:** Check strip of width 2δ in O(n)
- **Result:** **$\Theta(n \log n)$**

### 2.3 Maximum Subarray Sum (Divide & Conquer)
```
T(n) = 2T(n/2) + Θ(n)
```
- **Crossing subarray** takes O(n) to find
- **Result:** **$\Theta(n \log n)$**
- *Note: Kadane's algorithm is O(n) — better!*

### 2.4 Binary Tree Traversals
```
T(n) = 2T(n/2) + Θ(1)  [balanced]
T(n) = T(n-1) + Θ(1)   [skewed]
```
- **Balanced:** a=2, b=2, f(n)=1 → $\log_b a = 1$ > 0 → Case 1 → **$\Theta(n)$**
- **Skewed:** **$\Theta(n)$**

### 2.5 Tree Height / Diameter
```
T(n) = T(left) + T(right) + Θ(1)
```
- **Visits each node once** → **$\Theta(n)$**

---

## 🟡 MODULE 3: DYNAMIC PROGRAMMING RECURRENCES

> **GATE CS/IT Syllabus: "Dynamic Programming" — Core topic**

### 3.1 Fibonacci Numbers
```
T(n) = T(n-1) + T(n-2) + Θ(1)
```
- **Naive Recursive:** Exponential → **$\Theta(\phi^n)$** where $\phi = \frac{1+\sqrt{5}}{2} \approx 1.618$
- **DP/Memoization:** **$\Theta(n)$** time, $\Theta(n)$ space
- **Space Optimized:** **$\Theta(n)$** time, **$\Theta(1)$** space

### 3.2 Longest Common Subsequence (LCS)
```
T(m,n) = T(m-1,n-1) + Θ(1)           if X[m] = Y[n]
T(m,n) = max(T(m-1,n), T(m,n-1)) + Θ(1)  otherwise
```
- **DP Table:** (m+1) × (n+1)
- **Time:** **$\Theta(mn)$**
- **Space:** **$\Theta(mn)$** or **$\Theta(\min(m,n))$** optimized

### 3.3 Edit Distance (Levenshtein)
```
T(i,j) = T(i-1,j-1) + Θ(1)                    if match
T(i,j) = 1 + min(T(i-1,j), T(i,j-1), T(i-1,j-1))  otherwise
```
- **Time/Space:** **$\Theta(mn)$**

### 3.4 0/1 Knapsack
```
T(i,w) = max(T(i-1,w), value[i] + T(i-1, w-weight[i]))  if weight[i] ≤ w
T(i,w) = T(i-1,w)                                         otherwise
```
- **Time/Space:** **$\Theta(nW)$** where W = capacity
- **Pseudo-polynomial** (depends on numeric value W)

### 3.5 Unbounded Knapsack
```
T(w) = max(T(w), value[i] + T(w-weight[i]))  for all i
```
- **Time/Space:** **$\Theta(nW)$**

### 3.6 Matrix Chain Multiplication
```
T(i,j) = min_{i ≤ k < j} [T(i,k) + T(k+1,j) + p_{i-1}p_k p_j] + Θ(1)
```
- **Time:** **$\Theta(n^3)$**
- **Space:** **$\Theta(n^2)$**

### 3.7 Optimal BST
```
T(i,j) = min_{i ≤ r ≤ j} [T(i,r-1) + T(r+1,j)] + sum(i,j) + Θ(1)
```
- **Time:** **$\Theta(n^3)$** (Knuth optimization → $\Theta(n^2)$)

### 3.8 Longest Increasing Subsequence (LIS)
```
T(i) = 1 + max_{j < i, A[j] < A[i]} T(j)
```
- **DP:** **$\Theta(n^2)$**
- **Patience Sorting (Binary Search):** **$\Theta(n \log n)$**

### 3.9 Rod Cutting
```
T(n) = max_{1 ≤ i ≤ n} (price[i] + T(n-i))
```
- **Time:** **$\Theta(n^2)$**

### 3.10 Coin Change (Min Coins)
```
T(amount) = 1 + min_{c ∈ coins} T(amount - c)
```
- **Time:** **$\Theta(n \times \text{amount})$**

### 3.11 Subset Sum / Partition
```
T(i,sum) = T(i-1,sum) ∨ T(i-1, sum-A[i])
```
- **Time:** **$\Theta(n \times \text{sum})$**

---

## 🟠 MODULE 4: GRAPH ALGORITHM RECURRENCES

### 4.1 Dijkstra's Algorithm
```
T(V,E) = O((V+E) log V)  with binary heap
T(V,E) = O(E + V log V)  with Fibonacci heap
```
- **Not a standard recurrence** — greedy + priority queue

### 4.2 Bellman-Ford
```
T(V,E) = Θ(VE)
```
- **Relaxation:** V-1 iterations × E edges

### 4.3 Floyd-Warshall
```
T(k,i,j) = min(T(k-1,i,j), T(k-1,i,k) + T(k-1,k,j))
```
- **Time:** **$\Theta(V^3)$**
- **Space:** **$\Theta(V^2)$**

### 4.4 Prim's MST
```
T(V,E) = O((V+E) log V)  with binary heap
T(V,E) = O(E + V log V)  with Fibonacci heap
```

### 4.5 Kruskal's MST
```
T(V,E) = O(E log E) = O(E log V)  for sorting + DSU
```

### 4.6 BFS / DFS
```
T(V,E) = Θ(V + E)
```
- **Visits** each vertex and edge once

---

## 🔴 MODULE 5: ADVANCED RECURRENCES (GATE CS/IT)

### 5.1 Recursive Tree Algorithms

| Algorithm | Recurrence | Solution |
|-----------|------------|----------|
| **Tree Traversal** | T(n) = T(left) + T(right) + O(1) | Θ(n) |
| **Height** | T(n) = max(T(left), T(right)) + 1 | Θ(n) |
| **Diameter** | T(n) = T(left) + T(right) + O(1) | Θ(n) |
| **BST Search** | T(n) = T(n/2) + O(1) [balanced] | Θ(log n) |
| **BST Search** | T(n) = T(n-1) + O(1) [skewed] | Θ(n) |
| **AVL Insert** | T(n) = T(n/2) + O(1) | Θ(log n) |
| **Heap Insert** | T(n) = T(n/2) + O(1) | Θ(log n) |
| **Heapify** | T(n) = 2T(n/2) + O(1) | **Θ(n)** |

### 5.2 Special Recurrences

| Recurrence | Solution | Method |
|------------|----------|--------|
| T(n) = T(n-1) + 1/n | Θ(log n) | Harmonic series |
| T(n) = T(n/2) + T(n/3) + n | Θ(n) | Akra-Bazzi |
| T(n) = 2T(n/2) + n/log n | Θ(n log log n) | Master fails, use recursion tree |
| T(n) = T(√n) + 1 | Θ(log log n) | Substitution m = log n |
| T(n) = √n T(√n) + n | Θ(n log log n) | Substitution m = log n |
| T(n) = T(n-1) + T(n-2) | Θ(φ^n) | Characteristic equation |

---

## 🎯 MODULE 6: MASTER THEOREM APPLICATION TABLE

### Step-by-Step for GATE

```
Given: T(n) = aT(n/b) + f(n)

Step 1: Compute c = log_b a
Step 2: Compare f(n) with n^c
Step 3: Apply Case 1, 2, or 3
```

### Quick Classification

| Recurrence | a | b | f(n) | log_b a | Case | Solution |
|------------|---|---|------|---------|------|----------|
| Binary Search | 1 | 2 | 1 | 0 | 2 (k=0) | Θ(log n) |
| Merge Sort | 2 | 2 | n | 1 | 2 (k=0) | Θ(n log n) |
| Quick Sort (avg) | 2 | 2 | n | 1 | 2 (k=0) | Θ(n log n) |
| Quick Sort (worst) | — | — | — | — | Substitution | Θ(n²) |
| Strassen | 7 | 2 | n² | 2.807 | 1 | Θ(n^2.807) |
| Selection Sort | — | — | — | — | Expansion | Θ(n²) |
| Heapify | 2 | 2 | 1 | 1 | 1 | Θ(n) |
| Binary Tree Traversal | 2 | 2 | 1 | 1 | 1 | Θ(n) |
| LCS / Edit Distance | — | — | — | — | 2D DP | Θ(mn) |
| 0/1 Knapsack | — | — | — | — | 2D DP | Θ(nW) |
| Matrix Chain | — | — | — | — | 3D DP | Θ(n³) |
| Floyd-Warshall | — | — | — | — | 3D DP | Θ(V³) |

---

## ⚠️ MODULE 7: GATE TRAPS & COMMON MISTAKES

### Trap 1: Quick Sort Worst Case
> **Question:** "Quick sort with last element as pivot on already sorted array"
> **Answer:** Θ(n²) time, **0 swaps** (if self-swaps not counted)
> **GATE DA 2024 Q30** tested exactly this!

### Trap 2: Master Theorem Case 2 Variants
| f(n) | k | Solution |
|------|---|----------|
| n^c | 0 | Θ(n^c log n) |
| n^c log n | 1 | Θ(n^c log² n) |
| n^c log² n | 2 | Θ(n^c log³ n) |

### Trap 3: Non-Standard Forms (Master Theorem Fails)
| Recurrence | Why Master Fails | Use |
|------------|------------------|-----|
| T(n) = 2T(n/2) + n/log n | f(n) not polynomially comparable | Recursion tree / Akra-Bazzi |
| T(n) = T(n/3) + T(2n/3) + n | a not constant per subproblem | Recursion tree |
| T(n) = T(n-1) + 1/n | Not divide-and-conquer | Summation |
| T(n) = T(√n) + 1 | b not constant | Substitution |

### Trap 4: Space vs Time
| Algorithm | Time | Space |
|-----------|------|-------|
| Merge Sort | Θ(n log n) | **Θ(n)** (not in-place) |
| Quick Sort | Θ(n log n) avg | **Θ(log n)** stack avg |
| Heap Sort | Θ(n log n) | **Θ(1)** in-place |
| LCS (DP) | Θ(mn) | Θ(mn) or Θ(min(m,n)) |
| DFS (recursive) | Θ(V+E) | **Θ(V)** call stack |

---

## 📋 MODULE 8: GATE PYQ PATTERNS

### GATE DA 2024
| Q | Topic | Recurrence | Answer |
|---|-------|------------|--------|
| Q30 | Quick Sort swaps | T(n) = T(n-1) + n | 0 swaps |
| Q40 | Binary Search | T(n) = T(n/2) + O(1) | T(n) = T(n/2) + O(1) |

### GATE CS/IT Frequent Patterns
| Pattern | Frequency | Example |
|---------|-----------|---------|
| Merge Sort recurrence | Very High | T(n) = 2T(n/2) + n |
| Binary Search | High | T(n) = T(n/2) + 1 |
| Quick Sort worst | Medium | T(n) = T(n-1) + n |
| Strassen's | Low-Medium | T(n) = 7T(n/2) + n² |
| Heapify | Medium | T(n) = 2T(n/2) + 1 → Θ(n) |
| LCS/Edit Distance | High | Θ(mn) DP |
| Matrix Chain | Medium | Θ(n³) DP |
| Knapsack | Medium | Θ(nW) DP |
| Tree traversal | High | T(n) = T(left) + T(right) + 1 |
| Substitution method | Medium | T(n) = 2T(n/2) + n/log n |

---

## 🧮 MODULE 9: SOLVING TECHNIQUES CHEATSHEET

### 1. Substitution (Iteration) Method
```
T(n) = T(n-1) + n
     = T(n-2) + (n-1) + n
     = T(n-3) + (n-2) + (n-1) + n
     ...
     = T(1) + 2 + 3 + ... + n
     = Θ(n²)
```

### 2. Recursion Tree
```
T(n) = 2T(n/2) + n
Level 0: n
Level 1: 2 × n/2 = n
Level 2: 4 × n/4 = n
...
Level log n: n
Total: n × log n = Θ(n log n)
```

### 3. Master Theorem (Standard Form Only)
```
T(n) = aT(n/b) + f(n)

c = log_b a
if f(n) = O(n^{c-ε})     → Θ(n^c)                    [Case 1]
if f(n) = Θ(n^c log^k n) → Θ(n^c log^{k+1} n)       [Case 2]
if f(n) = Ω(n^{c+ε}) + regularity → Θ(f(n))         [Case 3]
```

### 4. Akra-Bazzi (Generalization)
```
T(n) = Σ a_i T(n/b_i) + f(n)
Solution: T(n) = Θ(n^p (1 + ∫_1^n f(u)/u^{p+1} du))
where Σ a_i / b_i^p = 1
```

### 5. Characteristic Equation (Linear Homogeneous)
```
T(n) = a_1 T(n-1) + a_2 T(n-2) + ... + a_k T(n-k)
Characteristic: x^k - a_1 x^{k-1} - ... - a_k = 0
Roots r_1, r_2, ..., r_k:
  Distinct real: Σ c_i r_i^n
  Repeated: (c_0 + c_1 n + ...) r^n
  Complex: n^α (c_1 cos(β n) + c_2 sin(β n))
```

---

## 🔗 MODULE 10: CROSS-REFERENCES

```dataview
LIST
FROM "ETAG/Programming, Data Structures and Algorithms"
WHERE file.name != "recurrence"
SORT file.name ASC
```

> **Related Files:**
> - `[[Programming, Data Structures and Algorithms]]` — Complete theory with implementations
> - `[[Time Complexities]]` — Sorting & operation complexity table
> - `[[PYQs and questions]]` — GATE DA PYQs + practice questions
> - `[[Index]]` — Navigation hub

---

## ✅ QUICK REFERENCE CARD (Print & Pin)

```
╔═══════════════════════════════════════════════════════════════════╗
║                    RECURRENCE QUICK REFERENCE                    ║
╠═══════════════════════════════════════════════════════════════════╣
║ BINARY SEARCH     T(n) = T(n/2) + 1          → Θ(log n)         ║
║ MERGE SORT        T(n) = 2T(n/2) + n         → Θ(n log n)       ║
║ QUICK SORT (avg)  T(n) = 2T(n/2) + n         → Θ(n log n)       ║
║ QUICK SORT (worst) T(n) = T(n-1) + n         → Θ(n²)            ║
║ STRASSEN          T(n) = 7T(n/2) + n²        → Θ(n^2.807)       ║
║ HEAPIFY           T(n) = 2T(n/2) + 1         → Θ(n)             ║
║ SELECTION SORT    T(n) = T(n-1) + n          → Θ(n²)            ║
║ BINARY TREE       T(n) = T(L) + T(R) + 1     → Θ(n)             ║
║ LCS / EDIT DIST   T(m,n) = DP table          → Θ(mn)            ║
║ 0/1 KNAPSACK      T(n,W) = DP table          → Θ(nW)            ║
║ MATRIX CHAIN      T(i,j) = min_k             → Θ(n³)            ║
║ FLOYD-WARSHALL    T(k,i,j) = min             → Θ(V³)            ║
║ FIBONACCI (naive) T(n) = T(n-1)+T(n-2)       → Θ(φ^n) ≈ 1.618^n║
║ FIBONACCI (DP)    T(n) = T(n-1)+T(n-2)       → Θ(n)            ║
╚═══════════════════════════════════════════════════════════════════╝

MASTER THEOREM:
T(n) = aT(n/b) + f(n)  |  c = log_b a
f(n) << n^c  → Case 1  → Θ(n^c)
f(n) = n^c log^k n → Case 2 → Θ(n^c log^{k+1} n)
f(n) >> n^c  → Case 3  → Θ(f(n))  (need regularity)
```

---

## 🏷️ Tags & Metadata

```yaml
tags:
  - DSA
  - GATE-DA
  - GATE-CS
  - Recurrence-Relations
  - Divide-and-Conquer
  - Dynamic-Programming
  - Master-Theorem
  - Algorithm-Analysis
  - Time-Complexity
  - GATE-Preparation
```