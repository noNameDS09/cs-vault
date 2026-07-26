# 628. Maximum Product of Three Numbers

## Problem Statement

Given an integer array `nums`, find three numbers whose product is maximum and return the maximum product.

---

## Examples

### Example 1

**Input**

```text
nums = [1,2,3]
```

**Output**

```text
6
```

---

### Example 2

**Input**

```text
nums = [1,2,3,4]
```

**Output**

```text
24
```

---

### Example 3

**Input**

```text
nums = [-1,-2,-3]
```

**Output**

```text
-6
```

---

## Constraints

```text
3 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000
```

## Code

```python
class Solution:
	'''
	Sort array first: Time -> O(N log(N)) 
	Case 1 : All are +ve -> return maximum product
	Case 2 : Negative numbers -> maximum should be product of first two numbers and last number 
	eg. [-10, -10, 5, 2]
    Case 1 = 5 * 2 * (-10) = -100
    Case 2 = (-10) * (-10) * 5 = 500 (Maximum)
	'''
    def maximumProduct(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()

        ans1 = arr[-1] * arr[-2] * arr[-3]
        ans2 = arr[0] * arr[1] * arr[-1]

        return max(ans1, ans2)
```

