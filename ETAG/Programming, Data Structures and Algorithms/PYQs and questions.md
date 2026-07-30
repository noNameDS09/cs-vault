---
tags:
  - DSA
  - GATE-DA
  - PYQ
  - Previous-Year-Questions
  - Interview-Preparation
aliases:
  - DSA PYQs
  - GATE DA DSA Questions
  - Past Year Questions
---

# 📝 GATE DA — Programming, Data Structures & Algorithms: PYQs & Practice Questions

> **Comprehensive collection** of GATE DA (2024, 2025) previous year questions for the DSA section, plus high-yield practice questions matching the syllabus. Each question includes answer, detailed explanation, and **GATE shortcuts**.

---

## 📋 GATE DA DSA Syllabus Coverage

| Syllabus Topic | Weightage | Question Numbers |
|----------------|-----------|------------------|
| Python Programming | ~2-3 Qs | Basic syntax, collections, complexity |
| Stacks, Queues, Linked Lists | ~1-2 Qs | Operations, applications |
| Trees (Binary, BST) | ~2-3 Qs | Traversals, properties, reconstruction |
| Search Algorithms | ~1 Q | Binary search, variants |
| Sorting Algorithms | ~1-2 Qs | Complexity, behavior on sorted input |
| Divide & Conquer | ~1 Q | Merge sort, Quick sort |
| Graph Theory (Intro) | ~2-3 Qs | BFS/DFS, Topological Sort, Shortest Path |

---

## 🟢 GATE DA 2025 — DSA Questions

> **Source:** `[[Papers/DA25]]`

### Q16. Dependency Preservation (Database/DSA Crossover)

> **Concept:** A decomposition is **dependency-preserving** if all functional dependencies can be checked **without joining** the decomposed relations.
> 
> If it is **not dependency-preserving**, the original relation must be reconstructed using a **JOIN** to verify or enforce dependencies.

**Answer:** (C) **Join**

---

### Q17. Relational Algebra Expression

> **Expression:**
> $$
> \pi_{\text{owner}}\left(\text{Own} \bowtie \left(\sigma_{\text{color}=\text{"red"}}\left(\text{Car} \bowtie \left(\sigma_{\text{maker}=\text{"ABC"}}(\text{Make})\right)\right)\right)\right)
> $$

**Step-by-step:**
1. `σ_maker="ABC"(Make)` → Models made by ABC
2. `Car ⋈ Make` → Cars made by ABC
3. `σ_color="red"` → Red cars made by ABC
4. `Own ⋈ ...` → Owners of those cars
4. `π_owner` → Return only owner names

**Answer:** (C) **All owners of a red car made by ABC**

---

## 🟢 GATE DA 2024 — DSA Questions

> **Source:** `[[Papers/DA24]]`

---

### Q18. Modeling Approach Matching

> **Match each concept to its fundamental approach:**

| Concept | Category |
|---------|----------|
| (p) Principal Component Analysis | (ii) Dimensionality Reduction |
| (q) Naïve Bayes Classification | (iii) Generative Model |
| (r) Logistic Regression | (i) Discriminative Model |

**Answer:** (p)→(ii), (q)→(iii), (r)→(i)

---

### Q19. K-Means Clustering Convexity Property

> **Question:** In Euclidean k-means, points A=[1,1] and B=[-1,1] belong to cluster 3. Which point must also belong to cluster 3?
> 
> (A) [0,0]  (B) [0,2]  (C) [2,0]  (D) [0,1]

**Reasoning:**
- K-means clusters = Voronoi cells = **convex sets**
- Convex property: If two points in set, **entire line segment** between them is in set
- Line segment joining [1,1] and [-1,1] is all points (x,1) where -1 ≤ x ≤ 1
- [0,1] lies on this segment

**Answer:** (D) **[0, 1]**

> **🎯 GATE Shortcut:** Euclidean k-means clusters are **always convex**. If two points in same cluster → all points on line between them also in cluster.

---

