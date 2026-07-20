# 287. Find the Duplicate Number

## Problem Statement

Given an array of integers `nums` containing `n + 1` integers, where each integer is in the range:

```text
[1, n]
```

There is **exactly one repeated number** in the array. Return that duplicate number.

You must solve the problem **without modifying the array** and using **only constant extra space**.

---

## Examples

### Example 1

**Input**

```text
nums = [1,3,4,2,2]
```

**Output**

```text
2
```

---

### Example 2

**Input**

```text
nums = [3,1,3,4,2]
```

**Output**

```text
3
```

---

### Example 3

**Input**

```text
nums = [3,3,3,3,3]
```

**Output**

```text
3
```

---

## Constraints

```text
1 <= n <= 10^5
nums.length == n + 1
1 <= nums[i] <= n
All integers in nums appear exactly once except for one integer,
which appears two or more times.
```

---

## Follow-up

- How can you prove that at least one duplicate number must exist in `nums`?
- Can you solve the problem in **O(n)** time while using **O(1)** extra space?


```python
class Solution:
    '''
    Use the same concept of "DETECTING CYCLE IN LINKED LIST"
    '''
    def findDuplicate(self, arr: List[int]) -> int:
        slow, fast = arr[0], arr[0]
        slow, fast = arr[slow], arr[arr[fast]]

        while slow != fast:
            slow = arr[slow]
            fast = arr[arr[fast]]
        
        slow = arr[0]

        while slow != fast:
            slow = arr[slow]
            fast = arr[fast]
        
        return slow
```