---
tags:
  - array
  - binary-search
  - matrix
---

# 74. Search a 2D Matrix


# Time -> O(m log(n))
```python
class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        n = len(mat[0])
        for row in mat:
            l, r = 0, n-1
            
            if row[l] <= target and row[r] >= target:
                while l <= r:
                    mid = (l + r) // 2
                    if row[mid] == target:
                        return True
                    elif row[mid] < target:
                        l = mid+1
                    else:
                        r = mid-1
        return False
```

# Time -> O(log(m*n))
```python
class Solution:
    def searchMatrix(self, arr: List[List[int]], target: int) -> bool:
        '''
        Consider the 2D matrix as 1D matrix, then solve
        '''

        m = len(arr)
        n = len(arr[0])

        left, right = 0, (m*n) - 1

        while left <= right:   # Binary search on 2D matrix
            mid = (left + right) // 2  # middle index
            
            row = mid // n # calculate the row of element
            col = mid % n  # calculate the col of element

            if arr[row][col] == target:
                return True
            elif arr[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
```