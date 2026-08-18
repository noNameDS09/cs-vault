---
tags:
  - array
  - two-pointers
  - binary-search
---

# 167. Two Sum II - Input Array Is Sorted

# Two Sum II - Input Array Is Sorted

## Problem Statement

Given a **1-indexed** array of integers `numbers` that is already sorted in **non-decreasing order**, find two numbers such that they add up to a specific `target`.

Let these two numbers be:

- `numbers[index1]`
- `numbers[index2]`

where:

- `1 <= index1 < index2 <= numbers.length`

Return the indices as an integer array:

```text
[index1, index2]
```

### Notes

- The input array is **sorted**.
- There is **exactly one solution**.
- You **cannot use the same element twice**.
- Your solution must use **only constant extra space (O(1))**.

---

## Examples

### Example 1

**Input**

```text
numbers = [2,7,11,15]
target = 9
```

**Output**

```text
[1,2]
```

**Explanation**

```text
2 + 7 = 9
```

---

### Example 2

**Input**

```text
numbers = [2,3,4]
target = 6
```

**Output**

```text
[1,3]
```

**Explanation**

```text
2 + 4 = 6
```

---

### Example 3

**Input**

```text
numbers = [-1,0]
target = -1
```

**Output**

```text
[1,2]
```

**Explanation**

```text
-1 + 0 = -1
```

---

## Constraints

```text
2 <= numbers.length <= 3 * 10^4
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
There is exactly one valid solution.
```

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l, r = 0, n-1

        while l<r:
            if nums[l] + nums[r] == target:
                return [l+1, r+1]
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1
        
        return []
```