### Q20. Naïve Bayes Parameter Count

> **Formula:** For m classes, K binary attributes: **Independent parameters = (m-1) + mK**
> 
> For 2 classes: **(2-1) + 2K = 2K + 1**

**Answer:** **2K + 1**

> **🎯 GATE Shortcut:** Memorize: `Naive Bayes params = (classes - 1) + classes × binary_attributes`

---

### Q23. Admissible Heuristic Combination

> **Given:** $h_1$ and $h_2$ are admissible heuristics ($0 \le h_i \le h^*$)
> **Which is always admissible?**
> 
> (A) $h_1 + h_2$  
> (B) $h_1 \times h_2$  
> (C) $\frac{h_1}{h_2}$  
> (D) $|h_1 - h_2|$

**Analysis:**
- (A) Sum: Can exceed $h^*$ → ❌
- (B) Product: Can exceed $h^*$ → ❌
- (C) Ratio: Can exceed $h^*$ → ❌
- (D) Absolute difference: $|h_1 - h_2| \le h^*$ → ✅

**Answer:** (D) **$|h_1 - h_2|$**

> **🎯 GATE Shortcut:** For admissible $h_1, h_2$:
> - ❌ Sum, Product, Ratio
> - ✅ **Max, Min, Absolute Difference**
> - **Bonus:** $\max(h_1, h_2)$ is also always admissible (standard A* combination)

---

### Q28. Tree Reconstruction from Traversals

> **Question:** Which traversal pair(s) can reconstruct a **full binary tree**?
> 
> (A) Preorder + Inorder  
> (B) Inorder + Postorder  
> (C) Preorder + Postorder  
> (D) Inorder only

**Full Binary Tree:** Every node has 0 or 2 children (no single-child nodes).

| Pair | General Binary Tree | Full Binary Tree |
|------|---------------------|------------------|
| Pre + In | ✅ | ✅ |
| In + Post | ✅ | ✅ |
| Pre + Post | ❌ (ambiguity with single child) | ✅ |
| In only | ❌ | ❌ |

**Answer:** **(A), (B), (C)** — all three work for full binary tree. If single-select: **(C)** (the one that *requires* full binary tree property)

> **🎯 GATE Shortcut:** 
> - Pre+In → ✅ Always
> - In+Post → ✅ Always
> - Pre+Post → ❌ General, ✅ **Full** binary tree only
> - Inorder alone → ❌ Never

---

### Q30. Quicksort Swaps on Sorted Array

> **Array:** [60, 70, 80, 90, 100] (already sorted)
> **Pivot:** Always last element
> **Question:** Minimum number of swaps?

**Trace:**
- Pivot=100: all elements < 100 → no swaps, recurse on [60,70,80,90]
- Pivot=90: all < 90 → no swaps, recurse on [60,70,80]
- Pivot=80: all < 80 → no swaps, recurse on [60,70]
- Pivot=70: all < 70 → no swaps

**Answer:** **0**

> **🎯 GATE Shortcut:** Already sorted + last element pivot → **worst-case comparisons (O(n²)), but minimum swaps = 0** (if self-swaps not counted). If self-swaps counted, answer would be n-1.

---

### Q31. SQL Join Count (Database/DSA)

> **Tables:** Jaipur teams (IDs: 2,1,6), Raiders with RaidPoints>200 (IDs: 1,2,5,6)
> **Question:** Rows in result of join?

**Matching IDs:** 1, 2, 6 → **3 rows**

**Answer:** **3**

---

### Q36. Expected Dice Throws (Probability/DP)

> **Problem:** Expected throws to get two consecutive even numbers on fair die.

**States:**
- $E_0$: previous throw not even
- $E_1$: previous throw was even

**Equations:**
$$
E_0 = 1 + \frac{1}{2}E_0 + \frac{1}{2}E_1
$$
$$
E_1 = 1 + \frac{1}{2}(0) + \frac{1}{2}E_0 = 1 + \frac{1}{2}E_0
$$

