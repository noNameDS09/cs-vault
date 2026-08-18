---
tags:
  - array
  - two-pointers
---

# 2078. Two Furthest Houses With Different Colors

## Problem Statement

There are `n` houses evenly lined up on a street, and each house is painted with a color.

You are given a **0-indexed** integer array `colors` of length `n`, where `colors[i]` represents the color of the `i`th house.

Return the **maximum distance** between any two houses that have **different colors**.

The distance between the `i`th and `j`th houses is defined as:

```text
abs(i - j)
```

where `abs(x)` is the absolute value of `x`.

---

## Examples

### Example 1

**Input**

```text
colors = [1,1,1,6,1,1,1]
```

**Output**

```text
3
```

**Explanation**

```text
The furthest two houses with different colors are house 0 and house 3.

House 0 has color 1.
House 3 has color 6.

Distance = |0 - 3| = 3.

House 3 and house 6 also produce the same maximum distance.
```

---

### Example 2

**Input**

```text
colors = [1,8,3,8,3]
```

**Output**

```text
4
```

**Explanation**

```text
The furthest two houses with different colors are house 0 and house 4.

House 0 has color 1.
House 4 has color 3.

Distance = |0 - 4| = 4.
```

---

### Example 3

**Input**

```text
colors = [0,1]
```

**Output**

```text
1
```

**Explanation**

```text
The two houses have different colors.

Distance = |0 - 1| = 1.
```

---

## Constraints

```text
n == colors.length
2 <= n <= 100
0 <= colors[i] <= 100
At least two houses have different colors.
```

## Code

```python
class Solution:
    def maxDistance(self, arr: List[int]) -> int:
	    '''
	    Make pair for every i and j and compute the answer
	    '''
        n = len(arr)
        ans = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if arr[i] != arr[j]:
                    ans = max(ans, abs(j-i))
        
        return ans
```