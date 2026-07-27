# 1464. Maximum Product of Two Elements in an Array

## Problem Statement

Given an integer array `nums`, choose two **different** indices `i` and `j`.

Return the maximum value of:

```text
(nums[i] - 1) × (nums[j] - 1)
```

---

## Examples

### Example 1

**Input**

```text
nums = [3,4,5,2]
```

**Output**

```text
12
```

**Explanation**

```text
Choose i = 1 and j = 2.

(nums[1] - 1) × (nums[2] - 1)
= (4 - 1) × (5 - 1)
= 3 × 4
= 12
```

---

### Example 2

**Input**

```text
nums = [1,5,4,5]
```

**Output**

```text
16
```

**Explanation**

```text
Choose i = 1 and j = 3.

(nums[1] - 1) × (nums[3] - 1)
= (5 - 1) × (5 - 1)
= 4 × 4
= 16
```

---

### Example 3

**Input**

```text
nums = [3,7]
```

**Output**

```text
12
```

---

## Constraints

```text
2 <= nums.length <= 500
1 <= nums[i] <= 10^3
```

## Code 

### Brute Force : O(n^2)

```python
class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        for i in range(n-1):
            for j in range(i+1, n):
                ans = max(ans, (arr[i]-1) * (arr[j]-1))
        return ans
```

### Sorting : O(n log(n))

```python
class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        arr.sort()
        return (arr[-1] - 1) * (arr[-2] -1)
```

### Optimal : O(n)

```python
class Solution:
	'''
	Track the 'biggest' and 'second biggest' element
	'''
	def maxProduct(self, arr: List[int]) -> int:
		mx, smx = 0, 0
		for i in arr:
			if i > mx:
				smx = mx
				mx = i
			else:
				smx = max(smx, i)
		return (mx-1) * (smx-1)
```