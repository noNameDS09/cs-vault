---
tags:
  - DSA
  - GATE-DA
  - Time-Complexity
  - Cheatsheet
  - Reference
aliases:
  - Time Complexity Cheatsheet
  - Big-O Reference
---

# ⏱️ Time & Space Complexity — Master Reference

> **Quick lookup** for all sorting, searching, and data structure operations. Essential for GATE DA and interview complexity analysis questions.

---

## 📊 Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable | In-Place | Notes |
|-----------|------|---------|-------|-------|--------|----------|-------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | ✅ | ✅ | Optimized: early exit if no swaps |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) | ❌ | ✅ | Min swaps (O(n)) |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | ✅ | ✅ | Best for small/nearly sorted |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ | ❌ | Stable, external sorting |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ | ✅* | Randomized pivot → O(n log n) expected |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ | ✅ | Guaranteed O(n log n) |
| **Timsort (Python)** | O(n) | O(n log n) | O(n log n) | O(n) | ✅ | ❌ | Hybrid merge+insertion, adaptive |
| **Counting Sort** | O(n+k) | O(n+k) | O(n+k) | O(n+k) | ✅ | ❌ | Integers in range [0, k] |
| **Radix Sort** | O(d(n+b)) | O(d(n+b)) | O(d(n+b)) | O(n+b) | ✅ | ❌ | d digits, base b |
| **Bucket Sort** | O(n+k) | O(n+k) | O(n²) | O(n+k) | ✅ | ❌ | Uniform distribution |

> *Quick Sort recursive stack: O(log n) average, O(n) worst

---

## 🔍 Search Algorithms

| Algorithm | Time | Space | Requires |
|-----------|------|-------|----------|
| **Linear Search** | O(n) | O(1) | Unsorted array |
| **Binary Search** | O(log n) | O(1) | **Sorted** array |
| **Ternary Search** | O(log₃ n) | O(1) | Unimodal function |
| **Jump Search** | O(√n) | O(1) | Sorted array |
| **Exponential Search** | O(log n) | O(1) | Unbounded sorted |
| **Interpolation Search** | O(log log n)* | O(1) | Uniformly distributed |
| **Fibonacci Search** | O(log n) | O(1) | Sorted array |

> *Average case for uniform distribution; worst O(n)

---

## 📦 Data Structure Operations

### Arrays / Lists (Python `list`)

| Operation | Time | Notes |
|-----------|------|-------|
| Access by index | O(1) | Random access |
| Search (unsorted) | O(n) | Linear scan |
| Search (sorted) | O(log n) | Binary search |
| Insert at end | O(1)* | Amortized |
| Insert at beginning | O(n) | Shifts all elements |
| Insert at middle | O(n) | Shifts elements |
| Delete at end | O(1) | |
| Delete at beginning | O(n) | Shifts all elements |
| Delete at middle | O(n) | Shifts elements |

### Linked List (Singly)

| Operation | Time | Notes |
|-----------|------|-------|
| Access by index | O(n) | No random access |
| Search | O(n) | |
| Insert at head | O(1) | |
| Insert at tail | O(1)* / O(n) | With/without tail pointer |
| Insert after node | O(1) | Given node reference |
| Delete head | O(1) | |
| Delete tail | O(n) | Need previous node |
| Delete node | O(1)* | Given node reference (copy next) |

### Doubly Linked List

| Operation | Time |
|-----------|------|
| Insert at head/tail | O(1) |
| Delete head/tail | O(1) |
| Delete given node | O(1) |
| Reverse traverse | O(n) |

### Hash Table (Python `dict` / `set`)

| Operation | Average | Worst | Notes |
|-----------|---------|-------|-------|
| Insert | O(1) | O(n) | Collisions |
| Lookup | O(1) | O(n) | |
| Delete | O(1) | O(n) | |
| Iterate all | O(n) | O(n) | |

> Python 3.7+: dict maintains insertion order (compact dict implementation)

### Stack / Queue / Deque

| Operation | Stack | Queue | Deque |
|-----------|-------|-------|-------|
| Push/Enqueue | O(1) | O(1) | O(1) |
| Pop/Dequeue | O(1) | O(1) | O(1) |
| Peek/Front | O(1) | O(1) | O(1) |
| Search | O(n) | O(n) | O(n) |

### Heap (Priority Queue)

| Operation | Time | Notes |
|-----------|------|-------|
| Build Heap (heapify) | O(n) | Floyd's algorithm |
| Insert | O(log n) | |
| Extract Min/Max | O(log n) | |
| Peek Min/Max | O(1) | |
| Decrease/Increase Key | O(log n) | Need position map |
| Merge (meld) | O(n) | Binary heap; O(log n) for Fibonacci |

### Binary Search Tree

