A **binary tree** is one of the most important data structures in computer science. It is widely used in searching, sorting, databases, file systems, compilers, and AI. Learning binary trees also makes it much easier to understand more advanced structures like Binary Search Trees (BSTs), AVL Trees, Red-Black Trees, and Heaps.

I'll teach it from the ground up using Python.

---

# 1. What is a Binary Tree?

A binary tree is a hierarchical data structure where:

* Each node stores a value.
* Each node can have **at most two children**:

  * Left child
  * Right child

Example:

```
        10
       /  \
      5    20
     / \     \
    3   7     30
```

Here,

* 10 is the root.
* 5 is the left child of 10.
* 20 is the right child of 10.
* 3 and 7 are children of 5.

---

# 2. Terminology

Consider this tree:

```
        A
      /   \
     B     C
    / \   /
   D   E F
```

### Root

Topmost node.

```
A
```

---

### Parent

Node having children.

```
A is parent of B and C
```

---

### Child

Node connected below another node.

```
B is child of A
```

---

### Leaf Node

Node with no children.

```
D E F C's right child(None)

Leaves:
D
E
F
```

---

### Internal Node

Node having at least one child.

```
A
B
C
```

---

### Edge

Connection between nodes.

```
A ---- B
```

---

### Depth

Distance from root.

```
A depth = 0

B depth = 1

D depth = 2
```

---

### Height

Longest path from node to leaf.

```
Height of D = 0

Height of B = 1

Height of A = 2
```

---

# 3. Creating a Binary Tree in Python

The most common implementation uses a class.

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

Now create nodes.

```python
root = TreeNode(10)

root.left = TreeNode(5)
root.right = TreeNode(20)

root.left.left = TreeNode(3)
root.left.right = TreeNode(7)

root.right.right = TreeNode(30)
```

The tree becomes

```
        10
       /  \
      5    20
     / \     \
    3   7     30
```

---

# 4. Visualizing the Memory

```
root
  |
  v
+--------+
| value=10
| left -----> Node(5)
| right ----> Node(20)
+--------+
```

Each child is itself another `TreeNode`.

---

# 5. Types of Binary Trees

## Full Binary Tree

Every node has either

* 0 children
* 2 children

Example

```
      A
     / \
    B   C
   / \
  D   E
```

---

## Perfect Binary Tree

All internal nodes have 2 children.

All leaves are at the same level.

```
        A
      /   \
     B     C
    / \   / \
   D  E  F  G
```

---

## Complete Binary Tree

Every level is completely filled except maybe the last.

Last level is filled left to right.

```
       A
      / \
     B   C
    / \  /
   D  E F
```

---

## Balanced Binary Tree

Height difference between left and right subtree is small (typically ≤1 for AVL trees).

Searching is efficient.

---

## Degenerate Tree

Looks like a linked list.

```
A
 \
  B
   \
    C
     \
      D
```

Very inefficient.

---

# 6. Tree Traversals

Traversal means visiting every node.

There are four major traversals.

---

# A. Inorder Traversal

Order:

```
Left

Root

Right
```

Tree

```
      10
     /  \
    5    20
   / \     \
  3   7     30
```

Visit

```
3

5

7

10

20

30
```

Python

```python
def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.value)
    inorder(node.right)
```

---

# B. Preorder Traversal

Order

```
Root

Left

Right
```

Output

```
10

5

3

7

20

30
```

Python

```python
def preorder(node):
    if node is None:
        return

    print(node.value)
    preorder(node.left)
    preorder(node.right)
```

---

# C. Postorder Traversal

Order

```
Left

Right

Root
```

Output

```
3

7

5

30

20

10
```

Python

```python
def postorder(node):
    if node is None:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.value)
```

---

# D. Level Order Traversal

Visits nodes level by level.

```
10

5 20

3 7 30
```

Python

```python
from collections import deque

def level_order(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.value)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)
```

This uses a **queue**, making it a breadth-first search (BFS).

---

# 7. Searching in a Binary Tree

