---
tags:
  - array
  - stack
  - monotonic-stack
---

# 739. Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, return an array answer such that ```answer[i]``` is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep ```answer[i] == 0``` instead.

```
Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```
```
Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```
```
Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100

## Brute Force : Time -> O(n^2), Space -> O(1)
```python
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        ans = [0] * n

        for i in range(n):
            for j in range(i+1, n):
                if temp[i] < temp[j]:
                    ans[i] = j - i
                    break

        return ans
```

## Better - Monotonic Stack. Time -> O(n*2), Space -> O(n)
```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(n-1, -1, -1): # traverse from end

            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            
            if not stack:
                result[i] = 0
            else:
                result[i] = stack[-1] - i

            stack.append(i)
        
        return result
```