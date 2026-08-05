# [3731. Find Missing Elements](https://leetcode.com/problems/find-missing-elements/)

You are given an integer array `nums` consisting of **unique** integers.

Originally, `nums` contained **every integer** within a certain range. However, some integers may have gone missing.

The **smallest** and **largest** integers of the original range are still present in `nums`.

Return a **sorted list** of all the missing integers in this range. If no integers are missing, return an empty list.

---

## Examples

### Example 1

**Input**

```text
nums = [1,4,2,5]
```

**Output**

```text
[3]
```

**Explanation**

```text
The smallest integer is 1 and the largest is 5.

The complete range is:
[1,2,3,4,5]

The missing integer is:
[3]
```

---

### Example 2

**Input**

```text
nums = [7,8,6,9]
```

**Output**

```text
[]
```

**Explanation**

```text
The smallest integer is 6 and the largest is 9.

The complete range is:
[6,7,8,9]

No integers are missing.
```

---

### Example 3

**Input**

```text
nums = [5,1]
```

**Output**

```text
[2,3,4]
```

**Explanation**

```text
The smallest integer is 1 and the largest is 5.

The complete range is:
[1,2,3,4,5]

The missing integers are:
[2,3,4]
```

---

## Constraints

```text
2 <= nums.length <= 100
1 <= nums[i] <= 100
nums consists of unique integers.
```

## Code

### **Approach 1: Brute Force O(n<sup>2</sup>)**

```python
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        
        mn = min(nums)
        mx = max(nums)

        for i in range(mn, mx):
            if i not in nums:
                ans.append(i)
        
        return ans
```

### **Approach 2: Sort and search using binary search** O(n log(n))

```python
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        from bisect import bisect_left
        ans = []
        nums.sort()
        n = len(nums)
        
        mn = min(nums)
        mx = max(nums)

        for i in range(mn, mx):
            idx = bisect_left(nums, i) # Binary search 
            if idx == len(nums) or nums[idx] != i:
                ans.append(i)
        
        return ans
```