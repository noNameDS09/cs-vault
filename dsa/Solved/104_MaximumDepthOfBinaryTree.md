---
tags:
  - tree
  - dfs
  - bfs
  - binary-tree
---

# 104. Maximum Depth of Binary Tree

## Problem Statement

Given the root of a binary tree, return its **maximum depth**.

The **maximum depth** of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node.

---

## Examples

### Example 1

**Input**

```text
root = [3,9,20,null,null,15,7]
```

**Output**

```text
3
```

---

### Example 2

**Input**

```text
root = [1,null,2]
```

**Output**

```text
2
```

---

## Constraints

```text
The number of nodes in the tree is in the range [0, 10^4].
-100 <= Node.val <= 100
```

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```