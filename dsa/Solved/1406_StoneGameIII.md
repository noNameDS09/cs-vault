# 1406. Stone Game III

## Problem Statement

Alice and Bob are playing a game with a row of stones. Each stone has an associated integer value given in the array `stoneValue`.

Alice and Bob take turns, with **Alice going first**.

On each turn, a player may take **1, 2, or 3** stones from the beginning of the remaining row.

- Each player's score is the sum of the values of the stones they take.
- Both players start with a score of `0`.
- The game ends when all stones have been taken.

Both Alice and Bob play **optimally**.

Return:

- `"Alice"` if Alice wins.
- `"Bob"` if Bob wins.
- `"Tie"` if both players finish with the same score.

---

## Examples

### Example 1

**Input**

```text
stoneValue = [1,2,3,7]
```

**Output**

```text
"Bob"
```

**Explanation**

```text
Alice's best move is to take the first three stones,
giving her a score of 6.

Bob then takes the remaining stone worth 7 and wins.
```

---

### Example 2

**Input**

```text
stoneValue = [1,2,3,-9]
```

**Output**

```text
"Alice"
```

**Explanation**

```text
Alice should take the first three stones.

If she takes only one or two stones initially,
Bob can play optimally and force Alice to take the
negative-valued stone, causing her to lose.

Taking the first three stones immediately guarantees Alice's victory.
```

---

### Example 3

**Input**

```text
stoneValue = [1,2,3,6]
```

**Output**

```text
"Tie"
```

**Explanation**

```text
Alice cannot force a win.

However, by taking the first three stones,
she can ensure that the game ends in a tie.
```

---

## Constraints

```text
1 <= stoneValue.length <= 5 × 10^4
-1000 <= stoneValue[i] <= 1000
```

## Code

```python
class Solution:
    def stoneGameIII(self, arr: List[int]) -> str:
        n = len(arr)
        from functools import cache
        @cache
        def solve(i):
            if i >= n:
                return 0
            
            s = 0
            mx = float('-inf')

            for k in range(3):
                if i + k < n:
                    s += arr[i+k]
                    mx = max(mx, s - solve(i+k+1))
            
            return mx
        
        d = solve(0)
        if d > 0:
            return "Alice"
        elif d < 0:
            return "Bob"
        
        return "Tie"
```