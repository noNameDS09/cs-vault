---
tags:
  - array
  - dynamic-programming
  - divide-and-conquer
  - kadane
---

# 53. Maximum Subarray

- **Difficulty:** 🟡 Medium
- **Status:** ✅ Solved

## 📝 Problem Statement

Given an integer array `nums`, find the **contiguous subarray** with the **largest sum**, and return its sum.

---

## 📌 Examples

### Example 1

**Input**
```text
nums = [-2,1,-3,4,-1,2,1,-5,4]
```

**Output**
```text
6
```

**Explanation**

The subarray:

```text
[4, -1, 2, 1]
```

has the largest sum:

```text
4 + (-1) + 2 + 1 = 6
```

---

### Example 2

**Input**
```text
nums = [1]
```

**Output**
```text
1
```

**Explanation**

The only subarray is:

```text
[1]
```

So the maximum subarray sum is **1**.

---

### Example 3

**Input**
```text
nums = [5,4,-1,7,8]
```

**Output**
```text
23
```

**Explanation**

The entire array forms the maximum subarray:

```text
[5, 4, -1, 7, 8]
```

Sum:

```text
5 + 4 - 1 + 7 + 8 = 23
```

---

## 📋 Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

---

## ⭐ Follow-up

After solving it in **O(n)** time, try implementing the **Divide and Conquer** approach, which is more subtle.

---

# 💡 Approach (Kadane's Algorithm)

### Idea

At every index, we have two choices:

1. Start a **new subarray** from the current element.
2. Extend the **previous subarray**.

So,

```python
curr = max(nums[i], curr + nums[i])
```

Keep track of the maximum sum seen so far.

---

## 🧠 Algorithm

1. Initialize:
   - `curr = nums[0]`
   - `ans = nums[0]`
2. Traverse the array from index `1`.
3. Update the current maximum ending at index `i`.
4. Update the global maximum.
5. Return `ans`.

---

## ✅ Python Solution

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = curr = nums[0]
        n = len(nums)

        for i in range(1, n):
            curr = max(nums[i], curr + nums[i])
            ans = max(ans, curr)

        return ans
```

---

## ⏱ Complexity Analysis

| Complexity | Value |
|------------|-------|
| Time | **O(n)** |
| Space | **O(1)** |

---

## 🔑 Key Insight

`curr` always stores the **maximum subarray sum ending at the current index**.

If extending the previous subarray becomes worse than starting fresh, we simply begin a new subarray.

This greedy observation makes **Kadane's Algorithm** one of the most elegant **O(n)** solutions for maximum subarray problems.