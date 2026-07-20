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

### Optimal Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverse(self, head, last):
        """
        Reverse the linked list segment from 'head' up to (but not including) 'last'.

        Example:
            head -> 1 -> 2 -> 3 -> last(4)

        After reversal:
            3 -> 2 -> 1 -> 4

        Returns:
            (new_head, new_tail)
        """
        prev = last
        curr = head

        while curr != last:
            # Save the next node before changing the link
            nxt = curr.next

            # Reverse the current node's pointer
            curr.next = prev

            # Move both pointers one step ahead
            prev = curr
            curr = nxt

        # 'prev' is the new head of the reversed segment.
        # Original 'head' becomes the tail.
        return prev, head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # No reversal needed
        if not head or k == 1:
            return head

        # Dummy node simplifies handling the first group
        dummy = ListNode(0)
        dummy.next = head

        # Points to the tail of the previously processed group
        prev_tail = dummy

        # Current group's head
        curr = head

        while curr:

            # Check if there are at least k nodes remaining
            temp = curr
            count = 0

            while count < k and temp:
                temp = temp.next
                count += 1

            # Fewer than k nodes remain -> leave them unchanged
            if count < k:
                break

            # Reverse the current group
            # new_head = head of reversed group
            # new_tail = tail of reversed group (original curr)
            new_head, new_tail = self.reverse(curr, temp)

            # Connect previous group to the reversed group
            prev_tail.next = new_head

            # Move prev_tail to the end of the reversed group
            prev_tail = new_tail

            # Start processing the next group
            curr = temp

        return dummy.next
```