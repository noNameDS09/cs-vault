# 875. Koko Eating Bananas

## Problem Statement

Koko loves to eat bananas. There are `n` piles of bananas, where the `i`th pile contains `piles[i]` bananas. The guards will return in `h` hours.

Koko can choose an eating speed of `k` bananas per hour.

During each hour:

- She chooses **one pile** of bananas.
- She eats up to `k` bananas from that pile.
- If the pile contains fewer than `k` bananas, she eats all of them and does not eat from any other pile during that hour.

Return the **minimum integer** `k` such that Koko can finish eating all the bananas within `h` hours.

---

## Examples

### Example 1

**Input**

```text
piles = [3,6,7,11]
h = 8
```

**Output**

```text
4
```

---

### Example 2

**Input**

```text
piles = [30,11,23,4,20]
h = 5
```

**Output**

```text
30
```

---

### Example 3

**Input**

```text
piles = [30,11,23,4,20]
h = 6
```

**Output**

```text
23
```

---

## Constraints

```text
1 <= piles.length <= 10^4
piles.length <= h <= 10^9
1 <= piles[i] <= 10^9
```

```python
class Solution:

    def canEat(self, piles, mid, h):
        ans = 0
        for i in piles:
            ans += i//mid
            if i % mid != 0:
                ans += 1
        
        return ans <= ha

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            mid = l + (r-l) // 2

            if self.canEat(piles, mid, h):
                r = mid
            else:
                l = mid+1

        return l
```