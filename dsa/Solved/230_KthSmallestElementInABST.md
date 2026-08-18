---
tags:
  - tree
  - bst
  - dfs
  - inorder-traversal
---

# [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

## Problem Statement

Given the root of a **Binary Search Tree (BST)** and an integer `k`, return the **kth smallest** value (1-indexed) among all the nodes in the tree.

---

## Examples

### Example 1

**Input**
<image src="https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg"> </image>

```text
root = [3,1,4,null,2]
k = 1
```

**Output**

```text
1
```

---

### Example 2

**Input**
<image src="https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg"> </image>
```text
root = [5,3,6,2,4,null,null,1]
k = 3
```

**Output**

```text
3
```

---

## Constraints

```text
The number of nodes in the tree is n.
1 <= k <= n <= 10^4
0 <= Node.val <= 10^4
```

---

## Follow-up

If the BST is modified frequently (i.e., insertions and deletions are performed often) and you need to find the **kth smallest** element repeatedly, how would you optimize the solution?

## Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root, arr):
        if root:
            self.dfs(root.left, arr)
            arr.append(root.val)
            self.dfs(root.right, arr)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        self.dfs(root, arr)
        print(arr)
        i = 0
        while i<k:
            i+=1
        return arr[i-1]
```