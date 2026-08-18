---
tags:
  - tree
  - dfs
  - binary-tree
---

# 110. Balanced Binary Tree

## Problem Statement

Given the root of a binary tree, determine whether the tree is **height-balanced**.

A binary tree is considered **height-balanced** if, for every node in the tree, the difference in height between its left and right subtrees is **at most 1**.

Return:

- `true` if the tree is height-balanced.
- `false` otherwise.

---

## Examples

### Example 1

**Input**

```text
root = [3,9,20,null,null,15,7]
```

**Output**

```text
true
```

---

### Example 2

**Input**

```text
root = [1,2,2,3,3,null,null,4,4]
```

**Output**

```text
false
```

---

### Example 3

**Input**

```text
root = []
```

**Output**

```text
true
```

---

## Constraints

```text
The number of nodes in the tree is in the range [0, 5000].
-10^4 <= Node.val <= 10^4
```

## Algorithm (Bottom-Up):

1. If the node is NULL, return height 0.
2. Recursively compute the height of the left subtree.
    If it returns -1, the tree is unbalanced.
3. Recursively compute the height of the right subtree.
    If it returns -1, the tree is unbalanced.
4. If abs(leftHeight - rightHeight) > 1, return -1.
5. Otherwise, return 1 + max(leftHeight, rightHeight).

If the final result is -1, the tree is not balanced; otherwise, it is balanced.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def height(self, root):
        if root is None:
            return 0
        
        left = self.height(root.left)
        if left == -1:
            return -1
        
        right = self.height(root.right)
        if right == -1:
            return -1
        
        if (abs(left - right)) > 1:
            return -1
        
        return 1 + max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.height(root) != -1
```