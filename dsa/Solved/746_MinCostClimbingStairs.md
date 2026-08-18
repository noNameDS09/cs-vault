---
tags:
  - array
  - dynamic-programming
---

# 746. Min Cost Climbing Stairs

## Problem Statement

You are given an integer array `cost` where `cost[i]` is the cost of the `i`th step on a staircase.

Once you pay the cost of a step, you can climb either:

- **One step**, or
- **Two steps**.

You may start from either:

- Step with index `0`, or
- Step with index `1`.

Return the **minimum cost** required to reach the top of the floor.

---

## Examples

### Example 1

**Input**

```text
cost = [10,15,20]
```

**Output**

```text
15
```

**Explanation**

```text
Start at index 1.

- Pay 15.
- Climb two steps to reach the top.

Total cost = 15.
```

---

### Example 2

**Input**

```text
cost = [1,100,1,1,1,100,1,1,100,1]
```

**Output**

```text
6
```

**Explanation**

```text
Start at index 0.

- Pay 1 and climb two steps to index 2.
- Pay 1 and climb two steps to index 4.
- Pay 1 and climb two steps to index 6.
- Pay 1 and climb one step to index 7.
- Pay 1 and climb two steps to index 9.
- Pay 1 and climb one step to reach the top.

Total cost = 6.
```

---

## Constraints

```text
2 <= cost.length <= 1000
0 <= cost[i] <= 999
```

### Code

This solution is using recursion and in-built memoization (`@cache`):
```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        @cache  # Memoization
        def solve(i):
            if i >= n:   # Base condition
                return 0
                
            # recursive call to further
            return min(
                cost[i] + solve(i + 1),
                cost[i] + solve(i + 2)
            )
        # either start from 0 or 1
        return min(solve(0), solve(1))
```


Apply the 4 mechanical rules from House Robber:

```
1. dp array of size n+2 (safe for i+2 boundary)
2. Base cases → dp[n] = 0, dp[n+1] = 0  (already handled by 0-init)
3. Loop from n-1 → 0  (opposite of recursion direction)
4. Replace solve(i) with dp[i]
5. Return min(dp[0], dp[1])
```

Your memoized version:

```python
return cost[i] + min(solve(i + 1), solve(i + 2))
```

Tabulated version — fill this in:

```python
def minCostClimbingStairs(cost):
    n = len(cost)
    dp = [0] * (n + 2)

    for i in range(n - 1, -1, -1):
        dp[i] = _______________

    return _______________
```

Two blanks. Fill them in — it's a direct translation of your memoized code.

This solution is using manual memoization of tabulation : 
```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        dp = [0] * (n+2)
        dp[0], dp[0] = 0, 0  # Base cases (similar to i >= n)
        
        for i in range(n-1, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        
        return min(dp[0], dp[1])
```


Spot on. The tabulation is correct — recurrence translated perfectly, loop direction right, return right.

Only issue is this line which does nothing useful:

```python
dp[0], dp[0] = 0, 0   # ← assigns dp[0] twice, should be dp[0], dp[1]
```

But since the whole array is already `0` from `[0] * (n+2)`, it doesn't affect correctness at all — just a typo to be aware of.

---

Now finish the job. One step left — **space optimization.**

You did this translation:

```
solve(i) → dp[i]
```

Now look at your loop — at every step `i`, you only ever look at `dp[i+1]` and `dp[i+2]`. You never look back further. So you don't need the full array — just two variables.

Same pattern as House Robber Stage 4. Apply it:

```python
def minCostClimbingStairs(cost):
    n = len(cost)
    next1 = 0    # was dp[i+1]
    next2 = 0    # was dp[i+2]

    for i in range(n - 1, -1, -1):
        curr = _______________   # same recurrence
        next2 = _______________  # shift window
        next1 = _______________  # shift window

    return _______________
```

Three blanks and a return. Fill them in — it's a direct copy of your tabulation logic with variable names swapped.

This is above implementation:
```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        next1, next2 = 0, 0

        for i in range(n-1, -1, -1):
            curr = cost[i] + min(next1, next2)
            next2 = next1
            next1 = curr
        
        return min(next1, next2)
```

Perfect. All four stages done cleanly.

But look at your return carefully:

```python
return min(next1, next2)
```

After the loop ends, `next2` holds what was `next1` at `i=1`, and `next1` holds `curr` at `i=0`. So this is actually returning `min(dp[0], dp[1])` — which is exactly right. You got it correctly by intuition, good.

---

### You've now solved one problem four ways. Look at the full progression:

```python
# Stage 1 — Brute recursion         O(2^n) time  O(n) space
return cost[i] + min(solve(i+1), solve(i+2))

# Stage 2 — Memoization             O(n) time    O(n) space
@cache
return cost[i] + min(solve(i+1), solve(i+2))    # identical logic

# Stage 3 — Tabulation              O(n) time    O(n) space
dp[i] = cost[i] + min(dp[i+1], dp[i+2])         # identical logic

# Stage 4 — Space optimized         O(n) time    O(1) space
curr = cost[i] + min(next1, next2)               # identical logic
```

The recurrence `cost[i] + min(next, next+2)` never changed once across all four stages. That's the core insight of DP — **find the recurrence once, then just change how you evaluate it.**

---

