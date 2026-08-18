---
tags:
  - array
  - dynamic-programming
  - game-theory
  - math
---

# [2029. Stone Game IX](https://leetcode.com/problems/stone-game-ix/)

Alice and Bob continue their games with stones. There is a row of n stones, and each stone has an associated value. You are given an integer array `stones`, where `stones[i]` is the **value** of the `ith` stone.

Alice and Bob take turns, with **Alice** starting first. On each turn, the player may remove any stone from `stones`. The player who removes a stone **loses** if the **sum** of the values of **all removed stones** is divisible by `3`. Bob will win automatically if there are no remaining stones (even if it is Alice's turn).

Assuming both players play **optimally**, return `true` _if Alice wins and_ `false` _if Bob wins_.

**Example 1:**

**Input:** stones = [2,1]
**Output:** true
**Explanation:** The game will be played as follows:
- Turn 1: Alice can remove either stone.
- Turn 2: Bob removes the remaining stone. 
The sum of the removed stones is 1 + 2 = 3 and is divisible by 3. Therefore, Bob loses and Alice wins the game.

**Example 2:**

**Input:** stones = [2]
**Output:** false
**Explanation:** Alice will remove the only stone, and the sum of the values on the removed stones is 2. 
Since all the stones are removed and the sum of values is not divisible by 3, Bob wins the game.

**Example 3:**

**Input:** stones = [5,1,2,4,3]
**Output:** false
**Explanation:** Bob will always win. One possible way for Bob to win is shown below:
- Turn 1: Alice can remove the second stone with value 1. Sum of removed stones = 1.
- Turn 2: Bob removes the fifth stone with value 3. Sum of removed stones = 1 + 3 = 4.
- Turn 3: Alices removes the fourth stone with value 4. Sum of removed stones = 1 + 3 + 4 = 8.
- Turn 4: Bob removes the third stone with value 2. Sum of removed stones = 1 + 3 + 4 + 2 = 10.
- Turn 5: Alice removes the first stone with value 5. Sum of removed stones = 1 + 3 + 4 + 2 + 5 = 15.
Alice loses the game because the sum of the removed stones (15) is divisible by 3. Bob wins the game.

**Constraints:**

- `1 <= stones.length <= 105`
- `1 <= stones[i] <= 104`

## Code

```python
class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        arr = [0, 0, 0]

        for i in stones:
            arr[i % 3] += 1
        
        if arr[0] %2 == 0:
            return arr[1] > 0 and arr[2] > 0
        
        return abs(arr[1]-arr[2]) > 2
```

## Intuition

# Stone Game IX

> [!abstract] Core Idea  
> **Only `x % 3` matters.**  
> Reduce every stone to one of three categories: remainder `0`, `1`, or `2`.

---

## 1. Problem

Alice and Bob take turns removing one stone.

- Alice goes first.
    
- Keep a running sum of removed stone values.
    
- If the running sum becomes divisible by `3`, the player who made that move **loses immediately**.
    
- If all stones are removed without anyone losing, Alice loses because she has no move left.
    
- Both players play optimally.
    

The goal is to determine whether **Alice can win**.

---

## 2. Key Observation — Only the Remainder Matters

For this game, the actual value of a stone is irrelevant.

We only care about:

```text
x % 3
```

For example:

|Stone|Remainder|
|---|--:|
|`1`|`1`|
|`2`|`2`|
|`3`|`0`|
|`4`|`1`|
|`5`|`2`|
|`7`|`1`|
|`8`|`2`|

Therefore, classify all stones into three groups:

```text
cnt[0] = number of stones where x % 3 == 0
cnt[1] = number of stones where x % 3 == 1
cnt[2] = number of stones where x % 3 == 2
```

For:

```text
stones = [2, 2, 5, 7, 8, 9]
```

we get:

```text
cnt[0] = 1
cnt[1] = 1
cnt[2] = 4
```

---

## 3. Why Remainder `0` Is Special

Suppose the current sum is:

```text
0 % 3
```

Taking a remainder-`0` stone gives:

```text
0 + 0 = 0
```

So the player immediately loses.

However, when the current sum is `1` or `2`, a remainder-`0` stone is safe:

```text
1 + 0 = 1
2 + 0 = 2
```

Therefore, `0` stones act like **safe extra moves**.

Their most important property is their **parity**:

```text
cnt[0] % 2
```

We don't need their exact count for the final decision.

---

## 4. Why Remainders `1` and `2` Matter

Suppose the current sum is `0`.

### Pick a `1`

The sum becomes:

```text
0 + 1 = 1
```

Now picking a `2` would cause:

```text
1 + 2 = 3
```

which is divisible by `3`, so the player taking the `2` loses.

### Pick a `2`

Similarly:

```text
0 + 2 = 2
```

and picking a `1` would cause:

```text
2 + 1 = 3
```

and lose immediately.

So `1` and `2` effectively oppose each other.

This is why the difference between:

```text
cnt[1]
```

and

```text
cnt[2]
```

is important.

---

## 5. The Important Counts

Let:

```text
cnt0 = cnt[0]
cnt1 = cnt[1]
cnt2 = cnt[2]
```

The game can be reduced to:

1. Whether `cnt1 == cnt2`
    
2. Whether `cnt0` is even or odd
    
3. If `cnt0` is odd, how large `|cnt1 - cnt2|` is
    

---

## 6. Final Winning Condition

The reliable condition is:

```python
if cnt1 == cnt2:
    return False

if cnt0 % 2 == 0:
    return True

return abs(cnt1 - cnt2) >= 3
```

In other words:

### Case 1 — Equal numbers of `1`s and `2`s

```text
cnt1 == cnt2
```

Alice loses.

---

### Case 2 — Unequal numbers and an even number of `0`s

```text
cnt1 != cnt2
cnt0 % 2 == 0
```

Alice wins.

---

### Case 3 — Unequal numbers and an odd number of `0`s

When:

```text
cnt0 % 2 == 1
```

Alice wins only if:

```text
|cnt1 - cnt2| >= 3
```

Otherwise, Alice loses.

---

## 7. Final Algorithm

### Step 1 — Count the remainders

```python
cnt = [0, 0, 0]

for x in stones:
    cnt[x % 3] += 1
```

### Step 2 — Apply the game-theory condition

```python
cnt0, cnt1, cnt2 = cnt

if cnt1 == cnt2:
    return False

if cnt0 % 2 == 0:
    return True

return abs(cnt1 - cnt2) >= 3
```

---

## 8. Complete Python Solution

```python
def stoneGameIX(stones):
    cnt = [0, 0, 0]

    for x in stones:
        cnt[x % 3] += 1

    cnt0, cnt1, cnt2 = cnt

    if cnt1 == cnt2:
        return False

    if cnt0 % 2 == 0:
        return True

    return abs(cnt1 - cnt2) >= 3
```

---

## 9. Example 1

```text
stones = [2, 1]
```

Counts:

```text
cnt0 = 0
cnt1 = 1
cnt2 = 1
```

Since:

```text
cnt1 == cnt2
```

Alice loses.

```text
Answer = False
```

---

## 10. Example 2

```text
stones = [1, 1, 1]
```

Counts:

```text
cnt0 = 0
cnt1 = 3
cnt2 = 0
```

We have:

```text
cnt1 != cnt2
```

and:

```text
cnt0 % 2 == 0
```

Therefore:

```text
Answer = True
```

Alice wins.

---

## 11. Example 3

Suppose:

```text
cnt0 = 1
cnt1 = 5
cnt2 = 2
```

Then:

```text
cnt1 != cnt2
```

and:

```text
cnt0 % 2 == 1
```

The difference is:

```text
|5 - 2| = 3
```

Since:

```text
3 >= 3
```

Alice wins.

---

## 12. Why Actual Values Don't Matter

Consider:

```text
[1, 4, 7, 10]
```

Every value has:

```text
x % 3 == 1
```

So, from the perspective of the game, they are equivalent.

Likewise:

```text
[2, 5, 8, 11]
```

all behave like remainder `2`.

Therefore, a potentially huge collection of values can be compressed into just:

```text
cnt0
cnt1
cnt2
```

This is a common competitive-programming technique:

> **When the game depends only on a value modulo `k`, classify values by their remainder instead of tracking the actual values.**

---

## 13. Complexity

We scan the array once.

### Time

```text
O(n)
```

Every stone is processed exactly once.

### Space

```text
O(1)
```

Only three counters are required:

```text
cnt0
cnt1
cnt2
```

---

## 14. Interview Memory Trick

If you need to remember the solution quickly, remember these four points:

> **1. Only `x % 3` matters.**

> **2. Count remainder `0`, `1`, and `2`.**

> **3. `1` and `2` are opposing moves.**

> **4. `0` stones mainly matter through their parity.**

Then remember:

```python
if cnt1 == cnt2:
    return False

if cnt0 % 2 == 0:
    return True

return abs(cnt1 - cnt2) >= 3
```

---

## 15. Final Takeaway

The difficult part of **Stone Game IX** is not the implementation.

The key is recognizing that the entire game can be compressed from arbitrary stone values into three counts:

```text
┌──────────────┬──────────────────────────┐
│ Remainder    │ Meaning                  │
├──────────────┼──────────────────────────┤
│ 0            │ Safe extra moves         │
│ 1            │ One side of the battle   │
│ 2            │ Opposing side             │
└──────────────┴──────────────────────────┘
```

Once those counts are known, the solution is just a few conditions.

**Pattern to remember:**

```text
Huge values
    ↓
Take modulo 3
    ↓
Count 0 / 1 / 2
    ↓
Analyze parity + imbalance
    ↓
O(n) time, O(1) space
```