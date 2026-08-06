# [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

## Problem Statement

Given the root of a binary tree, determine whether it is a **valid Binary Search Tree (BST)**.

A valid BST satisfies the following properties:

- The left subtree of a node contains only nodes with values **strictly less** than the node's value.
- The right subtree of a node contains only nodes with values **strictly greater** than the node's value.
- Both the left and right subtrees must also be valid Binary Search Trees.

Return:

- `true` if the tree is a valid BST.
- `false` otherwise.

---

## Examples

### Example 1

**Input**
<image src="https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg"> </image>

```text
root = [2,1,3]
```

**Output**

```text
true
```

---

### Example 2

**Input**
<image src="https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg"> </image>

```text
root = [5,1,4,null,null,3,6]
```

**Output**

```text
false
```

**Explanation**

```text
The root node has value 5, but its right child has value 4,
which violates the BST property because 4 is not greater than 5.
```

---

## Constraints

```text
The number of nodes in the tree is in the range [1, 10^4].
-2^31 <= Node.val <= 2^31 - 1
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

    def inorder(self, root, arr):
        if root:
            self.inorder(root.left, arr)
            arr.append(root.val)
            self.inorder(root.right, arr)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        self.inorder(root, arr)
        # print(arr)
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                return False

        return True
```