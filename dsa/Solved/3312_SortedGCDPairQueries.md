---
tags:
  - array
  - math
  - number-theory
  - gcd
  - inclusion-exclusion
  - sieve
  - binary-search
  - sorting
  - hash-table
---

# GCD of Pair Queries

## Problem Statement

You are given an integer array `nums` of length `n` and an integer array `queries`.

Construct an array `gcdPairs` by:

1. Computing the **GCD** of every possible pair `(nums[i], nums[j])`, where:

```text
0 <= i < j < n
```

2. Sorting all GCD values in **ascending order**.

For each query `queries[i]`, return the element at index `queries[i]` in the sorted `gcdPairs` array.

Return an integer array `answer`, where:

```text
answer[i] = gcdPairs[queries[i]]
```

> Here, `gcd(a, b)` denotes the greatest common divisor of `a` and `b`.

---

## Examples

### Example 1

**Input**

```text
nums = [2,3,4]
queries = [0,2,2]
```

**Output**

```text
[1,2,2]
```

**Explanation**

```text
gcdPairs =
[
    gcd(2,3),
    gcd(2,4),
    gcd(3,4)
]
=
[1,2,1]
```

After sorting:

```text
gcdPairs = [1,1,2]
```

Therefore:

```text
answer = [1,2,2]
```

---

### Example 2

**Input**

```text
nums = [4,4,2,1]
queries = [5,3,1,0]
```

**Output**

```text
[4,2,1,1]
```

**Explanation**

```text
Sorted gcdPairs = [1,1,1,2,2,4]
```

---

### Example 3

**Input**

```text
nums = [2,2]
queries = [0,0]
```

**Output**

```text
[2,2]
```

**Explanation**

```text
gcdPairs = [2]
```

---

## Constraints

```text
2 <= n == nums.length <= 10^5
1 <= nums[i] <= 5 × 10^4
1 <= queries.length <= 10^5
0 <= queries[i] < n × (n - 1) / 2
```

# Brute Force Solution. Time: O(n^2 log(n))
```python
from math import gcd
class Solution:
    '''
    Do as the question asks (Simulation)
    '''
    def gcdValues(self, arr: List[int], q: List[int]) -> List[int]:
        gcdP = set()
        n = len(arr)
        for i in range(n-1):
            for j in range(i+1, n):
                gcdP.append(gcd(arr[i], arr[j]))
        
        gcdP.sort()

        ans = []
        for i in range(len(q)):
            ans.append(gcdP[q[i]])
        
        return ans
        
```

# Optimal Sol
Let's ignore the code completely and understand the **algorithm**. The trick is to change the way you think about the problem.

## What does the problem ask?

Suppose

```text
A = [2,4,6]
```

All pairs are

| Pair  | GCD |
| ----- | --- |
| (2,4) | 2   |
| (2,6) | 2   |
| (4,6) | 2   |

Sorted GCDs:

```text
[2,2,2]
```

If a query asks for index `1`, answer is `2`.

The brute force solution is:

1. Generate every pair.
2. Compute every gcd.
3. Sort.
4. Answer queries.

This is impossible for `n = 100000`.

So we ask a different question.

---

# New idea

Instead of asking

> "What is the gcd of every pair?"

ask

> "How many pairs have gcd = 1?"
>
> "How many pairs have gcd = 2?"
>
> "How many pairs have gcd = 3?"
>
> ...

If we know these counts, we don't need to build the huge sorted array.

---

## Step 1: Frequency

Example

```text
A = [2,4,6,8]
```

Maximum = 8

Frequency array

```text
Number : 1 2 3 4 5 6 7 8
Freq   : 0 1 0 1 0 1 0 1
```

Meaning

* one 2
* one 4
* one 6
* one 8

---

# Step 2: Count numbers divisible by each i

Let's start with

```text
i = 2
```

Which numbers are divisible by 2?

```text
2
4
6
8
```

Count = 4

There are

```text
4C2 = 6
```

pairs.

These six pairs are

```text
(2,4)
(2,6)
(2,8)
(4,6)
(4,8)
(6,8)
```

Notice something.

Every one of them is divisible by 2.

So

```text
6 pairs are divisible by 2.
```

