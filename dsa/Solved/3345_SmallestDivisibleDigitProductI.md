# [3345. Smallest Divisible Digit Product I](https://leetcode.com/problems/smallest-divisible-digit-product-i/)

## Problem Statement

You are given two integers `n` and `t`.

Return the **smallest integer greater than or equal to** `n` such that the **product of its digits** is divisible by `t`.

---

## Examples

### Example 1

**Input**

```text
n = 10
t = 2
```

**Output**

```text
10
```

**Explanation**

```text
The product of the digits of 10 is:

1 × 0 = 0

Since 0 is divisible by 2, 10 is the smallest integer
greater than or equal to 10 that satisfies the condition.
```

---

### Example 2

**Input**

```text
n = 15
t = 3
```

**Output**

```text
16
```

**Explanation**

```text
The product of the digits of 16 is:

1 × 6 = 6

Since 6 is divisible by 3, 16 is the smallest integer
greater than or equal to 15 that satisfies the condition.
```

---

## Constraints

```text
1 <= n <= 100
1 <= t <= 10
```

## Code

```python
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        def product(x):
            p = 1
            while x > 0:
                p = p * (x%10)
                x = x // 10
            return p

        while True:
            p = product(n)
            if p % t == 0:
                return n
            n += 1
        
        return n
```