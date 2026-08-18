---
tags:
  - tree
  - bst
  - dfs
---

# 235. Lowest Common Ancestor of a Binary Search Tree

## Problem Statement

Given the root of a **Binary Search Tree (BST)** and two nodes `p` and `q`, return their **Lowest Common Ancestor (LCA)**.

The **Lowest Common Ancestor (LCA)** of two nodes is the lowest node in the tree that has both `p` and `q` as descendants. A node can be a descendant of itself.

---

## Examples

### Example 1

**Input**

```text
root = [6,2,8,0,4,7,9,null,null,3,5]
p = 2
q = 8
```

**Output**

```text
6
```

**Explanation**

```text
The lowest common ancestor of nodes 2 and 8 is 6.
```

---

### Example 2

**Input**

```text
root = [6,2,8,0,4,7,9,null,null,3,5]
p = 2
q = 4
```

**Output**

```text
2
```

**Explanation**

```text
The lowest common ancestor of nodes 2 and 4 is 2.

A node can be a descendant of itself, so 2 is the LCA.
```

---

### Example 3

**Input**

```text
root = [2,1]
p = 2
q = 1
```

**Output**

```text
2
```

---

## Constraints

```text
The number of nodes in the tree is in the range [2, 10^5].
-10^9 <= Node.val <= 10^9
All Node.val values are unique.
p != q
p and q will both exist in the BST.
```

## Code

**Algorithm**:
Case 1 : If `p` and `q` both are less than `root` then the answer is on the `left`
Case 2 : If `p` and `q` both are greater than `root` then the answer is on the `right`
Else : `root` itself is the answer

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
```