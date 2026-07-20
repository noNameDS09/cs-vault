# 704. Binary Search

## Problem Statement

Given a sorted array of integers `nums` (sorted in **ascending order**) and an integer `target`, return the index of `target` if it exists in the array. Otherwise, return `-1`.

Your algorithm must have a time complexity of **O(log n)**.

---

## Examples

### Example 1

**Input**

```text
nums = [-1,0,3,5,9,12]
target = 9
```

**Output**

```text
4
```

**Explanation**

```text
9 exists in nums, and its index is 4.
```

---

### Example 2

**Input**

```text
nums = [-1,0,3,5,9,12]
target = 2
```

**Output**

```text
-1
```

**Explanation**

```text
2 does not exist in nums, so return -1.
```

---

## Constraints

```text
1 <= nums.length <= 10^4
-10^4 < nums[i], target < 10^4
All the integers in nums are unique.
nums is sorted in ascending order.
```

## Solution
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1

        while(l <= r):
            idx = (l + r) // 2

            if nums[idx] == target:
                return idx
            elif nums[idx] > target:
                r = idx-1
            else:
                l = idx + 1
        
        return -1
```