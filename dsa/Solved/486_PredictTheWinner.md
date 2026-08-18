---
tags:
  - array
  - dynamic-programming
  - game-theory
  - minimax
---

# 486. Predict the Winner

## Problem Statement

You are given an integer array `nums`. Two players are playing a game with this array: **Player 1** and **Player 2**.

- Player 1 starts first.
- Both players begin with a score of `0`.
- On each turn, a player chooses **one number** from either end of the array (`nums[0]` or `nums[nums.length - 1]`).
- The chosen number is added to the player's score, and the array size decreases by one.
- The game ends when there are no numbers left.

Return `true` if **Player 1** can win the game. If both players finish with the same score, Player 1 is still considered the winner, so return `true`.

You may assume that **both players play optimally**.

---

## Examples

### Example 1

**Input**

```text
nums = [1,5,2]
```

**Output**

```text
false
```

**Explanation**

```text
Initially, Player 1 can choose either 1 or 2.

If Player 1 chooses 2 (or 1), Player 2 can choose 5.

The final scores become:

Player 1 = 3
Player 2 = 5

Therefore, Player 1 cannot win.
```

---

### Example 2

**Input**

```text
nums = [1,5,233,7]
```

**Output**

```text
true
```

**Explanation**

```text
Player 1 first chooses 1.

Player 2 must choose either 5 or 7.

Regardless of Player 2's choice, Player 1 can then choose 233.

Final scores:

Player 1 = 234
Player 2 = 12

Therefore, Player 1 wins.
```

---

## Constraints

```text
1 <= nums.length <= 20
0 <= nums[i] <= 10^7
```

## Code

```python
class Solution:
	def predictTheWinner(self, nums: List[int]) -> bool:
		n = len(nums)
		if ~n & 1: return True
		
		@cache
		def solve(i, j):
			if i == j: return nums[i]
			return max(
					nums[i] - solve(i+1, j),
					nums[j] - solve(i, j-1)
				)
		
		return solve(0, n-1) >= 0
```

---
## What the problem asks

Two players take turns picking a number from **either end** of the array. Each plays optimally. Does Player 1 win (score ≥ Player 2)?

---

## The key insight — score difference instead of absolute scores

Instead of tracking both players' scores separately, the function tracks the **net score difference** from the perspective of whoever is currently picking.

When it's your turn with subarray `nums[i..j]`:

- Pick `nums[i]` → your net gain = `nums[i] - solve(i+1, j)` (opponent now plays on the remaining array, their gain becomes your loss)
- Pick `nums[j]` → your net gain = `nums[j] - solve(i, j-1)`

You play **optimally**, so you take the `max` of both. If the final result `>= 0`, Player 1's net advantage is non-negative, so they win or tie.

---

## Line by line

```python
n = len(nums)
if ~n & 1: return True
```

`~n` is bitwise NOT of `n`, equal to `-(n+1)`. So `~n & 1` checks if `-(n+1)` is odd, which is true when `n` is even. **When the array length is even, Player 1 always wins** — they can always mirror the opponent's strategy to guarantee at least half the total. So we short-circuit immediately.

```python
@cache
def solve(i, j):
```

`solve(i, j)` returns the **maximum score difference** the current player can achieve over the opponent on subarray `nums[i..j]`. `@cache` memoizes results (more on this below).

```python
if i == j: return nums[i]
```

Base case — only one element left, current player must take it. Net gain = `nums[i]`.

```python
return max(
    nums[i] - solve(i+1, j),
    nums[j] - solve(i, j-1)
)
```

- `nums[i] - solve(i+1, j)` — pick left end; opponent then plays optimally on `[i+1..j]`, their gain `solve(i+1, j)` becomes **your loss**
- `nums[j] - solve(i, j-1)` — pick right end; same logic

Take the `max` because you play optimally.

```python
return solve(0, n-1) >= 0
```

Player 1 goes first on the full array. If their net score difference ≥ 0, they win or tie.

---

## Why `@cache`?

Without it, the recursion recomputes the same subproblems **exponentially** many times.

Consider `nums = [1, 2, 3, 4]`. The call tree for `solve(0, 3)` branches like this:

```
solve(0,3)
├── solve(1,3)          # pick left (nums[0])
│   ├── solve(2,3)
│   └── solve(1,2)  ← computed here
└── solve(0,2)          # pick right (nums[3])
    ├── solve(1,2)  ← would be recomputed here without cache
    └── solve(0,1)
```

`solve(1, 2)` appears in multiple branches. Without caching, it gets recomputed every time. The total unique subproblems are all pairs `(i, j)` where `i <= j` — that's only **O(n²)** states. `@cache` stores each result the first time and returns it instantly on repeat calls.

|                  | Without `@cache` | With `@cache`    |
| ---------------- | ---------------- | ---------------- |
| Time complexity  | O(2ⁿ)            | O(n²)            |
| Space complexity | O(n) call stack  | O(n²) memo table |


`@cache` (from `functools`) is Python's built-in **LRU cache with no size limit** — equivalent to `@lru_cache(maxsize=None)`. It works on functions with hashable arguments (integers, tuples — not lists). Since `i` and `j` are integers here, it works perfectly.

---

## Dry run — `nums = [1, 2, 3, 4]`

Array is length 4 (even) → the short-circuit `if ~n & 1` fires and returns `True` immediately. So let's use `nums = [1, 5, 2]` (odd length, no short-circuit):

```
solve(0, 2):
  pick nums[0]=1 → 1 - solve(1,2)
    solve(1,2):
      pick nums[1]=5 → 5 - solve(2,2) = 5 - 2 = 3
      pick nums[2]=2 → 2 - solve(1,1) = 2 - 5 = -3
      return max(3, -3) = 3
  → 1 - 3 = -2

  pick nums[2]=2 → 2 - solve(0,1)
    solve(0,1):
      pick nums[0]=1 → 1 - solve(1,1) = 1 - 5 = -4
      pick nums[1]=5 → 5 - solve(0,0) = 5 - 1 = 4
      return max(-4, 4) = 4
  → 2 - 4 = -2

solve(0,2) = max(-2, -2) = -2
```

`-2 >= 0` is `False` → Player 1 loses. Player 2 wins with optimal play. ✓

---

## The mental model to remember

> `solve(i, j)` = "if I play optimally and my opponent plays optimally, by how much do I beat them on this subarray?"

Positive → current player wins. Negative → current player loses. The subtraction `nums[i] - solve(...)` is the core move: **you gain, opponent plays next and their gain flips to your loss**.