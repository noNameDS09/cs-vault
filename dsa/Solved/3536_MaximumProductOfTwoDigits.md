---
tags:
  - array
  - math
---

# 3536. Maximum Product of Two Digits

## Problem Statement

You are given a positive integer `n`.

Return the **maximum product** of any two digits in `n`.

> **Note:** You may use the same digit twice only if it appears at least twice in `n`.

---

## Examples

### Example 1

**Input**

```text
n = 31
```

**Output**

```text
3
```

**Explanation**

```text
The digits of n are [3, 1].

The possible products are:
3 × 1 = 3

The maximum product is 3.
```

---

### Example 2

**Input**

```text
n = 22
```

**Output**

```text
4
```

**Explanation**

```text
The digits of n are [2, 2].

The possible products are:
2 × 2 = 4

The maximum product is 4.
```

---

### Example 3

**Input**

```text
n = 124
```

**Output**

```text
8
```

**Explanation**

```text
The digits of n are [1, 2, 4].

The possible products are:
1 × 2 = 2
1 × 4 = 4
2 × 4 = 8

The maximum product is 8.
```

---

## Constraints

```text
10 <= n <= 10^9
```

## Code

```python
class Solution:
    def maxProduct(self, n: int) -> int:
        arr = [int(i) for i in str(n)]
        mx = max(arr)
        arr.remove(mx)
        mn = 0
        for i in arr:
            if i > mn and i <= mx:
                mn = i
        
        return mx*mn
```