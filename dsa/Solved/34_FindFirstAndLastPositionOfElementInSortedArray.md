# 34. Find First and Last Position of Element in Sorted Array

## Problem Statement

Given an array of integers `nums` sorted in **non-decreasing order** and an integer `target`, find the **starting** and **ending** positions of `target` in the array.

If `target` is not present in the array, return:

```text
[-1, -1]
```

Your algorithm must run in **O(log n)** time.

---

## Examples

### Example 1

**Input**

```text
nums = [5,7,7,8,8,10]
target = 8
```

**Output**

```text
[3,4]
```

---

### Example 2

**Input**

```text
nums = [5,7,7,8,8,10]
target = 6
```

**Output**

```text
[-1,-1]
```

---

### Example 3

**Input**

```text
nums = []
target = 0
```

**Output**

```text
[-1,-1]
```

---

## Constraints

```text
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is sorted in non-decreasing order.
-10^9 <= target <= 10^9
```

```python
class Solution:
    '''
    Use the binary search
    1. find the leftmost index
    2. find the rightmost index
    return [left, right]
    '''

    def findLeft(self, arr, target):
        '''
        function to find leftmost index of the target
        '''
        n = len(arr)
        l, r = 0, n-1
        ans = -1
        while l <= r:
            mid = l + (r-l) // 2
            if arr[mid] == target:
                ans = mid
                r = mid - 1 # Keep in mind this condition
                
            elif arr[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return ans
    
    def findRight(self, arr, target):
        '''
        function to find the rightmost index of the target
        '''
        n = len(arr)
        l, r = 0, n-1
        ans = -1
        while l <= r:
            mid = l + (r-l) // 2
            if arr[mid] == target:
                ans = mid
                l = mid + 1 # just changed this condition
                
            elif arr[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return ans

    def find(self, arr, target, left=False):
        '''
        Both the above functions can be implemented in one single function using the left:Boolean parameter
        If we want to get leftmost index set left=True other wise left=False
        '''
        n = len(arr)
        l, r = 0, n-1
        ans = -1
        while l <= r:
            mid = l + (r-l) // 2
            if arr[mid] == target:
                ans = mid
                if left:
                    r = mid - 1
                else:
                    l = mid + 1
                    # ans = mid
            elif arr[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return ans
            
    def searchRange(self, arr: List[int], target: int) -> List[int]:
        left, right = -1, -1

        left = self.find(arr, target, True)
        right = self.find(arr, target, False)

        return [left, right]
```