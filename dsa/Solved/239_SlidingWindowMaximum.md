---
tags:
  - array
  - queue
  - sliding-window
  - monotonic-queue
---

# 239. Sliding Window Maximum

## Problem Statement

You are given an array of integers `nums` and an integer `k`.

There is a sliding window of size `k` that moves from the leftmost part of the array to the rightmost part. You can only see the `k` elements inside the current window.

Each time the sliding window moves one position to the right, return the maximum value in the current window.

Return an array containing the maximum value for each sliding window.

---

## Examples

### Example 1

Input

```text
nums = [1,3,-1,-3,5,3,6,7]
k = 3
```

Output

```text
[3,3,5,5,6,7]
```

Explanation

```text
Window Position              Maximum
---------------             -------
[1  3  -1] -3  5  3  6  7      3
 1 [3  -1  -3] 5  3  6  7      3
 1  3 [-1  -3  5] 3  6  7      5
 1  3  -1 [-3  5  3] 6  7      5
 1  3  -1  -3 [5  3  6] 7      6
 1  3  -1  -3  5 [3  6  7]     7
```

---

### Example 2

Input

```text
nums = [1]
k = 1
```

Output

```text
[1]
```

---

## Constraints

```text
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
```


# Sliding Window Maximum (CodeStoryWithMik Style Explanation)

## Intuition

The brute-force approach is to look at every window of size `k` and find its maximum.

- Each window takes `O(k)` time.
- There are approximately `n` windows.

Time Complexity: `O(n × k)`

This is too slow for `n = 10^5`.

---

# Optimized Approach - Monotonic Deque (Decreasing)

The idea is to maintain a deque (double-ended queue) that stores the indices of useful elements.

The deque follows these properties:

1. The front always contains the index of the maximum element for the current window.
2. Elements are stored in decreasing order of their values.
3. We remove:
   - Elements that are outside the current window.
   - Elements smaller than the current element because they can never become the maximum in future windows.

Since every element is inserted and removed at most once, the algorithm runs in O(n) time.

---

# Code

```python
from collections import deque

class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:

        dq = deque()
        n = len(arr)
        ans = []

        for i in range(n):

            # Step 1: Remove indices that are outside the current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Step 2: Remove all smaller elements from the back
            while dq and arr[i] > arr[dq[-1]]:
                dq.pop()

            # Step 3: Insert current index
            dq.append(i)

            # Step 4: Window of size k is formed
            if i >= k - 1:
                ans.append(arr[dq[0]])

        return ans
```
