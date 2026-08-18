---
tags:
  - array
  - dynamic-programming
  - game-theory
  - interval-dp
---

# [1563. Stone Game V](https://leetcode.com/problems/stone-game-v/)

There are several stones **arranged in a row**, and each stone has an associated value which is an integer given in the array `stoneValue`.

In each round of the game, Alice divides the row into **two non-empty rows** (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.

The game ends when there is only **one stone remaining**. Alice's score is initially **zero**.

Return _the maximum score that Alice can obtain_.

**Example 1:**

**Input:** stoneValue = [6,2,3,4,5,5]
**Output:** 18
**Explanation:** In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice's score is now 11.
In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 16 (11 + 5).
The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.

**Example 2:**

**Input:** stoneValue = [7,7,7,7,7,7,7]
**Output:** 28

**Example 3:**

**Input:** stoneValue = [4]
**Output:** 0

**Constraints:**

- `1 <= stoneValue.length <= 500`
- `1 <= stoneValue[i] <= 106`

## Code

```python
class Solution:
    def stoneGameV(self, arr: List[int]) -> int:
        from functools import cache
        from itertools import accumulate
        
        # prefix sum for calculating the sum from i to j
        prefix = list(accumulate(arr))
        
        @cache
        def solve(l, r):
            if l >= r:
                return 0
            curr = float('-inf')
            # check each non-empty partition
            for mid in range(l, r):
	            # left and right sum for comparison
                l_sum = prefix[mid] - (prefix[l-1] if l>0 else 0)
                r_sum = prefix[r] - prefix[mid]

                if l_sum < r_sum:
                    curr = max(curr, l_sum + solve(l, mid))
                elif l_sum > r_sum:
                    curr = max(curr, r_sum + solve(mid+1, r))
                else: # if both are equal then return the maximum of both the partition
                    curr = max(curr, l_sum + solve(l, mid), r_sum + solve(mid+1, r))
            
            return curr
        
        return solve(0, len(arr)-1)
```

**With proper comments**

```python
class Solution:
    def stoneGameV(self, arr: List[int]) -> int:
        from functools import cache
        from itertools import accumulate

        # ---------------------------------------------------------
        # Prefix sum array
        #
        # prefix[i] = sum of arr[0] ... arr[i]
        #
        # This allows us to calculate the sum of any subarray
        # arr[l...r] in O(1) time.
        #
        # Sum of arr[l...r]:
        #     prefix[r] - prefix[l-1]
        #
        # If l == 0, there is no prefix[l-1], so we simply use 0.
        # ---------------------------------------------------------
        prefix = list(accumulate(arr))

        # ---------------------------------------------------------
        # solve(l, r):
        # Returns the maximum score we can obtain from the
        # subarray arr[l...r].
        #
        # We try every possible partition:
        #
        #     arr[l ... mid] | arr[mid+1 ... r]
        #
        # Depending on which side has the smaller sum, we are
        # forced to continue the game on that side.
        # ---------------------------------------------------------
        @cache
        def solve(l, r):

            # If there is only one element, we cannot split it,
            # so no more points can be obtained.
            if l >= r:
                return 0

            # Store the best score among all possible partitions.
            curr = float('-inf')

            # Try every possible partition point.
            #
            # Example:
            # arr = [6, 2, 3, 4]
            #
            # For l = 0, r = 3:
            #
            # mid = 0 -> [6] | [2,3,4]
            # mid = 1 -> [6,2] | [3,4]
            # mid = 2 -> [6,2,3] | [4]
            #
            for mid in range(l, r):

                # -------------------------------------------------
                # Calculate the sum of the left part:
                #
                #     arr[l ... mid]
                # -------------------------------------------------
                l_sum = prefix[mid] - (prefix[l - 1] if l > 0 else 0)

                # -------------------------------------------------
                # Calculate the sum of the right part:
                #
                #     arr[mid+1 ... r]
                # -------------------------------------------------
                r_sum = prefix[r] - prefix[mid]

                # -------------------------------------------------
                # Case 1:
                # Left sum is smaller.
                #
                # We gain the left sum and must continue playing
                # with the left subarray.
                # -------------------------------------------------
                if l_sum < r_sum:
                    curr = max(
                        curr,
                        l_sum + solve(l, mid)
                    )

                # -------------------------------------------------
                # Case 2:
                # Right sum is smaller.
                #
                # We gain the right sum and must continue playing
                # with the right subarray.
                # -------------------------------------------------
                elif l_sum > r_sum:
                    curr = max(
                        curr,
                        r_sum + solve(mid + 1, r)
                    )

                # -------------------------------------------------
                # Case 3:
                # Both sides have the same sum.
                #
                # Since both sides are equal, we are allowed to
                # choose either side.
                #
                # Therefore, take the better of:
                #
                #     left sum + best score from left
                #     right sum + best score from right
                # -------------------------------------------------
                else:
                    curr = max(
                        curr,
                        l_sum + solve(l, mid),
                        r_sum + solve(mid + 1, r)
                    )

            # Return the best score possible for arr[l...r].
            return curr

        # Start with the complete array.
        return solve(0, len(arr) - 1)
```