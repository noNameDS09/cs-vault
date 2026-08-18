---
tags:
  - array
  - matrix
  - simulation
---

# 1260. Shift 2D Grid

## Problem Statement

You are given a 2D grid of size `m × n` and an integer `k`.

You need to shift the grid `k` times.

In one shift operation:

- The element at `grid[i][j]` moves to `grid[i][j + 1]`.
- The element at `grid[i][n - 1]` moves to `grid[i + 1][0]`.
- The element at `grid[m - 1][n - 1]` moves to `grid[0][0]`.

Return the 2D grid after applying the shift operation `k` times.

---

## Examples

### Example 1

**Input**

```text
grid = [[1,2,3],
        [4,5,6],
        [7,8,9]]
k = 1
```

**Output**

```text
[[9,1,2],
 [3,4,5],
 [6,7,8]]
```

---

### Example 2

**Input**

```text
grid = [[3,8,1,9],
        [19,7,2,5],
        [4,6,11,10],
        [12,0,21,13]]
k = 4
```

**Output**

```text
[[12,0,21,13],
 [3,8,1,9],
 [19,7,2,5],
 [4,6,11,10]]
```

---

### Example 3

**Input**

```text
grid = [[1,2,3],
        [4,5,6],
        [7,8,9]]
k = 9
```

**Output**

```text
[[1,2,3],
 [4,5,6],
 [7,8,9]]
```

---

## Constraints

```text
m == grid.length
n == grid[i].length
1 <= m <= 50
1 <= n <= 50
-1000 <= grid[i][j] <= 1000
0 <= k <= 100
```

```python
class Solution:

    def rev(self, arr, i, j):
        while i<j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        col = len(grid[0])

        grid = [j for i in grid for j in i]
        n = len(grid)
        k %= n

        self.rev(grid, 0, n-1)
        self.rev(grid, 0, k-1)
        self.rev(grid, k, n-1)

        ans = []

        j = col
        for i in range(0, n, col):
            ans.append(grid[i:j])
            j += col
        
        return ans
```