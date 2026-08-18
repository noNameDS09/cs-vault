---
tags:
  - linked-list
  - math
  - recursion
---

# 2. Add Two Numbers

## Problem Statement

You are given two **non-empty linked lists** representing two non-negative integers.

The digits are stored in **reverse order**, and each node contains a single digit.

Add the two numbers and return the sum as a linked list.

You may assume that the two numbers do **not** contain any leading zeros, except the number `0` itself.

---

## Examples

### Example 1

**Input**

```text
l1 = [2,4,3]
l2 = [5,6,4]
```

**Output**

```text
[7,0,8]
```

**Explanation**

```text
342 + 465 = 807
```

---

### Example 2

**Input**

```text
l1 = [0]
l2 = [0]
```

**Output**

```text
[0]
```

---

### Example 3

**Input**

```text
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
```

**Output**

```text
[8,9,9,9,0,0,0,1]
```

---

## Constraints

```text
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the linked list represents a number with no leading zeros, except for the number 0 itself.
```

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = 0, 0

        i = 1 # counter for multiples in 1, 10, 100, ...

        while l1:
            n1 += l1.val * i
            i *= 10
            l1 = l1.next

        i = 1
        while l2:
            n2 += l2.val * i
            i *= 10
            l2 = l2.next
        
        n1 += n2
        
        if not n1: # if total is 0 return 0
            return ListNode(0)
        
        ans = ListNode()
        temp = ans
        
        while n1:
            curr = ListNode(n1 % 10)
            n1 = n1 // 10
            temp.next = curr
            temp = curr
        
        return ans.next
```