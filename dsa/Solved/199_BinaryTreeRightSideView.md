---
tags:
  - tree
  - bfs
  - dfs
  - binary-tree
---

# 199. Binary Tree Right Side View

## Problem Statement

Given the root of a binary tree, imagine yourself standing on the **right side** of the tree.

Return the values of the nodes you can see, ordered from **top to bottom**.

---

## Examples

### Example 1

**Input**

```text
root = [1,2,3,null,5,null,4]
```

**Output**

```text
[1,3,4]
```

---

### Example 2

**Input**

```text
root = [1,2,3,4,null,null,null,5]
```

**Output**

```text
[1,3,4,5]
```

---

### Example 3

**Input**

```text
root = [1,null,3]
```

**Output**

```text
[1,3]
```

---

### Example 4

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
	Implement the BFS
	
	Just pop the nodes until the last one remains from that level.
	The last node will append to the answer
	'''
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        from collections import deque
        q = deque([root])
        ans = []
        while q:
            temp = len(q)   # to track how many nodes are there in current level
            for i in range(temp-1):   # iterate until one node remains (right side view)
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            node = q.popleft()  # this is the rightmost node of that level
            # enqueue the remaining elements
            if node.left:  
			    q.append(node.left)
            if node.right:
                q.append(node.right)
			
			# append to the answer
            ans.append(node.val)

        return ans

```