Since a regular binary tree has no ordering, search every node.

```python
def search(root, target):
    if root is None:
        return False

    if root.value == target:
        return True

    return search(root.left, target) or search(root.right, target)
```

Time Complexity

```
O(n)
```

---

# 8. Counting Nodes

```python
def count_nodes(root):
    if root is None:
        return 0

    return 1 + count_nodes(root.left) + count_nodes(root.right)
```

Example

```
6 nodes
```

---

# 9. Sum of Nodes

```python
def tree_sum(root):
    if root is None:
        return 0

    return root.value + tree_sum(root.left) + tree_sum(root.right)
```

---

# 10. Height of Tree

```python
def height(root):
    if root is None:
        return -1

    return 1 + max(height(root.left), height(root.right))
```

For

```
      10
     /  \
    5    20
   / \     \
  3   7     30
```

Height

```
2
```

---

# 11. Counting Leaf Nodes

```python
def leaf_count(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    return leaf_count(root.left) + leaf_count(root.right)
```

Output

```
3
```

Leaves

```
3
7
30
```

---

# 12. Mirror of Tree

Original

```
      10
     /  \
    5    20
```

Mirror

```
      10
     /  \
   20    5
```

Python

```python
def mirror(root):
    if root is None:
        return

    root.left, root.right = root.right, root.left

    mirror(root.left)
    mirror(root.right)
```

---

# 13. Time Complexities

| Operation             | Time                |
| --------------------- | ------------------- |
| Search                | O(n)                |
| Insert (general tree) | Depends on strategy |
| Traversal             | O(n)                |
| Count nodes           | O(n)                |
| Height                | O(n)                |
| Mirror                | O(n)                |

---

# 14. Recursive Thinking

Almost every binary tree algorithm follows this pattern:

```python
def solve(node):

    if node is None:
        return

    solve(node.left)

    # process node

    solve(node.right)
```

This works because every subtree is itself a binary tree.

---

# 15. Common Interview Problems

Once you're comfortable with the basics, these are common problems to practice:

1. Height of a binary tree
2. Diameter of a binary tree
3. Maximum depth
4. Minimum depth
5. Check if two trees are identical
6. Check if a tree is symmetric
7. Lowest Common Ancestor (LCA)
8. Zigzag traversal
9. Left view and right view
10. Boundary traversal
11. Vertical order traversal
12. Top view and bottom view
13. Maximum path sum
14. Serialize and deserialize a tree
15. Invert (mirror) a binary tree

---

# 16. Binary Tree vs. Binary Search Tree (BST)

A **binary tree** and a **binary search tree** are not the same.

A regular binary tree has **no ordering rule**:

```
      10
     /  \
   50     3
```

This is a valid binary tree.

A **BST** must satisfy:

* All values in the left subtree are smaller than the node.
* All values in the right subtree are larger than the node.

Example:

```
       10
      /  \
     5    20
    / \   / \
   2   7 15 30
```

Because of this ordering, searching in a balanced BST is much faster—typically **O(log n)** instead of **O(n)**.

---

## Complete Example

```python
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.value, end=" ")
    inorder(node.right)

def height(node):
    if node is None:
        return -1
    return 1 + max(height(node.left), height(node.right))

# Build tree
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(30)

print("Inorder traversal:")
inorder(root)          # 3 5 7 10 20 30

print("\nHeight:", height(root))  # 2
```

### Learning roadmap

To build strong skills with trees, follow this sequence:

1. Understand binary tree terminology and node structure.
2. Learn recursion thoroughly.
3. Master the four traversals: inorder, preorder, postorder, and level order.
4. Practice basic operations: search, count nodes, compute height, count leaves, and mirror a tree.
5. Move on to Binary Search Trees (BSTs), where insertion, deletion, and efficient searching are introduced.
6. Finally, study advanced trees like AVL Trees, Red-Black Trees, Heaps, and Tries.

A solid understanding of binary trees and recursion forms the foundation for many data structures and algorithms you'll encounter in coding interviews and real-world software development.
