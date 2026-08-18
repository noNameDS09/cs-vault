---
tags:
  - linked-list
  - hash-table
  - deep-copy
---

# 138. Copy List with Random Pointer

## Problem Statement

A linked list of length `n` is given such that each node contains an additional **random** pointer, which can point to any node in the list or `null`.

Construct a **deep copy** of the linked list.

The deep copy should consist of exactly `n` brand new nodes, where:

- Each new node has the same value as its corresponding original node.
- Both the `next` and `random` pointers should point to **new nodes** in the copied list.
- None of the pointers in the copied list should point to any node in the original list.

For example, if an original node `X.random` points to node `Y`, then in the copied list, the corresponding node `x.random` should point to the copied node `y`.

Return the head of the deep-copied linked list.

The linked list is represented as a list of nodes, where each node is represented as:

```text
[val, random_index]
```

where:

- `val` is the value of the node.
- `random_index` is the index of the node pointed to by the `random` pointer, or `null` if there is no such pointer.

> Your function is only given the head of the original linked list.

---

## Examples

### Example 1

**Input**

```text
head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

**Output**

```text
[[7,null],[13,0],[11,4],[10,2],[1,0]]
```

---

### Example 2

**Input**

```text
head = [[1,1],[2,1]]
```

**Output**

```text
[[1,1],[2,1]]
```

---

### Example 3

**Input**

```text
head = [[3,null],[3,0],[3,null]]
```

**Output**

```text
[[3,null],[3,0],[3,null]]
```

---

## Constraints

```text
0 <= n <= 1000
-10^4 <= Node.val <= 10^4
Node.random is null or points to some node in the linked list.
```

---

# Approach 1: Hash Map (Most Intuitive)

## Idea

As you create copies of the original nodes, maintain a mapping:

```text
Original Node  →  Copied Node
```

This allows you to instantly find the copied version of any original node while reconstructing the `next` and `random` pointers.

---

## Pass 1: Copy All Nodes

Traverse the original linked list.

For each node:

- Create a new node with the same value.
- Store the mapping in a hash map.
- Do **not** assign the `next` or `random` pointers yet.

### Example

Original List

```text
A → B → C
```

Hash Map

```text
A → A'
B → B'
C → C'
```

---

## Pass 2: Connect the Pointers

Traverse the original list again.

For each original node:

```text
copied.next = map[original.next]
copied.random = map[original.random]
```

Since every original node already has a copied version, both pointers can be assigned directly.

Finally, return:

```text
map[head]
```

---

## Why Does This Work?

The challenging part is the `random` pointer because it can:

- Point to a node ahead in the list.
- Point to a previous node.
- Point to itself.
- Be `null`.

The hash map provides constant-time access to the copied version of any original node, regardless of where the `random` pointer points.

---

## Complexity Analysis

```text
Time Complexity : O(n)
Space Complexity: O(n)
```

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head

        mp = {} # Create a map 

        curr = head

        while curr:
            mp[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head

        while curr:
            mp[curr].next = mp.get(curr.next)
            mp[curr].random = mp.get(curr.random)
            curr = curr.next
        
        return mp[head]
```