---
tags:
  - array
  - dynamic-programming
  - game-theory
  - suffix-sum
---

# [1140. Stone Game II](https://leetcode.com/problems/stone-game-ii/)

Alice and Bob continue their games with piles of stones. There are a number of piles **arranged in a row**, and each pile has a positive integer number of stones `piles[i]`. The objective of the game is to end with the most stones.

Alice and Bob take turns, with Alice starting first.

On each player's turn, that player can take **all the stones** in the **first** `X` remaining piles, where `1 <= X <= 2M`. Then, we set `M = max(M, X)`. Initially, M = 1.

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

**Example 1:**

**Input:** piles = [2,7,9,4,4]

**Output:** 10

**Explanation:**

- If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get `2 + 4 + 4 = 10` stones in total.
- If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get `2 + 7 = 9` stones in total.

So we return 10 since it's larger.

**Example 2:**

**Input:** piles = [1,2,3,4,5,100]

**Output:** 104

**Constraints:**

- `1 <= piles.length <= 100`
- `1 <= piles[i] <= 104`

## Code

```python
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # suffix[i] = total stones from i to end
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        from functools import cache

        @cache
        def solve(i, m):
            # No stones left
            if i >= n:
                return 0

            mx = 0

            # Try taking 1 to 2*m piles
            for j in range(1, 2 * m + 1):
                if i + j > n:
                    break

                # Current stones - opponent's best score
                mx = max(
                    mx,
                    suffix[i] - solve(i + j, max(m, j))
                )

            return mx

        return solve(0, 1)
```