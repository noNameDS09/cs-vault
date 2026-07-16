# 226. Invert Binary Tree

## Problem Statement

Given the root of a binary tree, invert the tree and return its root.

Inverting a binary tree means swapping the left and right child of every node in the tree.

---

## Examples

### Example 1

**Input**

```text
root = [4,2,7,1,3,6,9]
```

**Output**

```text
[4,7,2,9,6,3,1]
```

---

### Example 2

**Input**

```text
root = [2,1,3]
```

**Output**

```text
[2,3,1]
```

---

### Example 3

**Input**

```text
root = []
```

**Output**

```text
[]
```

---

## Constraints

```text
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
```

### General Structure to solve the binary trees
1. if not ```root``` return
2. solve(root.left)
3. solve(root.right)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
```