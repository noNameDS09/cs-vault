	Good context. You have the right tree foundation — that's all you need to get this. And for competitive programming, segment trees are one of the highest-leverage data structures you can learn. Problems that would take O(n) per query drop to O(log n).

One honest thing to set expectations: segment trees are **not commonly asked in placement interviews** at the ₹15 LPA level. They show up in competitive programming (Codeforces Div 2 D/E, ICPC). So this is the right place to learn it — just know it's a CP skill, not a placement priority.

Let's go slow and steady, same style as DP.

---

## The problem segment trees solve

First, understand **why** segment trees exist. Consider this:

You have an array `nums = [2, 4, 3, 1, 6, 7, 2, 5]` and you need to handle two operations repeatedly:

```
1. Query  → "What is the sum of elements from index l to r?"
2. Update → "Change nums[i] to a new value"
```

You'll get thousands of these queries and updates mixed together.

**Naive approach:**

```python
# Query: loop from l to r
def query(l, r):
    return sum(nums[l:r+1])   # O(n) per query

# Update: direct assignment
def update(i, val):
    nums[i] = val             # O(1) per update
```

Query is O(n) — with 10⁵ queries on an array of size 10⁵, that's **10¹⁰ operations**. Too slow.

**Prefix sum approach:**

```python
# Precompute prefix sums
prefix[i] = nums[0] + nums[1] + ... + nums[i]

# Query becomes O(1)
def query(l, r):
    return prefix[r] - prefix[l-1]

# But update now breaks the entire prefix array → O(n) to rebuild
```

Query is fast but update is slow. You've just shifted the problem.

**The fundamental tension:**

```
Naive array   → Update O(1),  Query O(n)
Prefix sum    → Update O(n),  Query O(1)
Segment tree  → Update O(log n), Query O(log n)  ← best of both worlds
```

Segment tree is the data structure that balances both operations at O(log n). That's its entire reason for existing.

---

## The core idea — divide the array into segments

Take `nums = [2, 4, 3, 1, 6, 7, 2, 5]` (8 elements, indices 0–7).

A segment tree **precomputes sums for every contiguous segment** in a hierarchical tree structure:

```
Level 0 (root):     [0──7]  sum=30         covers entire array
                   /              \
Level 1:      [0──3] sum=10    [4──7] sum=20
              /       \         /        \
Level 2:  [0─1]=6  [2─3]=4  [4─5]=13  [6─7]=7
           / \      / \       / \       / \
Level 3: [0]=2 [1]=4 [2]=3 [3]=1 [4]=6 [5]=7 [6]=2 [7]=5
```

Every node stores the **sum of its segment**. Leaf nodes are individual elements. Each internal node = sum of its two children.

Two things to notice immediately:

1. The tree has **exactly `2n - 1` nodes** for an array of size `n`
2. The depth is **O(log n)** — same as any balanced binary tree

---

## How it's stored — array representation

Just like a heap, segment trees are stored in a **flat array** using index math. No actual tree nodes or pointers needed.

```
For a node at index i:
  Left child  → 2*i
  Right child → 2*i + 1
  Parent      → i // 2
```

Root is at index **1** (not 0 — makes the math cleaner).

For `nums` of size `n`, the segment tree array needs size `4*n` to be safe (handles non-power-of-2 sizes).

```python
nums = [2, 4, 3, 1, 6, 7, 2, 5]
tree = [0] * (4 * 8)   # 32 slots, most will be used

# After building:
tree[1]  = 30   # root: sum of [0..7]
tree[2]  = 10   # sum of [0..3]
tree[3]  = 20   # sum of [4..7]
tree[4]  = 6    # sum of [0..1]
tree[5]  = 4    # sum of [2..3]
tree[6]  = 13   # sum of [4..5]
tree[7]  = 7    # sum of [6..7]
tree[8]  = 2    # nums[0]
tree[9]  = 4    # nums[1]
tree[10] = 3    # nums[2]
tree[11] = 1    # nums[3]
tree[12] = 6    # nums[4]
tree[13] = 7    # nums[5]
tree[14] = 2    # nums[6]
tree[15] = 5    # nums[7]
```

---

## Stage 1 — Build

The build function fills this tree recursively. Same IBH model you know from DP:

```
1. What does build(node, start, end) do?
   → Fills tree[node] with the sum of nums[start..end]

2. Base case?
   → start == end (leaf node) → tree[node] = nums[start]

3. Recursive step?
   → Split the segment in half
   → Build left child, build right child
   → tree[node] = tree[left] + tree[right]
```