| Operation | Average | Worst (skewed) | Balanced (AVL/Red-Black) |
|-----------|---------|----------------|--------------------------|
| Search | O(log n) | O(n) | O(log n) |
| Insert | O(log n) | O(n) | O(log n) |
| Delete | O(log n) | O(n) | O(log n) |
| Min/Max | O(log n) | O(n) | O(log n) |
| Successor/Predecessor | O(log n) | O(n) | O(log n) |
| Traversal | O(n) | O(n) | O(n) |

### Balanced BST (AVL / Red-Black Tree)

| Operation | Time |
|-----------|------|
| Search | O(log n) |
| Insert | O(log n) |
| Delete | O(log n) |
| Space | O(n) |

### Trie (Prefix Tree)

| Operation | Time | Space |
|-----------|------|-------|
| Insert | O(m) | O(ALPHABET_SIZE × N × M) |
| Search | O(m) | |
| Prefix Search | O(m) | |
| Delete | O(m) | |

> m = key length, N = number of keys, M = average key length

### Segment Tree

| Operation | Time | Space |
|-----------|------|-------|
| Build | O(n) | O(4n) |
| Point Update | O(log n) | |
| Range Query | O(log n) | |
| Lazy Propagation | O(log n) | |

### Fenwick Tree (BIT)

| Operation | Time | Space |
|-----------|------|-------|
| Build | O(n log n) / O(n)* | O(n) |
| Point Update | O(log n) | |
| Prefix Sum | O(log n) | |
| Range Sum | O(log n) | |

> *O(n) build: `bit[i] += bit[i + (i & -i)]` for i in 1..n

### Disjoint Set Union (Union-Find)

| Operation | Time |
|-----------|------|
| Find (with path compression) | O(α(n)) ≈ O(1) |
| Union (by rank/size) | O(α(n)) ≈ O(1) |

> α(n) = inverse Ackermann function < 5 for all practical n

---

## 🌐 Graph Algorithms

| Algorithm | Time | Space | Use Case |
|-----------|------|-------|----------|
| **BFS** | O(V + E) | O(V) | Shortest path (unweighted), level order |
| **DFS** | O(V + E) | O(V) | Cycle detection, topological sort, components |
| **Topological Sort (Kahn)** | O(V + E) | O(V) | DAG ordering |
| **Topological Sort (DFS)** | O(V + E) | O(V) | DAG ordering |
| **Dijkstra (Binary Heap)** | O((V+E) log V) | O(V) | Non-negative weights |
| **Dijkstra (Fibonacci Heap)** | O(E + V log V) | O(V) | Theoretical optimum |
| **Bellman-Ford** | O(VE) | O(V) | Negative weights, detect negative cycle |
| **SPFA** | O(E) avg, O(VE) worst | O(V) | Often faster than Bellman-Ford |
| **Floyd-Warshall** | O(V³) | O(V²) | All-pairs shortest path |
| **Kruskal (MST)** | O(E log E) | O(V) | Sparse graphs |
| **Prim (MST, Binary Heap)** | O(E log V) | O(V) | Dense graphs |
| **Prim (MST, Fibonacci)** | O(E + V log V) | O(V) | |
| **Kosaraju (SCC)** | O(V + E) | O(V) | Strongly connected components |
| **Tarjan (SCC)** | O(V + E) | O(V) | Single-pass SCC |
| **Bipartite Check** | O(V + E) | O(V) | 2-coloring |

---

## 💡 Dynamic Programming Patterns

| Pattern | Example | Time | Space (Optimized) |
|---------|---------|------|-------------------|
| **1D Linear** | Fibonacci, Climbing Stairs | O(n) | O(1) |
| **1D with Choice** | House Robber, Coin Change | O(n × k) | O(n) / O(k) |
| **2D Grid** | Unique Paths, Min Path Sum | O(mn) | O(min(m,n)) |
| **2D String** | LCS, Edit Distance | O(mn) | O(min(m,n)) |
| **Interval DP** | Burst Balloons, Matrix Chain | O(n³) | O(n²) |
| **Tree DP** | House Robber III, Diameter | O(n) | O(h) |
| **Digit DP** | Count numbers with property | O(digits × states) | |
| **Bitmask DP** | TSP, Assignment | O(n × 2ⁿ) | O(2ⁿ) |
| **Knapsack 0/1** | Max value with weight limit | O(nW) | O(W) |
| **Knapsack Unbounded** | Complete knapsack | O(nW) | O(W) |
| **LIS (Patience)** | Longest Increasing Subsequence | O(n log n) | O(n) |

---

## 🧮 Mathematical Complexity

| Function | Growth | Common In |
|----------|--------|-----------|
| O(1) | Constant | Hash access, array index |
| O(log n) | Logarithmic | Binary search, heap ops |
| O(√n) | Square root | Trial division, some number theory |
| O(n) | Linear | Scan, BFS/DFS, counting sort |
| O(n log n) | Linearithmic | Merge sort, heap sort, BST ops |
| O(n²) | Quadratic | Nested loops, insertion sort |
| O(n³) | Cubic | Floyd-Warshall, matrix multiply |
| O(2ⁿ) | Exponential | Subsets, brute force |
| O(n!) | Factorial | Permutations, TSP brute force |
| O(nⁿ) | Super-exponential | Rare |

