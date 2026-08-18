---
tags:
  - linked-list
  - two-pointers
---

# 19. Remove Nth Node From End of List

## Problem Statement

Given the head of a linked list and an integer `n`, remove the **nth node from the end** of the list and return the head of the modified list.

---

## Examples

### Example 1

**Input**

```text
head = [1,2,3,4,5]
n = 2
```

**Output**

```text
[1,2,3,5]
```

---

### Example 2

**Input**

```text
head = [1]
n = 1
```

**Output**

```text
[]
```

---

### Example 3

**Input**

```text
head = [1,2]
n = 1
```

**Output**

```text
[1]
```

---

## Constraints

```text
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
```

---

## Follow-up

Can you solve this problem in **one pass**?



```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total = 0
        temp = head

        while temp:
            total += 1
            temp = temp.next
        
        if n == total:
            return head.next
        
        steps = total - n - 1
        temp = head

        while steps:
            steps -= 1
            temp = temp.next
        
        temp.next = temp.next.next
        return head
```