```python
def build(node, start, end):
    if start == end:
        # Leaf node — store the element directly
        tree[node] = nums[start]
        return

    mid = (start + end) // 2

    # Build left and right subtrees
    build(2 * node, start, mid)           # left child
    build(2 * node + 1, mid + 1, end)     # right child

    # Internal node = sum of children
    tree[node] = tree[2 * node] + tree[2 * node + 1]

# Call it: start building from root (node=1) covering full array
build(1, 0, n - 1)
```

Trace for `nums = [2, 4, 3, 1]` (smaller for clarity):

```
build(1, 0, 3)
├── build(2, 0, 1)
│   ├── build(4, 0, 0) → tree[4] = nums[0] = 2  ← leaf
│   └── build(5, 1, 1) → tree[5] = nums[1] = 4  ← leaf
│   tree[2] = tree[4] + tree[5] = 6
└── build(3, 2, 3)
    ├── build(6, 2, 2) → tree[6] = nums[2] = 3  ← leaf
    └── build(7, 3, 3) → tree[7] = nums[3] = 1  ← leaf
    tree[3] = tree[6] + tree[7] = 4
tree[1] = tree[2] + tree[3] = 10
```

**Time: O(n)** — every element visited exactly once.

---

Before moving to Query and Update, one check:

**What does `build(2*node, start, mid)` and `build(2*node+1, mid+1, end)` actually mean geometrically?**

If the current node covers segment `[0..3]` and `mid = 1`:

- Left child covers `[0..1]`
- Right child covers `[2..3]`

The segment is split exactly in half at every level. That's what gives the tree its O(log n) depth.

---

**Small question before Query:**

In the build trace above for `nums = [2, 4, 3, 1]`, what will `tree[1]`, `tree[2]`, `tree[3]` be? You can read the trace — just tell me the three values.

Exactly. All three correct.

```
tree[1] = 10  (sum of [2,4,3,1])
tree[2] = 6   (sum of [2,4])
tree[3] = 4   (sum of [3,1])
```

Build is clear. Let's move to Query.

---

## Stage 2 — Query

This is where the O(log n) magic happens. Given a range `[l, r]`, find the sum.

The key idea — at each node, one of three situations occurs:

```
Case 1 — Complete overlap
  The node's segment is FULLY inside [l, r]
  → return tree[node] directly, no need to go deeper

Case 2 — No overlap
  The node's segment is COMPLETELY outside [l, r]
  → return 0, nothing to add

Case 3 — Partial overlap
  The node's segment PARTIALLY intersects [l, r]
  → split: query left child + query right child
```

Visualized on `nums = [2, 4, 3, 1, 6, 7, 2, 5]`, query `[2, 6]`:

```
Root [0──7]: partial overlap → go deeper
  ├── [0──3]: partial overlap → go deeper
  │     ├── [0──1]: NO overlap → return 0
  │     └── [2──3]: COMPLETE overlap → return 4 ✓
  └── [4──7]: partial overlap → go deeper
        ├── [4──5]: COMPLETE overlap → return 13 ✓
        └── [6──7]: partial overlap → go deeper
              ├── [6──6]: COMPLETE overlap → return 2 ✓
              └── [7──7]: NO overlap → return 0

Answer = 0 + 4 + 13 + 2 + 0 = 19  ✓
(nums[2]+nums[3]+nums[4]+nums[5]+nums[6] = 3+1+6+7+2 = 19)
```

Only **6 nodes visited** instead of 5 elements — and for large arrays the savings are massive.

---

### The 3 questions for query

```
1. What does query(node, start, end, l, r) return?
   → Sum of nums[l..r] by looking at the segment [start..end]
     stored at tree[node]

2. Base cases?
   → No overlap:       return 0
   → Full overlap:     return tree[node]

3. Recursive step?
   → Partial overlap: split at mid
   → return query(left child) + query(right child)
```

How to detect each case:

```python
# No overlap: node's segment is completely outside [l, r]
if end < l or start > r:
    return 0

# Full overlap: node's segment is completely inside [l, r]
if l <= start and end <= r:
    return tree[node]

# Partial overlap: everything else → split
```

```python
def query(node, start, end, l, r):
    # Case 1: no overlap
    if end < l or start > r:
        return 0

    # Case 2: complete overlap
    if l <= start and end <= r:
        return tree[node]

    # Case 3: partial overlap → recurse
    mid = (start + end) // 2
    left_sum  = query(2 * node,     start,   mid, l, r)
    right_sum = query(2 * node + 1, mid + 1, end, l, r)

    return left_sum + right_sum

# Call: query from root covering full array
query(1, 0, n - 1, l, r)
```

**Time: O(log n)** — at each level you visit at most 4 nodes. Proven fact, trust it for now.

---

### Dry run — `nums = [2, 4, 3, 1]`, query `[1, 3]`

