---
tags:
  - array
  - math
---

# 66. Plus One

## Problem Statement

You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the `i`th digit of the integer.

The digits are ordered from **most significant** to **least significant** (left to right), and the integer does **not** contain any leading zeros.

Increment the integer by **one** and return the resulting array of digits.

---

## Examples

### Example 1

**Input**

```text
digits = [1,2,3]
```

**Output**

```text
[1,2,4]
```

**Explanation**

```text
The array represents the integer 123.

123 + 1 = 124

The resulting array is [1,2,4].
```

---

### Example 2

**Input**

```text
digits = [4,3,2,1]
```

**Output**

```text
[4,3,2,2]
```

**Explanation**

```text
The array represents the integer 4321.

4321 + 1 = 4322

The resulting array is [4,3,2,2].
```

---

### Example 3

**Input**

```text
digits = [9]
```

**Output**

```text
[1,0]
```

**Explanation**

```text
The array represents the integer 9.

9 + 1 = 10

The resulting array is [1,0].
```

---

## Constraints

```text
1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading zeros.
```

## Code

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = 1
        i = 1
        for d in digits[::-1]:
            n += d*i
            i *= 10
        
        # print(n)
        ans = []
        while n > 0:
            ans.append(n%10)
            n = n // 10


        return ans[::-1]
```