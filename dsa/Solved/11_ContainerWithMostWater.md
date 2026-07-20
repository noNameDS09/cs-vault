# 11. Container With Most Water

## Brute Force O(n^2))
```python
class Solution:
    def maxArea(self, arr: List[int]) -> int:
        ans = -1
        n = len(arr)
        for i in range(n):
            for j in range(i+1, n):
                curr = (j-i) * min(arr[i], arr[j])
                # print(curr)
                ans = max(ans, curr)
        
        return ans
```
## Better Approach (two pointers)
```python
class Solution:
    def maxArea(self, arr: List[int]) -> int:
        '''
        left and right pointers for the width and height of container.
        Measure the area (w * h).
        If left wall is shorter move left wall forward (to find taller wall).
        Else move right wall back 
        '''
        left, right = 0, len(arr) - 1
        ans = 0

        while left < right:
            w = right - left
            h = min(arr[left], arr[right])
            area = w * h
            
            ans = max(ans, area)

            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        
        return ans
```