---
tags:
  - array
  - stack
  - monotonic-stack
  - sorting
---

# 853. Car Fleet

There are `n` cars at given miles away from the starting mile `0`, traveling to reach the mile `target`.


You are given two integer arrays `position` and `speed`, both of length `n`, where:

- `position[i]` is the starting mile of the `i-th` car.
- `speed[i]` is the speed of the `i-th` car in miles per hour.

A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.

A **car fleet** is a single car or a group of cars driving next to each other. The speed of the fleet is the minimum speed of any car in the fleet.

If a car catches up to a car fleet exactly at the target, it is still considered part of that fleet.

Return the number of car fleets that will arrive at the destination.

## Example 1

**Input**
```text
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
```

**Output**
```text
3
```

## Example 2

**Input**
```text
target = 10
position = [3]
speed = [3]
```

**Output**
```text
1
```

## Example 3

**Input**
```text
target = 100
position = [0,2,4]
speed = [4,2,1]
```

**Output**
```text
1
```

## Constraints

```text
1 <= n <= 10^5
n == position.length == speed.length
0 < target <= 10^6
0 <= position[i] < target
All values in position are unique.
1 <= speed[i] <= 10^6
```

```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(pairs)[::-1]:
            stack.append((target - p) / s)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
```