### Common Summations

| Sum | Closed Form |
|-----|-------------|
| Σᵢ₌₁ⁿ 1 | n |
| Σᵢ₌₁ⁿ i | n(n+1)/2 |
| Σᵢ₌₁ⁿ i² | n(n+1)(2n+1)/6 |
| Σᵢ₌₁ⁿ i³ | (n(n+1)/2)² |
| Σᵢ₌₀ⁿ rⁱ | (rⁿ⁺¹ - 1)/(r - 1) for r ≠ 1 |
| Σᵢ₌₁ⁿ log i | log(n!) ≈ n log n (Stirling) |

### Master Theorem

For T(n) = aT(n/b) + f(n) where a ≥ 1, b > 1:

| Case | Condition | Solution |
|------|-----------|----------|
| 1 | f(n) = O(n^log_b(a) - ε) | Θ(n^log_b(a)) |
| 2 | f(n) = Θ(n^log_b(a) logᵏ n) | Θ(n^log_b(a) logᵏ⁺¹ n) |
| 3 | f(n) = Ω(n^log_b(a) + ε) & af(n/b) ≤ cf(n) | Θ(f(n)) |

Examples:
- Merge Sort: a=2, b=2, f(n)=n → Case 2 (k=0) → Θ(n log n)
- Binary Search: a=1, b=2, f(n)=1 → Case 2 (k=0) → Θ(log n)
- Strassen: a=7, b=2, f(n)=n² → Case 1 → Θ(n^log₂7) ≈ Θ(n^2.81)

---

## 🎯 GATE DA Specific Complexity Questions

> **Frequently tested patterns in GATE DA:**

1. **Recurrence Relations**
   - T(n) = 2T(n/2) + n → Θ(n log n)
   - T(n) = T(n-1) + n → Θ(n²)
   - T(n) = 2T(n/2) + 1 → Θ(n)
   - T(n) = T(n/2) + 1 → Θ(log n)

2. **Loop Analysis**
   ```python
   # O(n log n)
   for i in range(1, n+1):
       for j in range(1, n+1, i):  # harmonic series
           pass

   # O(n²)
   for i in range(n):
       for j in range(i, n):
           pass

   # O(n)
   i = 1
   while i < n:
       i *= 2

   # O(log n)
   i = n
   while i > 1:
       i //= 2
   ```

3. **Data Structure Choice**
   - Need O(1) insert/delete/search → Hash Table
   - Need ordered + O(log n) ops → Balanced BST
   - Need prefix sums + updates → Fenwick Tree
   - Need range min/max + updates → Segment Tree
   - Need dynamic connectivity → DSU
   - Need top-K → Heap

4. **Amortized Analysis**
   - Dynamic array append: O(1) amortized
   - Hash table resize: O(1) amortized
   - Splay tree: O(log n) amortized
   - DSU with path compression: O(α(n)) ≈ O(1)

---

## 📋 Quick Reference Card (Print This)

```
╔═══════════════════════════════════════════════════════════════════╗
║                    COMPLEXITY QUICK REFERENCE                    ║
╠════════════════╦═══════════════════════════════════════════════════╣
║ Operation      ║ Array   List    Dict    Heap    BST    Graph   ║
╠════════════════╬═══════════════════════════════════════════════════╣
║ Access         ║ O(1)    O(n)    O(1)    —       O(log n) —     ║
║ Search         ║ O(n)    O(n)    O(1)    —       O(log n) O(V+E)║
║ Insert         ║ O(n)    O(1)*   O(1)    O(log n) O(log n) O(1)  ║
║ Delete         ║ O(n)    O(1)*   O(1)    O(log n) O(log n) O(1)  ║
║ Sort           ║ O(n log n)        —       —       —       —    ║
║ Min/Max        ║ O(n)    O(n)    O(n)    O(1)    O(log n) —     ║
╚════════════════╩════════════════════════════════════════════════════╝
* with tail pointer / at head

╔═══════════════════════════════════════════════════════════════════╗
║  SORTING:  Merge=Quick=Heap O(n log n)  │  Counting=Radix O(n+k)  ║
║  SEARCH:   Binary O(log n) needs SORTED ║  Hash O(1) average      ║
║  GRAPH:    BFS/DFS O(V+E)  │  Dijkstra O(E log V)  │  Bellman O(VE)║
║  MST:      Kruskal O(E log E)  Prim O(E log V)                      ║
║  DP:       1D O(n)  2D O(mn)  Interval O(n³)  Bitmask O(n2ⁿ)       ║
╚═══════════════════════════════════════════════════════════════════╝
```

---

## 🏷️ Tags

```yaml
tags:
  - DSA
  - GATE-DA
  - Time-Complexity
  - Space-Complexity
  - Big-O
  - Cheatsheet
  - Reference
  - Interview-Preparation
```