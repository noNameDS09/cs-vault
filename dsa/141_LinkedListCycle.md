# 141. Linked List Cycle

## Problem Statement

Given the head of a linked list, determine whether the linked list contains a **cycle**.

A cycle exists if there is a node in the list that can be reached again by continuously following the `next` pointer.

> Internally, `pos` denotes the index of the node that the tail's `next` pointer connects to. It is used only for constructing the test cases and is **not** passed as a parameter.

Return:

- `true` if the linked list contains a cycle.
- `false` otherwise.

---

## Examples

### Example 1

**Input**

```text
head = [3,2,0,-4]
pos = 1
```

**Output**

```text
true
```

**Explanation**

```text
The tail connects to the node at index 1, creating a cycle.
```

---

### Example 2

**Input**

```text
head = [1,2]
pos = 0
```

**Output**

```text
true
```

**Explanation**

```text
The tail connects to the node at index 0, creating a cycle.
```

---

### Example 3

**Input**

```text
head = [1]
pos = -1
```

**Output**

```text
false
```

**Explanation**

```text
There is no cycle in the linked list.
```

---

## Constraints

```text
The number of nodes in the list is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
pos is -1 or a valid index in the linked list.
```

---

## Follow-up

Can you solve this problem using **O(1)** (constant) extra memory?

# Answer 
# 1. Using set
Use the ```set``` to track the visited nodes.
If the node is encountered again it is found in the ```set```.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        while head:
            if head in visited:
                return True

            visited.add(head)
            head = head.next

        return False
```

# Better approach using two pointers (slow and fast)
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
```