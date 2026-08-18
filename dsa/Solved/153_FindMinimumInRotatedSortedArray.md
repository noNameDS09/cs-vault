---
tags:
  - array
  - binary-search
---

# 153. Find Minimum in Rotated Sorted Array

## Problem Statement

Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times.

For example, the array:

```text
[0,1,2,4,5,6,7]
```

might become:

```text
[4,5,6,7,0,1,2]
```

if it was rotated 4 times, or:

```text
[0,1,2,4,5,6,7]
```

if it was rotated 7 times.

> Rotating an array by 1 position moves the last element to the front.

Given the rotated sorted array `nums` containing **unique** elements, return the **minimum element** in the array.

Your algorithm must run in **O(log n)** time.

---

## Examples

### Example 1

**Input**

```text
nums = [3,4,5,1,2]
```

**Output**

```text
1
```

**Explanation**

```text
The original array was [1,2,3,4,5], rotated 3 times.
```

---

### Example 2

**Input**

```text
nums = [4,5,6,7,0,1,2]
```

**Output**

```text
0
```

**Explanation**

```text
The original array was [0,1,2,4,5,6,7], rotated 4 times.
```

---

### Example 3

**Input**

```text
nums = [11,13,15,17]
```

**Output**

```text
11
```

**Explanation**

```text
The original array was [11,13,15,17], rotated 4 times.
```

---

## Constraints

```text
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers in nums are unique.
nums is sorted in ascending order and rotated between 1 and n times.
```

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1

        while l < r:
            mid = l + (r-l)//2

            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
            
        return nums[l]
```