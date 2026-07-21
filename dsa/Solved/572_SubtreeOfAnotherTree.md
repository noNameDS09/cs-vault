# 572. Subtree of Another Tree

## Problem Statement

Given the roots of two binary trees `root` and `subRoot`, return `true` if there exists a **subtree** of `root` that has the same structure and node values as `subRoot`. Otherwise, return `false`.

A **subtree** of a binary tree is a tree that consists of a node and **all of its descendants**. A tree is also considered a subtree of itself.

---

## Examples

### Example 1

**Input**

```text
root = [3,4,5,1,2]
subRoot = [4,1,2]
```

**Output**

```text
true
```

---

### Example 2

**Input**

```text
root = [3,4,5,1,2,null,null,null,null,0]
subRoot = [4,1,2]
```

**Output**

```text
false
```

---

## Constraints

```text
The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-10^4 <= root.val <= 10^4
-10^4 <= subRoot.val <= 10^4
```

## Code
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def same(self, s, t):
        if not s and not t: # if leaf nodes of null trees
            return True
        
        if s and t and s.val == t.val: # if nodes and equal values recursively call the 'same' function (it will go until both are leaf nodes) for the left and right nodes
            return self.same(s.left, t.left) and self.same(s.right, t.right)
        
        return False

    def isSubtree(self, T: Optional[TreeNode], subT: Optional[TreeNode]) -> bool:
        if not subT: return True # every null subtree is subtree of other tree
        if not T: return False # if other tree is null (no need to check if sub tree is null as we have checked it previously)

        if self.same(T, subT): # call the function
            return True
        
        return self.isSubtree(T.left, subT) or self.isSubtree(T.right, subT) # Recursively call the function to explore the child of main (other) tree
```