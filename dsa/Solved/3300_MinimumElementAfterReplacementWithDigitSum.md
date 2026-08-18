---
tags:
  - array
  - math
  - simulation
---

# 3300. Minimum Element After Replacement With Digit Sum

## Problem Statement

You are given an integer array `nums`.

Replace each element in `nums` with the **sum of its digits**.

Return the **minimum element** in `nums` after all replacements.

---

## Examples

### Example 1

**Input**

```text
nums = [10,12,13,14]
```

**Output**

```text
1
```

**Explanation**

```text
10 → 1 + 0 = 1
12 → 1 + 2 = 3
13 → 1 + 3 = 4
14 → 1 + 4 = 5

nums becomes [1,3,4,5].

The minimum element is 1.
```

---

### Example 2

**Input**

```text
nums = [1,2,3,4]
```

**Output**

```text
1
```

**Explanation**

```text
nums becomes [1,2,3,4].

The minimum element is 1.
```

---

### Example 3

**Input**

```text
nums = [999,19,199]
```

**Output**

```text
10
```

**Explanation**

```text
999 → 9 + 9 + 9 = 27
19  → 1 + 9 = 10
199 → 1 + 9 + 9 = 19

nums becomes [27,10,19].

The minimum element is 10.
```

---

## Constraints

```text
1 <= nums.length <= 100
1 <= nums[i] <= 10^4
```

## Code

```python
class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float('inf')
        for n in nums:
            n = str(n)
            s = sum([int(i) for i in n])
            ans = min(ans, s)
        
        return ans
```