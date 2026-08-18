---
tags:
  - tree
  - dfs
  - bfs
  - binary-tree
---

# [1448. Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)

## Problem Statement

Given the root of a binary tree, a node `X` is considered **good** if, on the path from the root to `X`, there are **no nodes with a value greater than `X`**.

Return the **number of good nodes** in the binary tree.

---

## Examples

### Example 1

**Input**
<image src="https://assets.leetcode.com/uploads/2020/04/02/test_sample_1.png"> </image>

```text
root = [3,1,4,3,null,1,5]
```

**Output**

```text
4
```

**Explanation**

```text
The good nodes are:

- Root node (3), which is always good.
- Node 4, since 4 is the maximum value on the path (3 → 4).
- Node 5, since 5 is the maximum value on the path (3 → 4 → 5).
- Node 3, since 3 is the maximum value on the path (3 → 1 → 3).
```

---

### Example 2

**Input**
<image src="https://assets.leetcode.com/uploads/2020/04/02/test_sample_2.png"> </image>

```text
root = [3,3,null,4,2]
```

**Output**

```text
3
```

**Explanation**

```text
Node 2 is not good because the path
(3 → 3 → 2) contains a node with value 3,
which is greater than 2.
```

---

### Example 3

**Input**

```text
root = [1]
```

**Output**

```text
1
```

**Explanation**

```text
The root node is always considered good.
```

---

## Constraints

```text
The number of nodes in the binary tree is in the range [1, 10^5].
-10^4 <= Node.val <= 10^4
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
    def dfs(self, root, mx, count):
        if not root:
            return count
        if root.val >= mx:
            count += 1
        mx = max(mx, root.val)
        
        count = self.dfs(root.left, mx, count)        
        count = self.dfs(root.right, mx, count)
        
        return count

    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val, 0)
        
```