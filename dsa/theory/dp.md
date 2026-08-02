# Dynamic Programming - Complete Guide for Coding Interviews

## Table of Contents
1. [Introduction](#introduction)
2. [Core Concepts](#core-concepts)
3. [When to Use DP](#when-to-use-dp)
4. [Approaches](#approaches)
5. [Common Patterns & Templates](#common-patterns--templates)
6. [Classic Problems](#classic-problems)
7. [Space Optimization Techniques](#space-optimization-techniques)
8. [Interview Tips](#interview-tips)
9. [Practice Problems by Difficulty](#practice-problems-by-difficulty)

---

## Introduction

**Dynamic Programming (DP)** is an algorithmic technique for solving optimization problems by breaking them down into simpler subproblems and storing the results of these subproblems to avoid redundant computations.

### Key Properties
- **Optimal Substructure**: An optimal solution can be constructed from optimal solutions of its subproblems
- **Overlapping Subproblems**: The same subproblems are solved multiple times

---

## Core Concepts

### State
A state represents a specific subproblem. Usually denoted as `dp[i]`, `dp[i][j]`, etc.

### Transition
The recurrence relation that defines how to compute the current state from previous states.

### Base Case
The simplest subproblem(s) that can be solved directly without recursion.

### Memoization (Top-Down)
```python
def dp(i):
    if i in memo:
        return memo[i]
    if base_case:
        return base_value
    memo[i] = transition(dp(i-1), dp(i-2), ...)
    return memo[i]
```

### Tabulation (Bottom-Up)
```python
dp = [0] * (n + 1)
dp[0] = base_value
for i in range(1, n + 1):
    dp[i] = transition(dp[i-1], dp[i-2], ...)
return dp[n]
```

---

## When to Use DP

| Indicator | Example |
|-----------|---------|
| "Maximum/Minimum" | Longest Increasing Subsequence |
| "Number of ways" | Climbing Stairs, Coin Change |
| "Can we achieve X?" | Subset Sum, Partition Equal Subset Sum |
| Decisions affect future choices | House Robber, Stock Trading |
| String/sequence matching | Edit Distance, LCS |

---

## Approaches

### 1. Top-Down (Memoization/Recursion + Cache)
- **Pros**: Intuitive, only computes needed states
- **Cons**: Recursion depth limit, function call overhead

### 2. Bottom-Up (Tabulation/Iterative)
- **Pros**: No recursion limit, faster, easier to optimize space
- **Cons**: Must compute all states, less intuitive initially

---

## Common Patterns & Templates

### Pattern 1: 1D DP - Linear Sequence

#### Template: Fibonacci / Climbing Stairs
```python
def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# Space Optimized O(1)
def climbStairs_opt(n: int) -> int:
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
```

#### Template: House Robber (Decision at each step)
```python
def rob(nums: List[int]) -> int:
    if not nums:
        return 0
    n = len(nums)
    if n == 1:
        return nums[0]
    
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    return dp[-1]

# Space Optimized
def rob_opt(nums: List[int]) -> int:
    prev2 = prev1 = 0
    for num in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + num)
    return prev1
```

#### Template: Maximum Subarray (Kadane's Algorithm)
```python
def maxSubArray(nums: List[int]) -> int:
    max_ending_here = max_so_far = nums[0]
    for num in nums[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
```

---

### Pattern 2: 2D DP - Grid/Matrix Problems

#### Template: Unique Paths / Grid DP
```python
def uniquePaths(m: int, n: int) -> int:
    dp = [[1] * n for _ in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]

# Space Optimized to O(n)
def uniquePaths_opt(m: int, n: int) -> int:
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j-1]
    return dp[-1]
```

#### Template: Minimum Path Sum
```python
def minPathSum(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[m-1][n-1]
```

#### Template: Edit Distance (Levenshtein Distance)
```python
def minDistance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # delete
                    dp[i][j-1],    # insert
                    dp[i-1][j-1]   # replace
                )
    
    return dp[m][n]
```

#### Template: Longest Common Subsequence (LCS)
```python
def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

# Space Optimized to O(min(m,n))
def lcs_opt(text1: str, text2: str) -> int:
    if len(text1) < len(text2):
        text1, text2 = text2, text1
    m, n = len(text1), len(text2)
    dp = [0] * (n + 1)
    
    for i in range(1, m + 1):
        prev = 0
        for j in range(1, n + 1):
            temp = dp[j]
            if text1[i-1] == text2[j-1]:
                dp[j] = 1 + prev
            else:
                dp[j] = max(dp[j], dp[j-1])
            prev = temp
    
    return dp[n]
```

---

### Pattern 3: Knapsack / Subset Problems

#### Template: 0/1 Knapsack
```python
def knapsack(weights: List[int], values: List[int], capacity: int) -> int:
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't take item i
            dp[i][w] = dp[i-1][w]
            # Take item i if it fits
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w-weights[i-1]] + values[i-1])
    
    return dp[n][capacity]

# Space Optimized O(W) - Iterate backwards!
def knapsack_opt(weights: List[int], values: List[int], capacity: int) -> int:
    dp = [0] * (capacity + 1)
    
    for i in range(len(weights)):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[capacity]
```

#### Template: Coin Change (Minimum Coins)
```python
def coinChange(coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1
```

#### Template: Coin Change 2 (Number of Ways)
```python
def change(amount: int, coins: List[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]
    
    return dp[amount]
```

#### Template: Subset Sum / Partition Equal Subset Sum
```python
def canPartition(nums: List[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False
    
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    
    return dp[target]
```

---

### Pattern 4: Interval DP

#### Template: Burst Balloons / Matrix Chain Multiplication
```python
def maxCoins(nums: List[int]) -> int:
    # Add boundary 1s
    nums = [1] + [n for n in nums if n > 0] + [1]
    n = len(nums)
    
    dp = [[0] * n for _ in range(n)]
    
    # length of subarray
    for length in range(2, n):
        for left in range(0, n - length):
            right = left + length
            # Try every possible last balloon to burst
            for k in range(left + 1, right):
                dp[left][right] = max(
                    dp[left][right],
                    nums[left] * nums[k] * nums[right] + dp[left][k] + dp[k][right]
                )
    
    return dp[0][n-1]
```

#### Template: Palindrome Partitioning / Minimum Cuts
```python
def minCut(s: str) -> int:
    n = len(s)
    # is_pal[i][j] = True if s[i:j+1] is palindrome
    is_pal = [[False] * n for _ in range(n)]
    
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            is_pal[i][j] = (s[i] == s[j]) and (j - i < 2 or is_pal[i+1][j-1])
    
    # dp[i] = min cuts for s[i:]
    dp = [0] * (n + 1)
    dp[n] = -1  # base case: empty string needs -1 cuts
    
    for i in range(n-1, -1, -1):
        dp[i] = float('inf')
        for j in range(i, n):
            if is_pal[i][j]:
                dp[i] = min(dp[i], 1 + dp[j+1])
    
    return dp[0]
```

---

### Pattern 5: DP on Strings - Palindromes

#### Template: Longest Palindromic Subsequence
```python
def longestPalindromeSubseq(s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n-1, -1, -1):
        dp[i][i] = 1
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
    return dp[0][n-1]
```

#### Template: Longest Palindromic Substring
```python
def longestPalindrome(s: str) -> str:
    n = len(s)
    if n < 2:
        return s
    
    dp = [[False] * n for _ in range(n)]
    start, max_len = 0, 1
    
    for i in range(n):
        dp[i][i] = True
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2 or dp[i+1][j-1]:
                    dp[i][j] = True
                    if length > max_len:
                        start, max_len = i, length
    
    return s[start:start+max_len]
```

---

### Pattern 6: Stock Trading Problems

#### Template: Best Time to Buy and Sell Stock (1 transaction)
```python
def maxProfit(prices: List[int]) -> int:
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit
```

#### Template: Best Time to Buy and Sell Stock II (Unlimited transactions)
```python
def maxProfit(prices: List[int]) -> int:
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit
```

#### Template: Best Time to Buy and Sell Stock III (At most 2 transactions)
```python
def maxProfit(prices: List[int]) -> int:
    if not prices:
        return 0
    
    # buy1, sell1, buy2, sell2
    buy1 = buy2 = float('inf')
    sell1 = sell2 = 0
    
    for price in prices:
        buy1 = min(buy1, price)
        sell1 = max(sell1, price - buy1)
        buy2 = min(buy2, price - sell1)  # reinvest profit from sell1
        sell2 = max(sell2, price - buy2)
    
    return sell2
```

#### Template: Best Time to Buy and Sell Stock with Cooldown
```python
def maxProfit(prices: List[int]) -> int:
    if not prices:
        return 0
    
    n = len(prices)
    # hold[i]: max profit on day i holding a stock
    # sold[i]: max profit on day i just sold
    # rest[i]: max profit on day i in cooldown/rest
    
    hold = -prices[0]
    sold = 0
    rest = 0
    
    for i in range(1, n):
        prev_hold, prev_sold, prev_rest = hold, sold, rest
        hold = max(prev_hold, prev_rest - prices[i])
        sold = prev_hold + prices[i]
        rest = max(prev_rest, prev_sold)
    
    return max(sold, rest)
```

#### Template: Best Time to Buy and Sell Stock with Transaction Fee
```python
def maxProfit(prices: List[int], fee: int) -> int:
    hold = -prices[0]
    sold = 0
    
    for price in prices[1:]:
        hold = max(hold, sold - price)
        sold = max(sold, hold + price - fee)
    
    return sold
```

---

### Pattern 7: Longest Increasing Subsequence (LIS)

#### Template: O(n²) DP
```python
def lengthOfLIS(nums: List[int]) -> int:
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n
    
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)
```

#### Template: O(n log n) with Binary Search (Patience Sorting)
```python
from bisect import bisect_left

def lengthOfLIS(nums: List[int]) -> int:
    tails = []
    
    for num in nums:
        idx = bisect_left(tails, num)
        if idx == len(tails):
            tails.append(num)
        else:
            tails[idx] = num
    
    return len(tails)
```

#### Template: Number of LIS
```python
def findNumberOfLIS(nums: List[int]) -> int:
    if not nums:
        return 0
    
    n = len(nums)
    lengths = [1] * n  # length of LIS ending at i
    counts = [1] * n   # count of LIS ending at i
    
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                if lengths[j] + 1 > lengths[i]:
                    lengths[i] = lengths[j] + 1
                    counts[i] = counts[j]
                elif lengths[j] + 1 == lengths[i]:
                    counts[i] += counts[j]
    
    max_len = max(lengths)
    return sum(c for l, c in zip(lengths, counts) if l == max_len)
```

---

### Pattern 8: DP on Trees

#### Template: House Robber III (Binary Tree)
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rob(root: TreeNode) -> int:
    def dfs(node):
        if not node:
            return (0, 0)  # (rob_this, not_rob_this)
        
        left = dfs(node.left)
        right = dfs(node.right)
        
        # If we rob this node, we cannot rob children
        rob_this = node.val + left[1] + right[1]
        
        # If we don't rob this, we can choose to rob or not rob children
        not_rob_this = max(left) + max(right)
        
        return (rob_this, not_rob_this)
    
    return max(dfs(root))
```

#### Template: Diameter of Binary Tree
```python
def diameterOfBinaryTree(root: TreeNode) -> int:
    self.max_diameter = 0
    
    def depth(node):
        if not node:
            return 0
        left = depth(node.left)
        right = depth(node.right)
        self.max_diameter = max(self.max_diameter, left + right)
        return 1 + max(left, right)
    
    depth(root)
    return self.max_diameter
```

---

### Pattern 9: Bitmask DP

#### Template: Traveling Salesman Problem (TSP)
```python
def tsp(dist: List[List[int]]) -> int:
    n = len(dist)
    # dp[mask][i] = min cost to visit all cities in mask, ending at i
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0  # Start at city 0
    
    for mask in range(1 << n):
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v):
                    continue
                new_mask = mask | (1 << v)
                dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + dist[u][v])
    
    # Return to start
    return min(dp[(1 << n) - 1][u] + dist[u][0] for u in range(n))
```

#### Template: Assign Tasks to Workers (Min Cost)
```python
def minCost(cost: List[List[int]]) -> int:
    n = len(cost)
    dp = [float('inf')] * (1 << n)
    dp[0] = 0
    
    for mask in range(1 << n):
        i = bin(mask).count('1')  # Current worker
        if i >= n:
            continue
        for j in range(n):
            if not (mask & (1 << j)):
                dp[mask | (1 << j)] = min(dp[mask | (1 << j)], dp[mask] + cost[i][j])
    
    return dp[(1 << n) - 1]
```

---

### Pattern 10: Digit DP

#### Template: Count Numbers with Property
```python
def countNumbers(num: str) -> int:
    from functools import lru_cache
    
    @lru_cache(None)
    def dfs(pos: int, tight: bool, leading_zero: bool, state) -> int:
        if pos == len(num):
            return 1 if is_valid(state) else 0
        
        limit = int(num[pos]) if tight else 9
        total = 0
        
        for digit in range(limit + 1):
            new_tight = tight and (digit == limit)
            new_leading_zero = leading_zero and (digit == 0)
            new_state = update_state(state, digit, new_leading_zero)
            total += dfs(pos + 1, new_tight, new_leading_zero, new_state)
        
        return total
    
    return dfs(0, True, True, initial_state)
```

---

## Classic Problems Summary

| Problem | Pattern | Time | Space | Key Insight |
|---------|---------|------|-------|-------------|
| Climbing Stairs | 1D Linear | O(n) | O(1) | Fibonacci |
| House Robber | 1D Linear | O(n) | O(1) | Max of (take, skip) |
| Coin Change | 1D Knapsack | O(n*amount) | O(amount) | Unbounded knapsack |
| Coin Change 2 | 1D Knapsack | O(n*amount) | O(amount) | Ways to make amount |
| Edit Distance | 2D String | O(m*n) | O(min(m,n)) | Insert/Delete/Replace |
| LCS | 2D String | O(m*n) | O(min(m,n)) | Match or skip |
| LIS | 1D Sequence | O(n log n) | O(n) | Patience sorting |
| Max Subarray | 1D Linear | O(n) | O(1) | Kadane's algorithm |
| Unique Paths | 2D Grid | O(m*n) | O(n) | Right + Down |
| Min Path Sum | 2D Grid | O(m*n) | O(n) | Min of (up, left) |
| Knapsack 0/1 | 2D Knapsack | O(n*W) | O(W) | Reverse iteration |
| Partition Equal | Subset Sum | O(n*sum) | O(sum) | Target = sum/2 |
| Burst Balloons | Interval DP | O(n³) | O(n²) | Last balloon to burst |
| Palindrome Part. | Interval DP | O(n²) | O(n²) | Precompute palindromes |
| Stock I/II/III | State Machine | O(n) | O(1) | Track buy/sell states |
| House Robber III | Tree DP | O(n) | O(h) | (rob, not_rob) tuple |
| TSP | Bitmask DP | O(n²*2ⁿ) | O(n*2ⁿ) | Mask = visited cities |

---

## Space Optimization Techniques

### 1. Rolling Array (2 rows for 2D DP)
```python
# Instead of dp[m][n]
dp = [[0] * n for _ in range(2)]
for i in range(m):
    curr = i % 2
    prev = 1 - curr
    for j in range(n):
        dp[curr][j] = transition(dp[prev][j], dp[curr][j-1])
```

### 2. Single Array (1D for 2D DP)
```python
# For problems where dp[i][j] depends on dp[i-1][j] and dp[i][j-1]
dp = [0] * n
for i in range(m):
    for j in range(n):
        if j > 0:
            dp[j] = transition(dp[j], dp[j-1])
        else:
            dp[j] = transition(dp[j], base)
```

### 3. Reverse Iteration (0/1 Knapsack)
```python
# MUST iterate backwards to avoid using updated values
for i in range(n):
    for w in range(capacity, weight[i] - 1, -1):
        dp[w] = max(dp[w], dp[w - weight[i]] + value[i])
```

### 4. Two Variables (Fibonacci-like)
```python
a, b = 0, 1
for _ in range(n):
    a, b = b, a + b
return a
```

---

## Interview Tips

### 1. **Identify the Problem Type**
- Keywords: "maximum", "minimum", "number of ways", "can we", "longest"
- Draw small examples to find pattern

### 2. **Define State Clearly**
- What does `dp[i]` or `dp[i][j]` represent?
- Write it as a comment

### 3. **Find Recurrence Relation**
- How to get current state from previous?
- Consider all choices at each step

### 4. **Determine Base Cases**
- Smallest subproblems
- Empty string/array, single element

### 5. **Decide Order of Computation**
- Top-down: recursion + memo
- Bottom-up: identify dependencies

### 6. **Optimize Space**
- Can you use 1D instead of 2D?
- Can you use O(1) variables?
- Reverse iteration for 0/1 knapsack

### 7. **Handle Edge Cases**
- Empty input
- Single element
- All negative numbers
- Large numbers (use modulo if needed)

### 8. **Trace Through Example**
- Manual trace for n=3 or n=4
- Verify recurrence works

---

## Practice Problems by Difficulty

### Easy
1. **Climbing Stairs** (LeetCode 70)
2. **House Robber** (LeetCode 198)
3. **Maximum Subarray** (LeetCode 53)
4. **Best Time to Buy and Sell Stock** (LeetCode 121)
5. **Fibonacci Number** (LeetCode 509)
6. **Min Cost Climbing Stairs** (LeetCode 746)

### Medium
1. **Coin Change** (LeetCode 322)
2. **Coin Change 2** (LeetCode 518)
3. **Longest Increasing Subsequence** (LeetCode 300)
4. **Edit Distance** (LeetCode 72)
5. **Longest Common Subsequence** (LeetCode 1143)
6. **Unique Paths** (LeetCode 62)
7. **Minimum Path Sum** (LeetCode 64)
8. **House Robber II** (LeetCode 213)
9. **Decode Ways** (LeetCode 91)
10. **Partition Equal Subset Sum** (LeetCode 416)
11. **Best Time to Buy and Sell Stock II** (LeetCode 122)
12. **Maximum Product Subarray** (LeetCode 152)
13. **Longest Palindromic Substring** (LeetCode 5)
14. **Palindromic Substrings** (LeetCode 647)

### Hard
1. **Burst Balloons** (LeetCode 312)
2. **Best Time to Buy and Sell Stock III** (LeetCode 123)
3. **Best Time to Buy and Sell Stock IV** (LeetCode 188)
4. **Regular Expression Matching** (LeetCode 10)
5. **Wildcard Matching** (LeetCode 44)
6. **Distinct Subsequences** (LeetCode 115)
7. **Interleaving String** (LeetCode 97)
8. **Palindrome Partitioning II** (LeetCode 132)
9. **Russian Doll Envelopes** (LeetCode 354)
10. **Cherry Pickup** (LeetCode 741)
11. **TSP** (Variations)
12. **Number of Music Playlists** (LeetCode 920)

---

## Quick Reference: State Definitions

| Problem | State Definition |
|---------|------------------|
| Fibonacci | `dp[i]` = i-th Fibonacci number |
| House Robber | `dp[i]` = max money from first i houses |
| Coin Change | `dp[i]` = min coins to make amount i |
| LIS | `dp[i]` = length of LIS ending at index i |
| LCS | `dp[i][j]` = LCS of text1[:i] and text2[:j] |
| Edit Distance | `dp[i][j]` = min ops to convert word1[:i] to word2[:j] |
| Knapsack | `dp[i][w]` = max value using first i items with weight w |
| Stock | `hold/sold/rest` = max profit in each state |
| Grid | `dp[i][j]` = min/max/path to reach (i,j) |
| Palindrome | `dp[i][j]` = is s[i:j+1] palindrome / LPS length |

---

## Python-Specific Tips

### Use `functools.lru_cache` for Memoization
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def dp(i, j):
    # recursive calls
    return result
```

### Use `bisect` for LIS O(n log n)
```python
from bisect import bisect_left, bisect_right
```

### Use `float('inf')` and `-float('inf')` for Min/Max
```python
dp = [float('inf')] * (n + 1)
dp[0] = 0
```

### List Comprehension for 2D Arrays
```python
dp = [[0] * n for _ in range(m)]
# NOT: [[0] * n] * m  (creates references to same list!)
```

### Tuple Unpacking for State Transitions
```python
hold, sold = sold - price, max(sold, hold + price)
```

---

## Common Mistakes to Avoid

1. **Wrong iteration order** - For 0/1 knapsack, iterate weight backwards
2. **Shallow copy** - `[[0]*n]*m` creates m references to same list
3. **Off-by-one errors** - Be careful with `range(n)` vs `range(n+1)`
4. **Forgetting base cases** - Empty string, single element, zero capacity
5. **Not handling negative numbers** - Kadane's needs special handling
6. **Space optimization too early** - Get correct 2D version first
7. **Confusing "at most k" vs "exactly k"** - Different state definitions
8. **Not using modulo** - When problem asks for answer % MOD

---

## Final Checklist Before Submitting

- [ ] State definition is clear and correct
- [ ] Recurrence relation handles all choices
- [ ] Base cases cover all edge conditions
- [ ] Iteration order respects dependencies
- [ ] Space optimization is correct (if applied)
- [ ] Time complexity matches constraints
- [ ] Tested with: empty, single, small, large inputs
- [ ] Modulo applied if required
- [ ] Variable names are descriptive
- [ ] Comments explain the logic

---

*Last Updated: 2024*
*Happy Coding! 🚀*