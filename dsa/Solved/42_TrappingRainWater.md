# 42. Trapping Rain Water

## Problem Statement

Given `n` non-negative integers representing an elevation map, where the width of each bar is `1`, compute how much rainwater can be trapped after raining.

---

## Examples

### Example 1

**Input**

```text
height = [0,1,0,2,1,0,1,3,2,1,2,1]
```

**Output**

```text
6
```

**Explanation**

```text
The elevation map represented by the array traps a total of 6 units of rainwater.
```

---

### Example 2

**Input**

```text
height = [4,2,0,3,2,5]
```

**Output**

```text
9
```

**Explanation**

```text
The elevation map represented by the array traps a total of 9 units of rainwater.
```

---

## Constraints

```text
n == height.length
1 <= n <= 2 × 10^4
0 <= height[i] <= 10^5
```

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = [0] * n, [0] * n
        left[0], right[-1] = height[0], height[-1]
        
        for i in range(1, n):
            left[i] = max(left[i-1], height[i])
        
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])

        ans = 0
        for i in range(1, n-1):
            ans += min(left[i], right[i]) - height[i]
        
        return ans
```