---
tags:
  - array
  - dynamic-programming
  - binary-search
  - segment-tree
---

# [2770. Maximum Number of Jumps to Reach the Last Index](https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/)

## Problem Statement

You are given a **0-indexed** integer array `nums` of length `n` and an integer `target`.

You start at index `0`.

In one jump, you can move from index `i` to any index `j` such that:

```text
0 <= i < j < n
-target <= nums[j] - nums[i] <= target
```

Return the **maximum number of jumps** required to reach index `n - 1`.

If it is **impossible** to reach the last index, return `-1`.

---

## Examples

### Example 1

**Input**

```text
nums = [1,3,6,4,1,2]
target = 2
```

**Output**

```text
3
```

**Explanation**

```text
One optimal sequence of jumps is:

0 → 1
1 → 3
3 → 5

Total jumps = 3.

It can be shown that no valid sequence reaches
the last index using more than 3 jumps.
```

---

### Example 2

**Input**

```text
nums = [1,3,6,4,1,2]
target = 3
```

**Output**

```text
5
```

**Explanation**

```text
One optimal sequence of jumps is:

0 → 1
1 → 2
2 → 3
3 → 4
4 → 5

Total jumps = 5.

It can be shown that this is the maximum possible.
```

---

### Example 3

**Input**

```text
nums = [1,3,6,4,1,2]
target = 0
```

**Output**

```text
-1
```

**Explanation**

```text
There is no valid sequence of jumps that reaches
the last index.
```

---

## Constraints

```text
2 <= nums.length == n <= 1000
-10^9 <= nums[i] <= 10^9
0 <= target <= 2 × 10^9
```

## Code

```python
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        from functools import cache

        n = len(nums)

        @cache
        def solve(i):
            # Base case:
            # If we have reached the last index, no more jumps are needed.
            if i == n - 1:
                return 0

            # Stores the maximum jumps possible from index i.
            # Initialize with -infinity to represent an unreachable state.
            ans = float('-inf')

            # Try jumping to every index ahead of the current index.
            for j in range(i + 1, n):

                # A jump is valid only if the absolute difference
                # between the two values is within the target.
                if abs(nums[j] - nums[i]) <= target:

                    # Make the jump and recursively compute the
                    # maximum jumps from the new index.
                    ans = max(ans, 1 + solve(j))

            # Return the best answer for the current index.
            return ans

        # Compute the answer starting from index 0.
        res = solve(0)

        # If the last index cannot be reached, return -1.
        return -1 if res == float('-inf') else res
```