---
tags:
  - array
  - hash-table
  - binary-search
---

# [3471. Find the Largest Almost Missing Integer](https://leetcode.com/problems/find-the-largest-almost-missing-integer/)

You are given an integer array `nums` and an integer `k`.

An integer `x` is **almost missing** from `nums` if `x` appears in _exactly_ one subarray of size `k` within `nums`.

Return the **largest** **almost missing** integer from `nums`. If no such integer exists, return `-1`.

A **subarray** is a contiguous sequence of elements within an array.

**Example 1:**

**Input:** nums = [3,9,2,1,7], k = 3

**Output:** 7

**Explanation:**

- 1 appears in 2 subarrays of size 3: `[9, 2, 1]` and `[2, 1, 7]`.
- 2 appears in 3 subarrays of size 3: `[3, 9, 2]`, `[9, 2, 1]`, `[2, 1, 7]`.
- 3 appears in 1 subarray of size 3: `[3, 9, 2]`.
- 7 appears in 1 subarray of size 3: `[2, 1, 7]`.
- 9 appears in 2 subarrays of size 3: `[3, 9, 2]`, and `[9, 2, 1]`.

We return 7 since it is the largest integer that appears in exactly one subarray of size `k`.

**Example 2:**

**Input:** nums = [3,9,7,2,1,7], k = 4

**Output:** 3

**Explanation:**

- 1 appears in 2 subarrays of size 4: `[9, 7, 2, 1]`, `[7, 2, 1, 7]`.
- 2 appears in 3 subarrays of size 4: `[3, 9, 7, 2]`, `[9, 7, 2, 1]`, `[7, 2, 1, 7]`.
- 3 appears in 1 subarray of size 4: `[3, 9, 7, 2]`.
- 7 appears in 3 subarrays of size 4: `[3, 9, 7, 2]`, `[9, 7, 2, 1]`, `[7, 2, 1, 7]`.
- 9 appears in 2 subarrays of size 4: `[3, 9, 7, 2]`, `[9, 7, 2, 1]`.

We return 3 since it is the largest and only integer that appears in exactly one subarray of size `k`.

**Example 3:**

**Input:** nums = [0,0], k = 1

**Output:** -1

**Explanation:**

There is no integer that appears in only one subarray of size 1.

**Constraints:**

- `1 <= nums.length <= 50`
- `0 <= nums[i] <= 50`
- `1 <= k <= nums.length`


## Code

```python
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        
        n = len(nums)
        if n == k: return max(nums)
        
        for i in range(n-k + 1):
            temp = nums[i:i+k]
            # print(temp)
            for val in temp:
                freq[val] += 1
        # print(freq)
        
        ans = -1
        
        for val, f in freq.items():
            if f == 1:
                ans = max(ans, val)
        
        return ans
```

```python
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        # Dictionary to store the frequency of each number
        # across all subarrays of size k.
        freq = defaultdict(int)

        n = len(nums)

        # If k == n, there is only one subarray (the entire array).
        # Therefore, the largest integer in nums is the answer.
        if n == k:
            return max(nums)

        # Generate every possible subarray of size k.
        for i in range(n - k + 1):

            # Extract the current subarray of length k.
            temp = nums[i:i + k]

            # Count the occurrence of every element in this subarray.
            for val in temp:
                freq[val] += 1

        ans = -1

        # We need the largest number that appears exactly once
        # across all the k-sized subarrays.
        for val, f in freq.items():
            if f == 1:
                ans = max(ans, val)

        return ans
```