**Solving:**
$E_0 = 2 + E_1 = 2 + 1 + \frac{1}{2}E_0 = 3 + \frac{1}{2}E_0$
$\frac{1}{2}E_0 = 3 \Rightarrow E_0 = 6$

**Answer:** **6** (Option C)

> **🎯 GATE Shortcut:** For "two consecutive successes" with probability $p$:
> $$E = \frac{1+p}{p^2} = \frac{1+0.5}{0.25} = 6$$
> General: $k$ consecutive successes → $E = \frac{1-p^k}{p^k(1-p)}$

---

### Q38. Tree Node Count (Recursive Function)

> **Tree:** Root 0 has children 1,2; 1 has children 3,4; 2 has children 5,6,7,8 (leaves)
> **Function:** `count(node)` returns 1 + sum of count(children)

**Calculation:**
- Leaves (3,4,5,6,7,8): each returns 1
- Node 1: 1 + 1 + 1 = 3? Wait, leaves return 1, so 1 + 1 + 1 = 3... but paper says 4?
- Wait, let's re-read: "Leaves (3,4,5,6,7,8) → each returns 1"
- Node 1: children 3,4 → 1 + 1 + 1 = 3? Paper says 4.
- Node 2: children 5,6,7,8 → 1 + 1+1+1+1 = 5? Paper says 4.
- Root 0: 1 + 4 + 4 = 9

**Answer:** **9**

> **Note:** The function counts the node itself + all descendants. Tree has 9 nodes total.

---

### Q40. Binary Search Recurrence

> **Question:** Recurrence for binary search?

**Answer:** (A) **$T(n) = T(n/2) + O(1)$**

> **🎯 GATE Shortcut:** 
> - Binary Search: $T(n) = T(n/2) + O(1) \to \Theta(\log n)$
> - Merge Sort: $T(n) = 2T(n/2) + O(n) \to \Theta(n \log n)$
> - Quick Sort (avg): $T(n) = 2T(n/2) + O(n) \to \Theta(n \log n)$
> - Quick Sort (worst): $T(n) = T(n-1) + O(n) \to \Theta(n^2)$

---

## 🟡 Additional High-Yield GATE DA DSA Questions

> **Curated from GATE CSE overlap + GATE DA pattern analysis**

---

### Python Programming

---

#### PY1. List Slicing & Mutation

```python
a = [1, 2, 3, 4, 5]
b = a[1:4]
b[0] = 99
print(a, b)
```

**Options:**
(A) [1, 2, 3, 4, 5] [99, 3, 4]  
(B) [1, 99, 3, 4, 5] [99, 3, 4]  
(C) [1, 2, 3, 4, 5] [1, 2, 3]  
(D) [1, 99, 3, 4, 5] [2, 3, 4]

**Answer:** (B) **`[1, 99, 3, 4, 5] [99, 3, 4]`**

**Explanation:** Slice creates new list, but elements are references. For integers (immutable), `b[0]=99` replaces reference in `b` only. Wait — slice of list creates **shallow copy** (new list object). `b = a[1:4]` creates `[2,3,4]`. Then `b[0]=99` changes `b` to `[99,3,4]`. Original `a` unchanged.

**Wait — correction:** `a[1:4]` creates a **new list** with copies of references. Since ints are immutable, `b[0]=99` only affects `b`. So `a` stays `[1,2,3,4,5]`.

**Correct Answer:** (A) **`[1, 2, 3, 4, 5] [99, 3, 4]`**

> **🎯 GATE Shortcut:** 
> - `b = a[:]` or `a[1:4]` → **shallow copy** (new list, same element references)
> - For **immutables** (int, str, tuple): modification creates new object, original unaffected
> - For **mutables** (list, dict): `b[0].append(x)` affects both; `b[0] = new` affects only b

---

#### PY2. Default Mutable Argument Trap

```python
def append_to(element, lst=[]):
    lst.append(element)
    return lst

print(append_to(1))
print(append_to(2))
print(append_to(3, []))
```

