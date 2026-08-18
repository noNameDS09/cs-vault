---
tags:
  - array
  - bit-manipulation
  - dynamic-programming
---

# [3702. Longest Subsequence With Non-Zero Bitwise XOR](https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/)

You are given an integer array `nums`.

Return the length of the **longest subsequence** in `nums` whose bitwise **XOR** is **non-zero**. If no such **subsequence** exists, return 0.

**Example 1:**

**Input:** nums = [1,2,3]

**Output:** 2

**Explanation:**

One longest subsequence is `[2, 3]`. The bitwise XOR is computed as `2 XOR 3 = 1`, which is non-zero.

**Example 2:**

**Input:** nums = [2,3,4]

**Output:** 3

**Explanation:**

The longest subsequence is `[2, 3, 4]`. The bitwise XOR is computed as `2 XOR 3 XOR 4 = 5`, which is non-zero.

**Constraints:**

- `1 <= nums.length <= 105`
- `0 <= nums[i] <= 109`

## Code

```python
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        from functools import reduce
        from operator import xor
        if sum(nums) == 0: return 0
        n = len(nums)
        return n-1 if reduce(xor, nums) == 0 else n

# Equivalent to following

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        from functools import reduce
        from operator import xor
        
        if sum(nums) == 0: return 0
        
        ans = reduce(xor, nums)
        
        if ans == 0:
            return len(nums) - 1
        
        return len(nums)

```