**But that does NOT mean all of them have gcd exactly 2.**

Some may have gcd 4.

Some may have gcd 8.

---

# Step 3: Why inclusion-exclusion?

Let's compute the actual gcds.

```text
(2,4)=2
(2,6)=2
(2,8)=2
(4,6)=2
(4,8)=4
(6,8)=2
```

So

```text
gcd=2 → 5 pairs
gcd=4 → 1 pair
```

Earlier we counted

```text
pairs divisible by2 = 6
```

Those six are

```text
gcd2
+
gcd4
```

Therefore

```text
exact gcd2

=

pairs divisible by2

-

pairs with gcd4
```

That is exactly why we subtract.

---

# Why do we go backwards?

Suppose we compute

```text
i = 2
```

To find

```text
exact gcd2
```

we need

```text
gcd4
gcd6
gcd8
...
```

These must already be known.

Therefore we compute

```text
8
7
6
5
4
3
2
1
```

from largest to smallest.

---

# Let's do the whole example

Array

```text
2 4 6 8
```

---

## i = 8

Numbers divisible by 8

```text
8
```

Count

```text
1
```

Pairs

```text
0
```

So

```text
exact8=0
```

---

## i = 7

None

```text
exact7=0
```

---

## i = 6

Only 6

```text
exact6=0
```

---

## i = 5

None

```text
0
```

---

## i = 4

Multiples

```text
4
8
```

Count

```text
2
```

Pairs

```text
1
```

Subtract multiples

```text
exact8=0
```

Therefore

```text
exact4=1
```

---

## i = 3

Multiples

```text
3
6
```

Only one number

```text
0 pairs
```

---

## i = 2

Multiples

```text
2
4
6
8
```

Count

```text
4
```

Pairs

```text
6
```

Subtract

```text
exact4=1
exact6=0
exact8=0
```

Therefore

```text
exact2

=

6-1

=

5
```

Correct.

---

## i = 1

Everything is divisible by 1.

Count

```text
4
```

Pairs

```text
6
```

Subtract

```text
exact2=5
exact3=0
exact4=1
...
```

```text
6-5-1=0
```

Exactly right.

---

Final result

```text
gcd1 =0
gcd2 =5
gcd3 =0
gcd4 =1
```

---

# Step 4: Prefix

Imagine writing the sorted GCD array.

```text
2 2 2 2 2 4
```

Instead we store

```text
exact

1→0
2→5
3→0
4→1
```

Prefix becomes

```text
1→0
2→5
3→5
4→6
```

Meaning

```text
Up to gcd2 there are 5 pairs.

Up to gcd4 there are 6 pairs.
```

---

# Step 5: Queries

Suppose query asks

```text
index=4
```

Sorted array

```text
Index

0 1 2 3 4 5

Value

2 2 2 2 2 4
```

Index 4 belongs to gcd2.

Prefix

```text
0
5
5
6
```

The first prefix greater than 4 is

```text
5
```

which is located at

```text
gcd=2
```

Hence answer is

```text
2
```

---

## The entire algorithm in one sentence

Instead of generating every pair, the algorithm:

1. Counts how many numbers are divisible by each possible GCD.
2. Uses those counts to compute how many pairs have **exactly** each GCD via inclusion-exclusion.
3. Builds cumulative counts (prefix sums).
4. Uses binary search to answer which GCD corresponds to the `k`-th pair in sorted order.

The conceptual leap is realizing that **counting pairs by GCD value is much cheaper than enumerating all pairs**. Once you have the count of pairs for each GCD, the queries become a simple prefix-sum and binary-search problem.

```python
from itertools import accumulate 
import bisect
class Solution:
    def gcdValues(self, arr: List[int], Q: List[int]) -> List[int]:
        mx = max(arr)
        freq = [0] * (mx + 1)

        for i in arr:
            freq[i] += 1
        
        GCD = [0] * (mx + 1)

        for i in range(mx, 0, -1):
            sm = sum(freq[i::i])
            GCD[i] = sm * (sm -1 ) // 2 - sum(GCD[i::i])
        
        GCD = list(accumulate(GCD))

        return [bisect.bisect_right(GCD, q) for q in Q]
```