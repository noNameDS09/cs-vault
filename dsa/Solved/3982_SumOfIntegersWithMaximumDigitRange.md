---
tags:
  - array
  - math
---

# [3982. Sum of Integers with Maximum Digit Range](https://leetcode.com/problems/sum-of-integers-with-maximum-digit-range/)

## Problem Statement

You are given an integer array `nums`.

The **digit range** of an integer is defined as the difference between its **largest digit** and **smallest digit**.

For example:

```text
5724 → largest digit = 7
        smallest digit = 2
        digit range = 7 - 2 = 5
```

Return the **sum of all integers** in `nums` whose digit range is equal to the **maximum digit range** among all integers in the array.

---

## Examples

### Example 1

**Input**

```text
nums = [5724,111,350]
```

**Output**

```text
6074
```

**Explanation**

| i | nums[i] | Largest Digit | Smallest Digit | Digit Range |
|---|---------|---------------|----------------|-------------|
| 0 | 5724 | 7 | 2 | 5 |
| 1 | 111 | 1 | 1 | 0 |
| 2 | 350 | 5 | 0 | 5 |

```text
The maximum digit range is 5.

The integers with this digit range are:
5724 and 350

Sum = 5724 + 350 = 6074
```

---

### Example 2

**Input**

```text
nums = [90,900]
```

**Output**

```text
990
```

**Explanation**

| i | nums[i] | Largest Digit | Smallest Digit | Digit Range |
|---|---------|---------------|----------------|-------------|
| 0 | 90 | 9 | 0 | 9 |
| 1 | 900 | 9 | 0 | 9 |

```text
The maximum digit range is 9.

Both integers have this digit range.

Sum = 90 + 900 = 990
```

---

## Constraints

```text
1 <= nums.length <= 100
10 <= nums[i] <= 10^5
```

## Code

```python
class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        d = float('-inf')
        ans = []

        def digit(num):
            num = list(str(num))
            num = [int(i) for i in num]
            mx = max(num)
            mn = min(num)
            print(mx-mn)
            return mx-mn

        for n in nums:
            result = digit(n)
            if result > d:
                ans.clear()
                d = result
                ans.append(n)
            elif result == d:
                ans.append(n)
        print(ans)
        return sum(ans)
```