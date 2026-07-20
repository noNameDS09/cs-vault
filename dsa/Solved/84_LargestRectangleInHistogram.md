# 84. Largest Rectangle in Histogram

# Largest Rectangle in Histogram

## Problem Statement

Given an array of integers `heights` representing the heights of bars in a histogram, where the width of each bar is `1`, return the area of the largest rectangle that can be formed within the histogram.

---

## Examples

### Example 1

**Input**

```text
heights = [2,1,5,6,2,3]
```

**Output**

```text
10
```

**Explanation**

```text
The histogram represented by the array has a largest rectangle
with an area of 10 units.
```

---

### Example 2

**Input**

```text
heights = [2,4]
```

**Output**

```text
4
```

**Explanation**

```text
The largest rectangle has an area of 4 units.
```

---

## Constraints

```text
1 <= heights.length <= 10^5
0 <= heights[i] <= 10^4
```

```python
class Solution:

    def NSE(self, arr): # next smallest element
        '''
        Algorithm (Right to Left)
        Traverse the array from right to left.
        Maintain a stack that is strictly increasing (top is the nearest smaller candidate).
        While the stack top is greater than or equal to the current element, pop it.
        If the stack is empty, answer is -1; otherwise, answer is the stack top.
        Push the current element onto the stack.
        '''
        n = len(arr)
        ans = [n] * n
        stack = []

        for i in range(n)[::-1]:

            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if stack:
                ans[i] = stack[-1]
            
            stack.append(i)

        return ans
    
    def PSE(self, arr):  # previous smallest element
        '''
        Traverse from left to right.
        Maintain a monotonic increasing stack.
        While the top of the stack is greater than or equal to the current element, pop it.
        The top of the stack (if it exists) is the previous smaller element.
        Push the current element onto the stack.
        '''
        n = len(arr)
        ans, stack = [-1] * n, []

        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]
            stack.append(i)
        
        return ans

    def largestRectangleArea(self, arr: List[int]) -> int:
        nse = self.NSE(arr)
        pse = self.PSE(arr)
        n = len(arr)
        ans = 0
        for i in range(n):
            width = nse[i] - pse[i] - 1
            ans = max(ans, width * arr[i])
        
        return ans
```