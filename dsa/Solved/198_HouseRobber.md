# 198. House Robber

## Problem Statement

You are a professional robber planning to rob houses along a street.

Each house contains a certain amount of money. The only constraint is that **adjacent houses have connected security systems**, so robbing two adjacent houses on the same night will automatically alert the police.

Given an integer array `nums`, where `nums[i]` represents the amount of money in the `i`th house, return the **maximum amount of money** you can rob without alerting the police.

---

## Examples

### Example 1

**Input**

```text
nums = [1,2,3,1]
```

**Output**

```text
4
```

**Explanation**

```text
Rob house 1 (money = 1) and house 3 (money = 3).

Total amount robbed = 1 + 3 = 4.
```

---

### Example 2

**Input**

```text
nums = [2,7,9,3,1]
```

**Output**

```text
12
```

**Explanation**

```text
Rob house 1 (money = 2),
house 3 (money = 9),
and house 5 (money = 1).

Total amount robbed = 2 + 9 + 1 = 12.
```

---

## Constraints

```text
1 <= nums.length <= 100
0 <= nums[i] <= 400
```

## Code

```python
class Solution:
	def rob(self, nums: List[int]) -> int:
		n = len(nums)
		@cache
		def solve(i):
			if i >= n: return 0
			return max(
				nums[i] + solve(i+2)
				solve(i+1)
			)
		return solve(0)
```


---

**Point 1 — "max money" is too vague.**

Max money _from where to where_? The whole array? From house `i` to the end?

The key to DP is that `solve(i)` must represent a **self-contained subproblem**. The most natural definition here is:

> `solve(i)` = maximum money you can rob **from house `i` to the last house**

This way `solve(0)` is the full answer, and `solve(i)` naturally depends on `solve(i+1)` and `solve(i+2)`.

---

**Point 2 — you skipped the base cases entirely.**

This is the most common reason DP code crashes or gives wrong answers. Ask yourself: what are the smallest inputs where you _know_ the answer without any recursion?

- `solve(n)` → no houses left → **return 0**
- `solve(n-1)` → only one house left, you must take it → **return nums[n-1]**

---

**Point 3 — "either choose i or skip it" is exactly right, but incomplete.**

You identified the two choices correctly. Now you need to say **what happens after each choice:**

- **Rob house `i`** → you gain `nums[i]`, but you _cannot_ rob house `i+1`, so you jump to `solve(i+2)`
- **Skip house `i`** → you gain nothing, move to `solve(i+1)`

You take the `max` of both because you play optimally.

---

So the full recurrence is:

```
solve(i) = max(
    nums[i] + solve(i+2),   # rob house i, skip i+1
    solve(i+1)              # skip house i
)
```

---

Now **you write the code.** Use the memoization template from above:

```python
memo = {}

def solve(i):
    # 1. base case(s)
    # 2. check cache
    # 3. compute using the recurrence
    # 4. store and return
```


One small gap though — you handled `i == n` but what if `solve(i+2)` gets called when `i+1 == n`? That means `i+2 == n+1`, which would go out of bounds... except your base case only catches `i == n`, not `i == n+1`.

Try it mentally: `nums = [5]`, n=1.

```
solve(0) → nums[0] + solve(2)
solve(2) → i == n+1, not caught!  ← IndexError
```

Fix is one extra base case:

```python
if i >= n:   # catches both n and n+1
    return 0
```

Change `==` to `>=` and your solution is airtight. Everything else is perfect.

---

Now let's convert your solution through all three stages side by side — this is the most important thing to see in one place.