**Output?**
```
[1]
[1, 2]
[3]
```

**Answer:** **`[1]` then `[1, 2]` then `[3]`**

**Explanation:** Default argument `lst=[]` evaluated **once at function definition**. All calls without explicit `lst` share the same list.

> **🎯 GATE Shortcut:** **Never use mutable defaults.** Use `lst=None` and `if lst is None: lst = []`

---

#### PY3. Time Complexity of List Operations

```python
# Which is O(1)?
# (A) lst.insert(0, x)
# (B) lst.pop()
# (C) lst.pop(0)
# (D) x in lst
```

**Answer:** (B) **`lst.pop()`** — removes from end, O(1)

| Operation | Time |
|-----------|------|
| `append` / `pop()` | O(1) amortized |
| `insert(0, x)` / `pop(0)` | O(n) |
| `x in lst` | O(n) |
| `lst[i]` | O(1) |

---

### Stacks & Queues

---

#### SQ1. Stack Permutations

> **Question:** Which permutation of 1,2,3,4,5 **cannot** be generated using a stack (input order 1,2,3,4,5)?

**Options:**
(A) 4,5,3,2,1  
(B) 2,3,4,5,1  
(C) 3,4,5,1,2  
(D) 1,2,3,4,5

**Answer:** (C) **3,4,5,1,2**

**Reasoning:** Stack permutation constraint: cannot have pattern **3-1-2** (i.e., output ...3...1...2... where 3>1<2 and 3 pushed before 1). In 3,4,5,1,2: we see 3, then later 1, then 2 (3>1<2) — forbidden pattern.

> **🎯 GATE Shortcut:** Forbidden pattern for stack: **output a > c > b where a comes before b before c**. Or simply: avoid **2-3-1** pattern in output relative to input order.

---

#### SQ2. Queue Using Two Stacks

> **Operations:** Enqueue O(1), Dequeue amortized O(1) using two stacks.

```python
class Queue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    
    def enqueue(self, x):
        self.in_stack.append(x)
    
    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()
```

**Question:** Amortized cost of dequeue?

**Answer:** **O(1)** — each element pushed to in_stack (1), popped from in_stack (1), pushed to out_stack (1), popped from out_stack (1) = 4 operations total = O(1) amortized

---

### Linked Lists

---

#### LL1. Detect & Remove Loop

> **Given:** Singly linked list with possible loop. Detect loop and remove it in O(n) time, O(1) space.

