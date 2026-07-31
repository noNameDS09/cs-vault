Tree problems on LeetCode look diverse, but a large percentage of them are variations of a few **core patterns**. If you master these templates, you can solve most binary tree questions quickly.

## 1. DFS Traversal Pattern (The Foundation)

**Use when:** You need to visit every node and compute something.

### Template

```python
def dfs(node):
    if not node:
        return

    # Do something with node

    dfs(node.left)
    dfs(node.right)
```

The three places where logic goes:

### Preorder: Root → Left → Right

Use for:

- Creating copies of trees
    
- Serialization
    
- Building paths
    

```python
def dfs(node):
    if not node:
        return

    process(node)
    dfs(node.left)
    dfs(node.right)
```

### Inorder: Left → Root → Right

Use for:

- Binary Search Tree sorted order
    
- Validating BST
    

```python
def dfs(node):
    if not node:
        return

    dfs(node.left)
    process(node)
    dfs(node.right)
```

### Postorder: Left → Right → Root

Use for:

- Height calculation
    
- Delete tree
    
- Bottom-up problems
    

```python
def dfs(node):
    if not node:
        return

    dfs(node.left)
    dfs(node.right)
    process(node)
```

---

# 2. Tree Height / Depth Pattern

**Common questions:**

- Maximum depth of binary tree
    
- Minimum depth
    
- Balanced binary tree
    
- Diameter of binary tree
    

### Key idea:

Return information from children to parent.

Example:

```python
def height(node):
    if not node:
        return 0

    left = height(node.left)
    right = height(node.right)

    return 1 + max(left, right)
```

### For balanced tree:

```python
def dfs(node):
    if not node:
        return 0

    left = dfs(node.left)
    if left == -1:
        return -1

    right = dfs(node.right)
    if right == -1:
        return -1

    if abs(left-right) > 1:
        return -1

    return 1 + max(left, right)
```

Pattern:

> Child gives answer → parent combines answers.

---

# 3. Tree Path Pattern

**Use when:**

- Root-to-leaf paths
    
- Path sum
    
- All paths
    
- Maximum path sum
    

## Root-to-leaf

Maintain current path:

```python
def dfs(node, path):
    if not node:
        return

    path.append(node.val)

    if not node.left and not node.right:
        print(path)

    dfs(node.left, path)
    dfs(node.right, path)

    path.pop()
```

Important:

```
choose
explore
unchoose
```

This is the same backtracking pattern.

---

# 4. Lowest Common Ancestor (LCA) Pattern

Questions:

- Lowest Common Ancestor of Binary Tree
    
- Find relationship between nodes
    

Idea:

Ask children:

"Did you find either target?"

```python
def lca(root, p, q):
    if not root or root == p or root == q:
        return root

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right:
        return root

    return left or right
```

Logic:

```
left found + right found
        |
      current node is answer
```

---

# 5. Level Order Traversal (BFS)

**Use when:**

- "Level by level"
    
- Minimum depth
    
- Right side view
    
- Zigzag traversal
    

Template:

```python
from collections import deque

def bfs(root):
    if not root:
        return []

    queue = deque([root])

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
```

The trick:

```python
level_size = len(queue)
```

captures one level.

---

# 6. Tree Construction Pattern

Questions:

- Build tree from preorder/inorder
    
- Serialize/deserialize
    

Usually:

```
array → tree
```

Example:

```python
def build(values):
    if not values:
        return None

    root = TreeNode(values[0])

    root.left = build(left_values)
    root.right = build(right_values)

    return root
```

For preorder + inorder:

Use hashmap:

```python
index = {value:i for i,value in enumerate(inorder)}
```

Then recursively split.

---

# 7. Binary Search Tree (BST) Pattern

BST property:

```
left < root < right
```

## Search

```python
def search(root, val):
    if not root:
        return None

    if root.val == val:
        return root

    if val < root.val:
        return search(root.left,val)

    return search(root.right,val)
```

---

## Validate BST

Don't compare only children.

Wrong:

```
       5
      /
     1
      \
       6  ❌
```

Use range:

```python
def valid(node, low, high):
    if not node:
        return True

    if not(low < node.val < high):
        return False

    return (
        valid(node.left, low, node.val)
        and
        valid(node.right, node.val, high)
    )
```

---

# 8. Tree + HashMap Pattern

**Use when:**  
You need information about nodes quickly.

Examples:

- Count paths
    
- Duplicate subtrees
    
- Vertical traversal
    

Example:

```python
count = {}

def dfs(node):
    if not node:
        return

    count[node.val] = count.get(node.val,0)+1

    dfs(node.left)
    dfs(node.right)
```

---

# 9. Convert Tree to Graph Pattern

Questions:

- Nodes at distance K
    
- Burn tree
    
- Find parents
    

Trees only have downward edges.

Add parent pointers:

```python
parent = {}

def build(node, par):
    if not node:
        return

    parent[node] = par

    build(node.left,node)
    build(node.right,node)
```

Now every node has:

```
left
right
parent
```

Run BFS.

---

# 10. Tree DP Pattern (Most Important)

Many hard tree problems are:

> Each node returns some information upward.

Example: Diameter

At every node:

```
left height
right height

answer = left + right
```

Template:

```python
answer = 0

def dfs(node):
    global answer

    if not node:
        return 0

    left = dfs(node.left)
    right = dfs(node.right)

    answer = max(answer, left+right)

    return 1 + max(left,right)
```

---

# How to Recognize Patterns Quickly

|Problem wording|Pattern|
|---|---|
|"maximum depth"|DFS height|
|"balanced"|DFS returning height|
|"path sum"|DFS path|
|"all paths"|Backtracking|
|"level order"|BFS queue|
|"nearest/minimum distance"|BFS|
|"ancestor"|LCA|
|"BST"|Inorder/range|
|"construct tree"|Divide & conquer|
|"distance between nodes"|Parent pointers + BFS|
|"maximum/minimum answer through node"|Tree DP|

---

## Suggested LeetCode Tree Learning Order

1. LeetCode Explore Cards basics:
    
    - Maximum Depth of Binary Tree
        
    - Same Tree
        
    - Invert Binary Tree
        
    - Symmetric Tree
        
2. Traversal:
    
    - Binary Tree Level Order Traversal
        
    - Right Side View
        
3. BST:
    
    - Validate BST
        
    - Kth Smallest Element in BST
        
4. Paths:
    
    - Path Sum
        
    - Path Sum II
        
    - Binary Tree Maximum Path Sum
        
5. Advanced:
    
    - Lowest Common Ancestor
        
    - Serialize and Deserialize Binary Tree
        
    - Vertical Order Traversal
        

A good mental model is:

**Traversal problems → DFS/BFS**  
**"Return something to parent" → Tree DP**  
**"Need relationship between nodes" → LCA/parent map**  
**"BST" → exploit ordering**

These four ideas cover most tree interview questions.