```python
# ============================================================
# STAGE 1 — Pure recursion (your original thinking)
# Time: O(2^n)  Space: O(n) call stack
# ============================================================
def rob_v1(nums):
    n = len(nums)

    def solve(i):
        if i >= n:
            return 0
        return max(
            solve(i + 1),              # skip
            nums[i] + solve(i + 2)     # rob
        )

    return solve(0)


# ============================================================
# STAGE 2 — Memoization / Top-down DP (what you wrote)
# Time: O(n)  Space: O(n) memo + O(n) call stack
# ============================================================
def rob_v2(nums):
    n = len(nums)

    @cache
    def solve(i):
        if i >= n:
            return 0
        return max(
            solve(i + 1),
            nums[i] + solve(i + 2)
        )

    return solve(0)


# ============================================================
# STAGE 3 — Tabulation / Bottom-up DP
# Time: O(n)  Space: O(n) dp array
# ============================================================
def rob_v3(nums):
    n = len(nums)
    dp = [0] * (n + 2)    # +2 to safely handle i+2 at boundaries

    # Fill from RIGHT to LEFT (base cases are at the end)
    for i in range(n - 1, -1, -1):
        dp[i] = max(
            dp[i + 1],             # skip house i
            nums[i] + dp[i + 2]    # rob house i
        )

    return dp[0]


# ============================================================
# STAGE 4 — Space optimized (no array needed)
# Time: O(n)  Space: O(1)
# ============================================================
def rob_v4(nums):
    n = len(nums)
    next1 = 0    # represents dp[i+1]
    next2 = 0    # represents dp[i+2]

    for i in range(n - 1, -1, -1):
        curr = max(next1, nums[i] + next2)
        next2 = next1
        next1 = curr

    return next1
```

The key observation across all four stages — **the recurrence never changes:**

```
solve(i) = max(solve(i+1), nums[i] + solve(i+2))
```

You just change _how_ you evaluate it. Recursion evaluates it lazily top-down. Tabulation evaluates it eagerly bottom-up. Space optimization realizes you only ever look 1-2 steps ahead, so you don't need the full array.

---

### The tabulation conversion rule (works for any DP)

When converting your memoized solution to tabulation, follow these steps mechanically:

```
1. Create a dp array of size n (or n+1, n+2 if needed for boundary safety)
2. Fill in base cases directly into the array
3. Loop in the OPPOSITE direction of your recursion
   → your recursion went solve(0) → solve(n), so loop from n-1 → 0
4. Replace every solve(i) with dp[i]
5. Return dp[starting_point] instead of solve(starting_point)
```

---

### Dry run of Stage 3 on `nums = [2, 7, 9, 3, 1]`

```
n = 5
dp = [0, 0, 0, 0, 0, 0, 0]   ← size n+2, all zeros (base cases built in)
indices: 0  1  2  3  4  5  6

i=4: dp[4] = max(dp[5], nums[4]+dp[6]) = max(0, 1+0) = 1
i=3: dp[3] = max(dp[4], nums[3]+dp[5]) = max(1, 3+0) = 3
i=2: dp[2] = max(dp[3], nums[2]+dp[4]) = max(3, 9+1) = 10
i=1: dp[1] = max(dp[2], nums[1]+dp[3]) = max(10, 7+3) = 10
i=0: dp[0] = max(dp[1], nums[0]+dp[2]) = max(10, 2+10) = 12

return dp[0] = 12
```

Answer: rob houses 0, 2, 4 → `2 + 9 + 1 = 12` ✓

---

You've now completed the full DP journey on one problem:

```
Brute force recursion         O(2^n)
→ + memoization               O(n) time, O(n) space
→ + tabulation (bottom-up)    O(n) time, O(n) space, no recursion limit
→ + space optimization        O(n) time, O(1) space  ← interview gold
```

---

**Next problem to cement this — try this one yourself:**

> **LC #746 — Min Cost Climbing Stairs.** You're given an array `cost[]` where `cost[i]` is the cost to step on stair `i`. Once you pay, you can jump 1 or 2 steps. You can start from index 0 or 1. Find the minimum cost to reach the top (index n).

Answer the 3 questions first, then write the memoized version, then convert to tabulation. Post whatever you get — even partial.