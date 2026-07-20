# 21. Merge Two Sorted Lists

## Problem Statement

You are given the heads of two **sorted linked lists**, `list1` and `list2`.

Merge the two lists into one **sorted linked list** by splicing together the nodes of the two input lists.

Return the head of the merged linked list.

---

## Examples

### Example 1

**Input**

```text
list1 = [1,2,4]
list2 = [1,3,4]
```

**Output**

```text
[1,1,2,3,4,4]
```

---

### Example 2

**Input**

```text
list1 = []
list2 = []
```

**Output**

```text
[]
```

---

### Example 3

**Input**

```text
list1 = []
list2 = [0]
```

**Output**

```text
[0]
```

---

## Constraints

```text
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
```

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next
        
        curr.next = list1 if list1 else list2  #attach remaining nodes

        return head.next
```