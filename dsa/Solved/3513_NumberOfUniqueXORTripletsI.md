# 3513. Number of Unique XOR Triplets I

## Problem Statement

You are given an integer array `nums` of length `n`, where `nums` is a **permutation** of the integers in the range:

```text
[1, n]
```

A **XOR triplet** is defined as:

```text
nums[i] XOR nums[j] XOR nums[k]
```

where:

```text
i <= j <= k
```

Return the **number of unique XOR values** that can be obtained from all possible triplets.

---

## Examples

### Example 1

**Input**

```text
nums = [1,2]
```

**Output**

```text
2
```

**Explanation**

The possible XOR triplets are:

```text
(0,0,0) → 1 XOR 1 XOR 1 = 1
(0,0,1) → 1 XOR 1 XOR 2 = 2
(0,1,1) → 1 XOR 2 XOR 2 = 1
(1,1,1) → 2 XOR 2 XOR 2 = 2
```

The unique XOR values are:

```text
{1, 2}
```

Therefore, the answer is:

```text
2
```

---

### Example 2

**Input**

```text
nums = [3,1,2]
```

**Output**

```text
4
```

**Explanation**

Some possible XOR triplets are:

```text
(0,0,0) → 3 XOR 3 XOR 3 = 3
(0,0,1) → 3 XOR 3 XOR 1 = 1
(0,0,2) → 3 XOR 3 XOR 2 = 2
(0,1,2) → 3 XOR 1 XOR 2 = 0
```

The unique XOR values are:

```text
{0, 1, 2, 3}
```

Therefore, the answer is:

```text
4
```

---

## Constraints

```text
1 <= n == nums.length <= 10^5
nums is a permutation of the integers in the range [1, n].
```

## Code 

```python
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)

        # Handle small cases separately.
        if n <= 2:
            return n

        # For n > 2, the number of distinct XOR values equals
        # the smallest power of two strictly greater than n.
        return 1 << n.bit_length()  # shifting the bits
```
