# 543. Diameter of Binary Tree

## Problem Statement

Given the root of a binary tree, return the **diameter** of the tree.

The **diameter** of a binary tree is the length of the **longest path** between any two nodes in the tree. This path may or may not pass through the root.

The length of a path between two nodes is measured by the **number of edges** between them.

---

## Examples

### Example 1

**Input**

```text
root = [1,2,3,4,5]
```

**Output**

```text
3
```

**Explanation**

```text
The longest path is either:

4 → 2 → 1 → 3

or

5 → 2 → 1 → 3

Both paths contain 3 edges.
```

---

### Example 2

**Input**

```text
root = [1,2]
```

**Output**

```text
1
```

---

## Constraints

```text
The number of nodes in the tree is in the range [1, 10^4].
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


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def height(r):
            nonlocal diameter   # To avoid syntax error and logical error
            if r is None:
                return 0
            left = height(r.left)
            right = height(r.right)
            diameter = max(diameter, left + right)
            return 1 + max(left, right)
        
        height(root)
        return diameter
```