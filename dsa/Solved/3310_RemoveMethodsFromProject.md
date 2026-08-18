---
tags:
  - array
  - graph
  - topological-sort
---

# 3310. Remove Methods From Project

## Problem Statement

You are maintaining a project that contains `n` methods numbered from `0` to `n - 1`.

You are given:

- An integer `n`, representing the number of methods.
- An integer `k`, representing a method that is known to contain a bug.
- A 2D integer array `invocations`, where:

```text
invocations[i] = [a_i, b_i]
```

indicates that method `a_i` invokes method `b_i`.

Method `k`, along with every method that is invoked by it (either directly or indirectly), is considered **suspicious**.

A group of suspicious methods can only be removed if **no method outside the group invokes any method inside the group**.

Return an array containing all the **remaining methods** after removing the suspicious methods.

- You may return the methods in **any order**.
- If it is **not possible** to remove all suspicious methods, return **all methods** (i.e., remove nothing).

---

## Examples

### Example 1

**Input**
<image src="https://assets.leetcode.com/uploads/2024/07/18/graph-2.png"></image>


```text
n = 4
k = 1
invocations = [[1,2],[0,1],[3,2]]
```

**Output**

```text
[0,1,2,3]
```

**Explanation**

```text
Methods 1 and 2 are suspicious.

However, methods 0 and 3 (which are not suspicious)
invoke methods inside the suspicious group.

Therefore, the suspicious methods cannot be removed,
so all methods remain.
```

---

### Example 2

**Input**
<image src="https://assets.leetcode.com/uploads/2024/07/18/graph-3.png"> </image>


```text
n = 5
k = 0
invocations = [[1,2],[0,2],[0,1],[3,4]]
```

**Output**

```text
[3,4]
```

**Explanation**

```text
Methods 0, 1, and 2 are suspicious.

No method outside this group invokes any of them,
so they can all be removed.

The remaining methods are:
[3,4]
```

---

### Example 3

**Input**

<image src="https://assets.leetcode.com/uploads/2024/07/20/graph.png"/> 


```text
n = 3
k = 2
invocations = [[1,2],[0,1],[2,0]]
```

**Output**

```text
[]
```

**Explanation**

```text
Every method is suspicious.

Since there are no methods outside the suspicious group,
all methods can be removed.

The remaining project is empty.
```

---

## Constraints

```text
1 <= n <= 10^5
0 <= k <= n - 1
0 <= invocations.length <= 2 × 10^5
invocations[i] == [a_i, b_i]
0 <= a_i, b_i <= n - 1
a_i != b_i
invocations[i] != invocations[j]
```

## Code

```python
from typing import List
from collections import defaultdict, deque


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Build the directed graph where:
        # u -> v means method u invokes method v.
        graph = defaultdict(list)
        for u, v in invocations:
            graph[u].append(v)

        # suspect[i] = True if method i is considered suspicious.
        suspect = [False] * n
        suspect[k] = True  # The initially infected/suspicious method.

        # Perform BFS/DFS (using deque) to mark all methods
        # that are reachable from the suspicious method.
        queue = deque([k])

        while queue:
            current = queue.pop()

            # Visit all methods invoked by the current method.
            for neighbor in graph[current]:
                if not suspect[neighbor]:
                    suspect[neighbor] = True
                    queue.append(neighbor)

        # Check whether any non-suspicious method invokes
        # a suspicious method.
        #
        # If such an edge exists, the suspicious methods cannot
        # be removed independently because they are still required
        # by a safe method. Hence, return all methods.
        for u, v in invocations:
            if not suspect[u] and suspect[v]:
                return list(range(n))

        # Otherwise, all suspicious methods can be removed safely.
        # Return the indices of the remaining (non-suspicious) methods.
        return [method for method in range(n) if not suspect[method]]
```