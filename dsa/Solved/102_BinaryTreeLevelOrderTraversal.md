---
tags:
  - tree
  - bfs
  - binary-tree
---

# 102. Binary Tree Level Order Traversal

## Problem Statement

Given the root of a binary tree, return the **level order traversal** of its nodes' values.

In a level order traversal, nodes are visited **level by level**, from **left to right**.

---

## Examples

### Example 1

**Input**

```text
root = [3,9,20,null,null,15,7]
```

**Output**

```text
[[3],[9,20],[15,7]]
```

---

### Example 2

**Input**

```text
root = [1]
```

**Output**

```text
[[1]]
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
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
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
	'''
	Implement BFS
	'''
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        from collections import deque
        
		ans = []    # array to store the answer
        queue = deque([root])
        # print(len(queue))
        while queue:
            size = len(queue)    # get the current size of queue (level)
            temp = []
            for i in range(size):   # push all the nodes that are at same level
                node = queue.popleft()
                temp.append(node.val)
                if node.left:    
                    queue.append(node.left)    # push the left child
				if node.right:
					queue.append(node.right)   # push the right child
            ans.append(temp)
        return ans
```