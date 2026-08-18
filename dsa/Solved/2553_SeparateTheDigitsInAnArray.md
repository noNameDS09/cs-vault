---
tags:
  - array
  - math
---

# [2553. Separate the Digits in an Array](https://leetcode.com/problems/separate-the-digits-in-an-array/)

## Problem Statement

Given an array of positive integers `nums`, return an array `answer` that consists of the digits of each integer in `nums` after separating them in the same order they appear.

Separating the digits of an integer means extracting all of its digits while preserving their order.

For example:

```text
10921 → [1,0,9,2,1]
```

Return the concatenation of the separated digits of every integer in `nums`.

---

## Examples

### Example 1

**Input**

```text
nums = [13,25,83,77]
```

**Output**

```text
[1,3,2,5,8,3,7,7]
```

**Explanation**

```text
13 → [1,3]
25 → [2,5]
83 → [8,3]
77 → [7,7]

answer = [1,3,2,5,8,3,7,7]
```

---

### Example 2

**Input**

```text
nums = [7,1,3,9]
```

**Output**

```text
[7,1,3,9]
```

**Explanation**

```text
Each number consists of a single digit.

Therefore, the answer is:
[7,1,3,9]
```

---

## Constraints

```text
1 <= nums.length <= 1000
1 <= nums[i] <= 10^5
```

## Code

```python
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []

        for i in nums:
            temp = []
            while i>0:
                temp.append(i%10)
                i = i // 10
            for ele in temp[::-1]:
                ans.append(ele)
        return ans
```

```python
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            for d in str(num):
                ans.append(int(d))
        
        return ans
```