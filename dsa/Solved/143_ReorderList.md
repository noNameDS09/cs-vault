---
tags:
  - linked-list
  - two-pointers
  - stack
  - recursion
---

# 143. Reorder List

## Problem Statement

You are given the head of a **singly linked list** represented as:

```text
L0 → L1 → … → Ln-1 → Ln
```

Reorder the list into the following pattern:

```text
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
```

You **may not modify the values** stored in the nodes. Only the **links between nodes** may be changed.

---

## Examples

### Example 1

**Input**

```text
head = [1,2,3,4]
```

**Output**

```text
[1,4,2,3]
```

---

### Example 2

**Input**

```text
head = [1,2,3,4,5]
```

**Output**

```text
[1,5,2,4,3]
```

---

## Constraints

```text
The number of nodes in the list is in the range [1, 5 × 10^4].
1 <= Node.val <= 1000
```

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Algorithm:
    1. Find the middle element to reverse the list
    2. Reverse the list
    3. Apply the logic
    '''
    def findMiddle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        return slow
    
    def reverse(self, head):
        new = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = new
            new = curr
            curr = nxt
        
        return new

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        middle = self.findMiddle(head)
        revHead = self.reverse(middle)

        currH = head

        while revHead.next:
            tempCurr = currH.next
            currH.next = revHead

            tempRev = revHead.next
            revHead.next = tempCurr

            currH = tempCurr
            revHead = tempRev
        
        return head

```