# 416. Partition Equal Subset Sum

## Problem Statement

Given an integer array `nums`, determine whether it can be partitioned into **two subsets** such that the sum of the elements in both subsets is equal.

Return:

- `true` if such a partition exists.
- `false` otherwise.

---

## Examples

### Example 1

**Input**

```text
nums = [1,5,11,5]
```

**Output**

```text
true
```

**Explanation**

```text
The array can be partitioned into:

[1,5,5] and [11]

Both subsets have a sum of 11.
```

---

### Example 2

**Input**

```text
nums = [1,2,3,5]
```

**Output**

```text
false
```

**Explanation**

```text
The array cannot be partitioned into two subsets with equal sum.
```

---

## Constraints

```text
1 <= nums.length <= 200
1 <= nums[i] <= 100
```

## Intuition

```
1. solve(i, target) → bool
2. target == 0 → True
   i == n     → False
3. Skip → solve(i+1, target)
   Take → solve(i+1, target - nums[i])  only if nums[i] <= target
   Return True if EITHER choice returns True
```

## Code

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0:
            return False

        @cache
        def solve(i, target) -> bool:
            if target == 0:
                return True
            if i == n and target != 0:
                return False
            if target < 0:
                return False
            return solve(i+1, target - nums[i]) or solve(i+1, target)
        
        return solve(0, total//2)
```

```python
class Solution:
	def canPartition(self, nums: List[int]) -> bool:
		n = len(nums)
		total = sum(nums)
		if total % 2 != 0:   # if odd sum
			return False
		
		from funtools import cache
		
		@cache
		def solve(i, target) -> bool:
			if target == 0:
				return True
			if i == n:
				return False
			
			skip = solve(i+i, target)
			take = solve(i+i, target - nums[i]) if nums[i] <= target else False
			return skip or take
		
		return solve(0, total // 2)
```