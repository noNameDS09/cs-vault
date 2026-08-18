---
tags:
  - linked-list
  - recursion
  - two-pointers
---

# 206. Reverse Linked List

## Problem Statement

Given the head of a **singly linked list**, reverse the linked list and return the head of the reversed list.

**Follow-up:** Can you solve the problem using both an **iterative** and a **recursive** approach?

---

## Examples

### Example 1

**Input**

```text
head = [1,2,3,4,5]
```

**Output**

```text
[5,4,3,2,1]
```

---

### Example 2

**Input**

```text
head = [1,2]
```

**Output**

```text
[2,1]
```

---

### Example 3

**Input**

```text
head = []
```

**Output**

```text
[]
```

---

## Constraints

```text
The number of nodes in the list is in the range [0, 5000].
-5000 <= Node.val <= 5000
```

---

## Follow-up

Can you reverse the linked list using:

- **Iterative approach**
- **Recursive approach**

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
```