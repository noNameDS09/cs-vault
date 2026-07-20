# 33. Search in Rotated Sorted Array

## Problem Statement

There is an integer array `nums` sorted in ascending order with **distinct** values.

Before being passed to your function, `nums` may have been rotated at an unknown index `k` (`1 <= k < nums.length`) such that the array becomes:

```text
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
```

For example:

```text
[0,1,2,4,5,6,7]
```

might become:

```text
[4,5,6,7,0,1,2]
```

after being rotated by 3 positions.

Given the rotated array `nums` and an integer `target`, return the **index** of `target` if it exists in the array. Otherwise, return `-1`.

Your algorithm must run in **O(log n)** time.

---

## Examples

### Example 1

**Input**

```text
nums = [4,5,6,7,0,1,2]
target = 0
```

**Output**

```text
4
```

---

### Example 2

**Input**

```text
nums = [4,5,6,7,0,1,2]
target = 3
```

**Output**

```text
-1
```

---

### Example 3

**Input**

```text
nums = [1]
target = 0
```

**Output**

```text
-1
```

---

## Constraints

```text
1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values in nums are unique.
nums is an ascending array that is possibly rotated.
-10^4 <= target <= 10^4
```

```python
class Solution:

    def findPivot(self, nums, n):
        l, r = 0, n-1

        while l < r:
            mid = l + (r-l)//2
            
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
        return r
    
    def bs(self, l, r, nums, target):
        while l<=r:
            mid = l + (r-l)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        
        return -1

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        pivot = self.findPivot(nums, n)

        idx = self.bs(0, pivot-1, nums, target)
        if idx != -1:
            return idx
        
        return self.bs(pivot, n-1, nums, target)
```