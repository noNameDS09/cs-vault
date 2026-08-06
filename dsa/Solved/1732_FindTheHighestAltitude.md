# [1732. Find the Highest Altitude](https://leetcode.com/problems/find-the-highest-altitude/)

## Problem Statement

There is a biker going on a road trip consisting of `n + 1` points at different altitudes.

The biker starts at point `0` with an altitude of `0`.

You are given an integer array `gain` of length `n`, where:

```text
gain[i]
```

represents the **net gain in altitude** between points `i` and `i + 1`.

Return the **highest altitude** reached during the trip.

---

## Examples

### Example 1

**Input**

```text
gain = [-5,1,5,0,-7]
```

**Output**

```text
1
```

**Explanation**

```text
Starting altitude = 0

Altitudes at each point:

[0, -5, -4, 1, 1, -6]

The highest altitude reached is 1.
```

---

### Example 2

**Input**

```text
gain = [-4,-3,-2,-1,4,3,2]
```

**Output**

```text
0
```

**Explanation**

```text
Starting altitude = 0

Altitudes at each point:

[0, -4, -7, -9, -10, -6, -3, -1]

The highest altitude reached is 0.
```

---

## Constraints

```text
n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100
```

## Code

```python
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        curr = 0

        for i in gain:
            curr += i
            ans = max(ans, curr)

        return ans
```