Expected answer: `4 + 3 + 1 = 8`

```
query(1, 0, 3, 1, 3)
  partial overlap → split at mid=1

  query(2, 0, 1, 1, 3)
    partial overlap → split at mid=0

    query(4, 0, 0, 1, 3)
      end=0 < l=1 → NO overlap → return 0

    query(5, 1, 1, 1, 3)
      l=1 <= start=1 and end=1 <= r=3 → FULL overlap → return tree[5]=4

    return 0 + 4 = 4

  query(3, 2, 3, 1, 3)
    l=1 <= start=2 and end=3 <= r=3 → FULL overlap → return tree[3]=4

  return 4 + 4 = 8  ✓
```

---

## Stage 3 — Update

Update is simpler than query. When `nums[i]` changes to a new value:

```
1. Walk DOWN the tree from root to the leaf at index i
2. Update the leaf
3. On the way BACK UP, recompute each internal node
   (same as build: tree[node] = tree[left] + tree[right])
```

The 3 questions:

```
1. What does update(node, start, end, i, val) do?
   → Updates nums[i] to val and fixes all affected tree nodes

2. Base case?
   → start == end (reached the leaf) → tree[node] = val

3. Recursive step?
   → Figure out if index i is in left or right half
   → Recurse into that child
   → Recompute tree[node] from both children on the way back up
```

```python
def update(node, start, end, i, val):
    # Base case: reached the leaf
    if start == end:
        tree[node] = val
        nums[i] = val      # keep original array in sync
        return

    mid = (start + end) // 2

    if i <= mid:
        update(2 * node, start, mid, i, val)        # i is in left half
    else:
        update(2 * node + 1, mid + 1, end, i, val)  # i is in right half

    # Recompute this node from updated children
    tree[node] = tree[2 * node] + tree[2 * node + 1]

# Call: update from root
update(1, 0, n - 1, i, val)
```

Trace for `nums = [2, 4, 3, 1]`, update index 1 to value 10:

```
update(1, 0, 3, 1, 10)
  mid=1, i=1 <= mid → go left
  update(2, 0, 1, 1, 10)
    mid=0, i=1 > mid → go right
    update(5, 1, 1, 1, 10)
      start==end → tree[5] = 10  ← leaf updated
    tree[2] = tree[4] + tree[5] = 2 + 10 = 12  ← recomputed
  tree[1] = tree[2] + tree[3] = 12 + 4 = 16    ← recomputed

Before: tree = [_, 10, 6, 4, 2, 4, 3, 1]
After:  tree = [_, 16, 12, 4, 2, 10, 3, 1]  ✓
```

Only **3 nodes updated** out of 7 total — O(log n). ✓

---

## Complete implementation

```python
class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums
        self.tree = [0] * (4 * self.n)
        self.build(1, 0, self.n - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.nums[start]
            return
        mid = (start + end) // 2
        self.build(2 * node, start, mid)
        self.build(2 * node + 1, mid + 1, end)
        self.tree[node] = self.tree[2*node] + self.tree[2*node+1]

    def query(self, node, start, end, l, r):
        if end < l or start > r:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        left  = self.query(2*node,   start,   mid, l, r)
        right = self.query(2*node+1, mid+1,   end, l, r)
        return left + right

    def update(self, node, start, end, i, val):
        if start == end:
            self.tree[node] = val
            self.nums[i] = val
            return
        mid = (start + end) // 2
        if i <= mid:
            self.update(2*node,   start, mid,   i, val)
        else:
            self.update(2*node+1, mid+1, end,   i, val)
        self.tree[node] = self.tree[2*node] + self.tree[2*node+1]

    # Clean public interface — caller doesn't need to know internals
    def range_sum(self, l, r):
        return self.query(1, 0, self.n-1, l, r)

    def point_update(self, i, val):
        self.update(1, 0, self.n-1, i, val)


# Usage
nums = [2, 4, 3, 1, 6, 7, 2, 5]
st = SegmentTree(nums)

print(st.range_sum(2, 6))    # 3+1+6+7+2 = 19
st.point_update(3, 10)       # nums[3]: 1 → 10
print(st.range_sum(2, 6))    # 3+10+6+7+2 = 28
```

---

## Complexity summary

|Operation|Time|Space|
|---|---|---|
|Build|O(n)|O(n)|
|Query|O(log n)|O(log n) call stack|
|Update|O(log n)|O(log n) call stack|

---

**One question before we go to practice problems:**

In the update function, after recursing into the correct child, we recompute:

```python
self.tree[node] = self.tree[2*node] + self.tree[2*node+1]
```

Why do we use **both** children here even though only **one** of them was updated?