---
tags:
  - array
  - bit-manipulation
  - hash-table
---

# 3514. Number of Unique XOR Triplets II

## Problem Statement

You are given an integer array `nums`.

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
nums = [1,3]
```

**Output**

```text
2
```

**Explanation**

The possible XOR triplets are:

```text
(0,0,0) → 1 XOR 1 XOR 1 = 1
(0,0,1) → 1 XOR 1 XOR 3 = 3
(0,1,1) → 1 XOR 3 XOR 3 = 1
(1,1,1) → 3 XOR 3 XOR 3 = 3
```

The unique XOR values are:

```text
{1, 3}
```

Therefore, the answer is:

```text
2
```

---

### Example 2

**Input**

```text
nums = [6,7,8,9]
```

**Output**

```text
4
```

**Explanation**

The unique XOR triplet values are:

```text
{6, 7, 8, 9}
```

Therefore, the answer is:

```text
4
```

---

## Constraints

```text
1 <= nums.length <= 1500
1 <= nums[i] <= 1500
```

## Code 
```python
class Solution:
    def uniqueXorTriplets(self, arr: List[int]) -> int:
        temp = []
        n = len(arr)
        for i in range(n):
            for j in range(i, n):
                temp.append(arr[i] ^ arr[j])
        
        temp = list(set(temp)) # convert to set for unique xor values -> then again to list
        ans = []
        for i in range(n):
            for j in range(len(temp)):
                ans.append(arr[i] ^ temp[j])
        
        ans = set(ans)

        return len(ans)
```