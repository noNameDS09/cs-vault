# 25. Reverse Nodes in k-Group

## Problem Statement

Given the head of a linked list, reverse the nodes of the list **k at a time**, and return the modified list.

- `k` is a positive integer and is less than or equal to the length of the linked list.
- If the number of nodes is **not a multiple of `k`**, the remaining nodes at the end should remain in their original order.
- You **may not modify the values** stored in the nodes. Only the **nodes themselves** may be rearranged.

Return the head of the modified linked list.

---

## Examples

### Example 1

**Input**

```text
head = [1,2,3,4,5]
k = 2
```

**Output**

```text
[2,1,4,3,5]
```

---

### Example 2

**Input**

```text
head = [1,2,3,4,5]
k = 3
```

**Output**

```text
[3,2,1,4,5]
```

---

## Constraints

```text
The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
```

---

## Follow-up

Can you solve the problem using **O(1)** extra memory?


# Naive Approach, Modify the values of nodes
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse(self, arr, start, end):
        while start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)    # Store all the values in array
            temp = temp.next
        
        for i in range(0, len(arr)-k+1, k): #reverse only k groups
            self.reverse(arr, i, i+k-1)
        
        temp = head
        for i in arr:
            temp.val = i
            temp = temp.next
        
        return head
```