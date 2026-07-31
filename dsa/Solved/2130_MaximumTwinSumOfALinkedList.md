# 2130. Maximum Twin Sum of a Linked List

## Problem Statement

In a linked list of even length `n`, the `i`th node (0-indexed) is the **twin** of the `(n - 1 - i)`th node, where:

```text
0 <= i <= (n / 2) - 1
```

For example, if `n = 4`:

- Node `0` is the twin of node `3`.
- Node `1` is the twin of node `2`.

The **twin sum** is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the **maximum twin sum** of the linked list.

---

## Examples

### Example 1

**Input**

```text
head = [5,4,2,1]
```

**Output**

```text
6
```

**Explanation**

```text
Node 0 and node 3 have twin sum = 5 + 1 = 6.
Node 1 and node 2 have twin sum = 4 + 2 = 6.

The maximum twin sum is 6.
```

---

### Example 2

**Input**

```text
head = [4,2,2,3]
```

**Output**

```text
7
```

**Explanation**

```text
Node 0 and node 3 have twin sum = 4 + 3 = 7.
Node 1 and node 2 have twin sum = 2 + 2 = 4.

The maximum twin sum is 7.
```

---

### Example 3

**Input**

```text
head = [1,100000]
```

**Output**

```text
100001
```

**Explanation**

```text
There is only one pair of twins.

Twin sum = 1 + 100000 = 100001.
```

---

## Constraints

```text
The number of nodes in the list is an even integer in the range [2, 10^5].
1 <= Node.val <= 10^5
```

## Code

One solution is to store the node values in the array and use the two pointers for obtaining the answer

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        while head:
	        arr.append(head.val)
	        head = head.next
	    
	    i, j = 0 , len(arr)-1
	    
	    ans = 0
	    while i < j:
		    ans = max(ans, arr[i] + arr[j])
		    i += 1
		    j -= 1
		    
        return ans
```

Another approach is to traverse in the linked like in reverse fashion for the half.
**Algorithm:**
	1. Find the middle node
	2. Reverse the second half of the list (mid to last node)
	3. Use two pointers to obtain the answer

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
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

    def pairSum(self, head: Optional[ListNode]) -> int:
        temp = head
        mid = self.findMiddle(temp)
        new = self.reverse(mid)

        ans = 0
        temp2 = new
        temp = head
        while(temp2):
            ans = max(ans, temp.val + temp2.val)
            temp = temp.next
            temp2 = temp2.next
        return ans
```