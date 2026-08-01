# 2095. Delete the Middle Node of a Linked List

## Problem Statement

You are given the head of a linked list.

Delete the **middle node** of the linked list and return the head of the modified list.

The middle node of a linked list of size `n` is the `⌊n / 2⌋`th node (using **0-based indexing**), where `⌊x⌋` denotes the greatest integer less than or equal to `x`.

For example:

```text
n = 1 → middle node = 0
n = 2 → middle node = 1
n = 3 → middle node = 1
n = 4 → middle node = 2
n = 5 → middle node = 2
```

---

## Examples

### Example 1

**Input**

```text
head = [1,3,4,7,1,2,6]
```

**Output**

```text
[1,3,4,1,2,6]
```

**Explanation**

```text
The linked list has 7 nodes.

The middle node is node 3 (value = 7).

After removing it, the list becomes:
[1,3,4,1,2,6]
```

---

### Example 2

**Input**

```text
head = [1,2,3,4]
```

**Output**

```text
[1,2,4]
```

**Explanation**

```text
The linked list has 4 nodes.

The middle node is node 2 (value = 3).

After removing it, the list becomes:
[1,2,4]
```

---

### Example 3

**Input**

```text
head = [2,1]
```

**Output**

```text
[2]
```

**Explanation**

```text
The linked list has 2 nodes.

The middle node is node 1 (value = 1).

After removing it, only node 0 remains.
```

---

## Constraints

```text
The number of nodes in the list is in the range [1, 10^5].
1 <= Node.val <= 10^5
```

## Code 

**Approach 1**

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	'''
	Common approach to store the values in the array and build the LL
	'''
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mp = {
            1: 0,
            2: 1,
            3: 1,
            4: 2,
            5: 2
        }

        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        if len(arr) < 6:
            arr.pop(mp[len(arr)])
        else:
            arr.pop(len(arr) // 2)
        if not arr:
            return None
        nhead = ListNode(arr[0])
        temp = nhead

        for i in arr[1:]:
            temp.next = ListNode(i)
            temp = temp.next
        return nhead           

```

**Approach 2**
Using `slow` and `fast` pointers
**Algorithm:**
	1. Use the `slow` and `fast` pointers to identify the middle node of LL
	2. Use the `prev` pointer to store the previous node
	3. Update the pointers as `prev.next = slow.next (mid.next)` 
	4. Return `head`

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        if not head.next:
            return None
        
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = slow.next
        return head
```