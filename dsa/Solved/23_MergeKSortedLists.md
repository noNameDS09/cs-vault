# 23. Merge k Sorted Lists

## Problem Statement

You are given an array `lists` of `k` linked lists, where each linked list is sorted in **ascending order**.

Merge all the linked lists into one **sorted linked list** and return its head.

---

## Examples

### Example 1

**Input**

```text
lists = [[1,4,5],[1,3,4],[2,6]]
```

**Output**

```text
[1,1,2,3,4,4,5,6]
```

**Explanation**

The input linked lists are:

```text
[
  1 → 4 → 5,
  1 → 3 → 4,
  2 → 6
]
```

After merging them into one sorted linked list:

```text
1 → 1 → 2 → 3 → 4 → 4 → 5 → 6
```

---

### Example 2

**Input**

```text
lists = []
```

**Output**

```text
[]
```

---

### Example 3

**Input**

```text
lists = [[]]
```

**Output**

```text
[]
```

---

## Constraints

```text
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of all lists[i].length will not exceed 10^4.
```

# This is the most common solution that comes to our mind after seeing. Time: O(N log(N)), Space: O(N)
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        1. Store all the elements in the array : Space -> O(N)
        2. Sort them : Time -> O(N log(N))
        3. Create a new Linked List and append elements of the array one by one
        4. Return the head of the linked list
        '''
        l = []
        
        for i in lists:
            temp = i
            while temp:
                # print(temp.val)
                l.append(temp.val)
                temp = temp.next
        
        l = sorted(l)

        head = ListNode()
        temp = head
        
        for i in l:
            curr = ListNode(i)
            temp.next = curr
            temp = temp.next

        return head.next
```

# Optimal solution is using the min-heap. Time (N log(K))
### Algorithm

1. Push the head of each non-empty list into a min-heap.
2. Repeatedly:
   - Pop the smallest node.
   - Append it to the result list.
   - If the popped node has a next node, push that into the heap.
3. Continue until the heap is empty.
```python
import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []   # Create a min-heap

        for i, node in enumerate(lists): # Store the head nodes of all the lists
            if node:
                heapq.heappush(heap, (node.val, i, node))

        head = ListNode()
        temp = head

        while heap:
            val, i, node = heapq.heappop(heap)  # pop the smallest node

            temp.next = node    # append it to the results
            temp = temp.next

            if node.next:   # if next node exists then push to heap
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return head.next
```