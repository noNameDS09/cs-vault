---
tags:
  - tree
  - dfs
  - bfs
  - binary-tree
---

# 100. Same Tree

## Problem Statement

Given the roots of two binary trees `p` and `q`, determine whether they are the **same tree**.

Two binary trees are considered the same if:

- They are **structurally identical**.
- The corresponding nodes have the **same value**.

Return:

- `true` if the two trees are the same.
- `false` otherwise.

---

## Examples

### Example 1

**Input**

```text
p = [1,2,3]
q = [1,2,3]
```

**Output**

```text
true
```

---

### Example 2

**Input**

```text
p = [1,2]
q = [1,null,2]
```

**Output**

```text
false
```

---

### Example 3

**Input**

```text
p = [1,2,1]
q = [1,1,2]
```

**Output**

```text
false
```

---

## Constraints

```text
The number of nodes in both trees is in the range [0, 100].
-10^4 <= Node.val <= 10^4
```

```python
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def bfs(self, node):
        arr = []
        queue = deque([node])

        while queue:
            n = queue.popleft()
            if n is None:
                arr.append(None)
                continue
            
            arr.append(n.val)

            # if n.left:
            queue.append(n.left)
            # if n.right:
            queue.append(n.right)
        
        return arr

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.bfs(p) == self.bfs(q)
```        