**Algorithm (Floyd's Cycle Detection):**
```python
def detect_and_remove(head):
    slow = fast = head
    # 1. Detect loop
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return  # No loop
    
    # 2. Find loop start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    # 3. Find last node in loop
    while fast.next != slow:
        fast = fast.next
    
    # 4. Break loop
    fast.next = None
```

**Question:** Why does step 2 work?

**Proof:** Let distance from head to loop start = $L$, loop start to meeting point = $k$, loop length = $C$. 
- Slow travels: $L + k$
- Fast travels: $L + k + mC = 2(L + k) \Rightarrow L + k = mC \Rightarrow L = mC - k$
- Reset slow to head. When slow moves $L$ steps, fast moves $L$ steps from meeting point: $k + L = k + mC - k = mC$ → back to loop start!

---

### Trees & Binary Trees

---

#### TR1. Tree Traversals

```text
       1
      / \
     2   3
    / \   \
   4   5   6
```

**Question:** Match traversal to output.

| Traversal | Output |
|-----------|--------|
| Preorder | 1,2,4,5,3,6 |
| Inorder | 4,2,5,1,3,6 |
| Postorder | 4,5,2,6,3,1 |
| Level Order | 1,2,3,4,5,6 |

> **🎯 GATE Shortcut:** 
> - **Preorder:** Root first → **Root, Left, Right**
> - **Inorder:** Root middle → **Left, Root, Right** (BST gives sorted!)
> - **Postorder:** Root last → **Left, Right, Root**
> - **Level Order:** BFS with queue

---

#### TR2. Height of Tree from Parent Array

> **Input:** `parent = [-1, 0, 0, 1, 1]` (index = node, value = parent)
> **Question:** Height of tree?

**Tree:**
```
    0
   / \
  1   2
 / \
3   4
```
Height = 2 (edges) or 3 (nodes). GATE usually asks for **edges** = **2**.

**Algorithm:** 
```python
def height(parent):
    n = len(parent)
    depth = [0]*n
    def get_depth(i):
        if depth[i]: return depth[i]
        if parent[i] == -1: return 0
        depth[i] = 1 + get_depth(parent[i])
        return depth[i]
    return max(get_depth(i) for i in range(n))
```

---

#### TR3. BST Validation

> **Question:** Which is correct for checking if a binary tree is a BST?

```python
# (A) Check node.val > left.val and node.val < right.val
# (B) Check inorder traversal is sorted
# (C) Pass min/max bounds recursively
# (D) All of the above
```

**Answer:** (C) **Pass min/max bounds recursively** — only correct method.

**Why (A) fails:** Doesn't check entire subtree bounds (e.g., right child of left subtree could be > root)

**Why (B) fails:** Requires O(n) space for traversal, and fails for duplicate values unless handled carefully

**Correct (C):**
```python
def is_bst(node, min_val=-inf, max_val=inf):
    if not node: return True
    if not (min_val < node.val < max_val): return False
    return (is_bst(node.left, min_val, node.val) and 
            is_bst(node.right, node.val, max_val))
```

> **🎯 GATE Shortcut:** BST validation = **range propagation**. Each node gets valid (min, max) from ancestors.

---

#### TR4. Number of Binary Trees / BSTs

> **Question:** Number of structurally different binary trees with n nodes? Number of BSTs with n distinct keys?

**Answer:**
- Binary Trees (unlabeled): **Catalan number** $C_n = \frac{1}{n+1}\binom{2n}{n}$
- BSTs with distinct keys: **Same Catalan number** $C_n$
- Binary trees with n *labeled* nodes: $C_n \times n!$

| n | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $C_n$ | 1 | 2 | 5 | 14 | 42 |

---

### Search Algorithms

---

#### SE1. Binary Search Variants

> **Question:** Find first occurrence of target in sorted array with duplicates.

```python
def first_occurrence(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo if lo < len(arr) and arr[lo] == target else -1
```

**Loop Invariant:** `arr[0..lo-1] < target`, `arr[hi..] >= target`

**Variants:**
| Variant | Condition | Return |
|---------|-----------|--------|
| Lower bound (first ≥) | `arr[mid] < target` | `lo` |
| Upper bound (first >) | `arr[mid] <= target` | `lo` |
| Exact match | `arr[mid] == target` | `mid` |

---

#### SE2. Search in Rotated Sorted Array

```python
def search(nums, target):
    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if nums[mid] == target: return mid
        # Left half sorted
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        # Right half sorted
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1
```

**Time:** O(log n) — **binary search works** because at least one half is always sorted.

---

### Sorting Algorithms

---

#### SO1. QuickSort Partition Trace

> **Array:** [5, 3, 8, 4, 2, 7, 1, 10]
> **Pivot:** Last element (10)
> **After one partition:** ?

**Answer:** Array unchanged, pivot at end. All elements < 10.

> **With pivot = 4 (index 3):**
> Using Lomuto: [3, 2, 1, **4**, 5, 7, 8, 10] — pivot at index 3

> **🎯 GATE Shortcut:** 
> - **Already sorted + last pivot** → worst case O(n²) comparisons, **0 swaps** (minimum)
> - **Reverse sorted + last pivot** → worst case O(n²), maximum swaps

---

#### SO2. Stability of Sorting

| Algorithm | Stable? |
|-----------|---------|
| Bubble Sort | ✅ |
| Insertion Sort | ✅ |
| Merge Sort | ✅ |
| **Quick Sort** | ❌ |
| **Heap Sort** | ❌ |
| Selection Sort | ❌ |
| Counting Sort | ✅ |
| Radix Sort | ✅ (if stable subroutine) |

> **Question:** Which sorting algorithm is **stable, in-place, O(n log n) worst-case**?
> **Answer:** **None exists** (theoretical lower bound). Merge sort is stable O(n log n) but not in-place. Heap sort is in-place O(n log n) but not stable.

---

### Divide & Conquer

---

#### DC1. Merge Sort Recurrence

$$T(n) = 2T(n/2) + \Theta(n) \to \Theta(n \log n)$$

> **Question:** Space complexity of merge sort?
> **Answer:** **O(n)** auxiliary (not in-place)

> **Question:** Space complexity of Quick Sort?
> **Answer:** **O(log n)** average (stack), **O(n)** worst (stack)

---

#### DC2. Master Theorem Applications

| Recurrence | a | b | f(n) | Case | Solution |
|------------|---|---|------|------|----------|
| T(n) = 2T(n/2) + n | 2 | 2 | n | 2 (k=0) | Θ(n log n) |
| T(n) = 2T(n/2) + 1 | 2 | 2 | 1 | 1 | Θ(n) |
| T(n) = T(n/2) + 1 | 1 | 2 | 1 | 2 (k=0) | Θ(log n) |
| T(n) = 4T(n/2) + n² | 4 | 2 | n² | 2 (k=0) | Θ(n² log n) |
| T(n) = 3T(n/4) + n log n | 3 | 4 | n log n | 1 | Θ(n^log₄3) |

---

### Graph Theory (Introduction)

---

#### GR1. BFS vs DFS Properties

| Property | BFS | DFS |
|----------|-----|-----|
| Data Structure | Queue | Stack (recursion) |
| Shortest Path (unweighted) | ✅ | ❌ |
| Cycle Detection (undirected) | ✅ | ✅ |
| Cycle Detection (directed) | ❌ | ✅ (colors) |
| Topological Sort | ✅ (Kahn) | ✅ (post-order) |
| Connected Components | ✅ | ✅ |
| Bipartite Check | ✅ | ✅ |
| Space (worst) | O(V) | O(V) |

---

#### GR2. Topological Sort — Kahn's Algorithm

```python
def topological_sort(graph, n):
    indeg = [0]*n
    for u in graph:
        for v in graph[u]:
            indeg[v] += 1
    
    q = deque([i for i in range(n) if indeg[i] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    
    return order if len(order) == n else []  # cycle if empty
```

**Question:** If multiple valid topological orders exist, Kahn's algorithm with queue produces which one?

**Answer:** Lexicographically smallest (if vertices processed in order and queue is FIFO)

---

#### GR3. Dijkstra's Algorithm

> **Constraint:** **Non-negative edge weights only**

```python
def dijkstra(graph, start, n):
    dist = [inf]*n
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue  # stale entry
        for v, w in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
    return dist
```

**Time:** O((V+E) log V) with binary heap

> **Question:** Why does Dijkstra fail with negative edges?
> **Answer:** Greedy choice (pick min distance vertex) assumes distance can't be improved later. Negative edge can create shorter path to already-processed vertex.

---

#### GR4. Bellman-Ford

> **Handles:** Negative weights, **detects negative cycles**

```python
def bellman_ford(edges, n, start):
    dist = [inf]*n
    dist[start] = 0
    for _ in range(n-1):
        for u, v, w in edges:
            if dist[u] != inf and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
    # Check negative cycle
    for u, v, w in edges:
        if dist[u] != inf and dist[v] > dist[u] + w:
            return None  # negative cycle
    return dist
```

**Time:** O(VE)

---

#### GR5. Minimum Spanning Tree

| Algorithm | Time | Best For |
|-----------|------|----------|
| **Kruskal** | O(E log E) | Sparse graphs |
| **Prim (Binary Heap)** | O(E log V) | Dense graphs |
| **Prim (Fibonacci Heap)** | O(E + V log V) | Theoretical optimum |

> **Question:** Both produce same MST weight?
> **Answer:** **Yes**, if all edge weights distinct → unique MST. If duplicates → same weight, possibly different trees.

---

### Question

Consider the following undirected graph:

```text
    A      B
     \    /
       E
     /   \
    C     D
```

**Question:**  
If the starting vertex for BFS is **not specified** and you may start from **any vertex**, how many **distinct BFS traversal orderings** are possible? Assume that the neighbors of a vertex may be visited in any order.

---

### Answer

Consider each possible starting vertex.

|Starting Vertex|Number of BFS Orderings|
|---|--:|
|E|(4! = 24)|
|A|(3! = 6)|
|B|(3! = 6)|
|C|(3! = 6)|
|D|(3! = 6)|

Total number of distinct BFS orderings:

$$
\begin{aligned}
24 + 6 + 6 + 6 + 6 &= 48
\end{aligned}

\boxed{48}
$$

### Exam Tip

For these questions:

1. Choose each possible starting vertex.
    
2. Perform BFS level by level.
    
3. Count the valid permutations of vertices discovered at the same BFS level while respecting the FIFO queue.
    
4. Add the counts for all possible starting vertices (only if the source is not fixed).
    




## 🟡 Practice Questions by Topic

> **Solve these for mastery. No solutions — question types only.**

---

### Topic: Python & Complexity
1. Trace output of nested list comprehensions with side effects
2. Time complexity of `sum(lst[i] for i in range(0, n, 2))` vs list slicing
3. Dictionary iteration order guarantees (Python 3.7+)
4. `@lru_cache` vs manual memoization — memory behavior difference

### Topic: Stacks & Queues
5. Implement queue with two stacks — amortized analysis proof
6. Evaluate postfix expression — algorithm & complexity
7. Next greater element to right — monotonic stack pattern
8. Largest rectangle in histogram — stack application
9. Valid parentheses with wildcards `*` — greedy/stack hybrid

### Topic: Linked Lists
10. Reverse linked list in groups of k
11. Merge k sorted linked lists — heap vs divide&conquer
12. Add two numbers represented as linked lists
13. Flatten multilevel doubly linked list
14. Copy linked list with random pointer — O(1) space approach

### Topic: Trees
15. Construct binary tree from preorder + inorder
16. Construct binary tree from inorder + postorder
17. Serialize/deserialize binary tree — multiple formats
18. Lowest common ancestor (BST vs binary tree)
18. Diameter of binary tree — single traversal
19. Maximum path sum (any node to any node)
20. Check if binary tree is subtree of another
21. Convert sorted array to balanced BST
22. Recover BST with two swapped nodes

### Topic: Heaps
23. Find median from data stream — two heaps
24. Kth largest element in stream
25. Merge k sorted arrays — min-heap
26. Top k frequent elements — bucket sort vs heap
27. K closest points to origin — max-heap of size k

### Topic: Binary Search
28. Search in 2D matrix (row/col sorted)
29. Find peak element — O(log n)
30. Search in rotated sorted array with duplicates
31. Minimize maximum subarray sum (split array)
32. Koko eating bananas / capacity to ship packages

### Topic: Sorting
33. Sort colors (Dutch national flag) — 3-way partition
34. Count inversions — merge sort modification
35. External merge sort — disk-based sorting
36. Stability importance — when it matters

### Topic: Graphs
37. Number of islands — BFS/DFS/Union-Find
38. Clone graph — BFS with hashmap
39. Course schedule I/II — topological sort
40. Alien dictionary — topological sort on derived graph
41. Network delay time — Dijkstra
42. Cheapest flights within K stops — Bellman-Ford / modified Dijkstra
43. Minimum spanning tree — Kruskal + DSU
44. Find critical/psuedo-critical edges in MST
45. Word ladder — bidirectional BFS
46. Strongly connected components — Kosaraju/Tarjan
47. Bridges in graph — Tarjan's algorithm

### Topic: Dynamic Programming
48. 0/1 Knapsack — space optimization
49. Longest increasing subsequence — O(n log n)
50. Edit distance — 2D DP
51. Coin change / coin change 2
52. House robber I/II/III (tree)
53. Maximum product subarray
54. Regular expression matching
55. Burst balloons — interval DP
56. Palindrome partitioning — backtracking + DP

### Topic: Greedy
57. Interval scheduling / meeting rooms
58. Fractional knapsack
59. Jump game I/II
60. Gas station
61. Task scheduler

### Topic: Backtracking
62. N-Queens
63. Sudoku solver
64. Generate parentheses
65. Word search

### Topic: Advanced Data Structures
66. Trie — implement, prefix search, autocomplete
67. Segment tree — range sum/min/max with updates
68. Fenwick tree — prefix sum, inversion count
69. DSU — dynamic connectivity, accounts merge
70. Monotonic stack — next greater, histogram, trapping rain water

---

## 🎯 GATE DA Exam Strategy for DSA

### Marks Distribution (Estimated)
| Question Type | Count | Marks Each | Total |
|---------------|-------|------------|-------|
| MCQ (1 mark) | 5-7 | 1 | 5-7 |
| MCQ (2 marks) | 3-5 | 2 | 6-10 |
| MSQ (1-2 marks) | 2-3 | 1-2 | 2-6 |
| NAT (1-2 marks) | 2-4 | 1-2 | 2-8 |
| **Total DSA** | | | **~15-25 marks** |

### High-Yield Topics (Priority Order)
1. **Trees (BST, traversals, properties)** — 3-4 questions guaranteed
2. **Graphs (BFS/DFS, Topological Sort, Shortest Path)** — 3-4 questions
3. **Sorting (Quick/Merge behavior, complexity)** — 2-3 questions
4. **Binary Search (variants, rotated array)** — 1-2 questions
5. **Stacks/Queues (applications, stack permutations)** — 1-2 questions
6. **Python (list/dict operations, complexity)** — 1-2 questions
7. **Heaps (median, top-k, Dijkstra/Prim)** — 1-2 questions
8. **Linked Lists (cycle, reversal, merge)** — 0-1 question
9. **DP/Greedy/Backtracking** — Rare in DA, but possible 1 question

### GATE Shortcuts Cheatsheet

| Pattern | Shortcut |
|---------|----------|
| BST from traversals | Inorder + (Pre/Post) ✅ always; Pre+Post ✅ only full tree |
| QuickSort on sorted | Max comparisons, **0 swaps** (min) |
| Stack permutation | Forbidden: **3-1-2** pattern (2-3-1 in output order) |
| Dijkstra | Non-negative weights only; fails with negative |
| MST | Kruskal: sparse; Prim: dense; both give same weight |
| Tree height | Edges = nodes-1 on longest path |
| Catalan numbers | BSTs with n keys = Binary trees with n nodes = $C_n$ |
| Admissible heuristic combos | Max, Min, \|diff\| ✅; Sum, Prod, Ratio ❌ |
| K-means clusters | **Always convex** in Euclidean space |

---

## 📚 Recommended Practice Resources

| Resource | Use For |
|----------|---------|
| `[[dsa/Solved]]` | LeetCode solutions with explanations |
| `[[Programming, Data Structures and Algorithms]]` | Theory + implementations |
| `[[Time Complexities]]` | Quick complexity reference |
| GATE DA 2024/2025 papers | Actual exam pattern |
| GATE CSE 2020-2023 (DSA subset) | Extra practice for overlapping topics |
| LeetCode "GATE DA" tag / custom list | Targeted practice |

---

## 🏷️ Tags

```yaml
tags:
  - DSA
  - GATE-DA
  - PYQ
  - Previous-Year-Questions
  - Interview-Preparation
  - Trees
  - Graphs
  - Sorting
  - Searching
  - Dynamic-Programming
  - Data-Structures
  - Algorithms
  - Python
```