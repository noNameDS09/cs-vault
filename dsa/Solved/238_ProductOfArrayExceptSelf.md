---
tags:
  - array
  - prefix-sum
---

# 238. Product of Array Except Self

## Problem Statement

Given an integer array `nums`, return an array `answer` such that:

```text
answer[i] = product of all elements of nums except nums[i]
```

### Constraints

- Do **not** use the division operator.
- The algorithm must run in **O(n)** time.
- The product of any prefix or suffix fits in a **32-bit integer**.

---

## Examples

### Example 1

**Input**

```text
nums = [1,2,3,4]
```

**Output**

```text
[24,12,8,6]
```

---

### Example 2

**Input**

```text
nums = [-1,1,0,-3,3]
```

**Output**

```text
[0,0,9,0,0]
```

---

## Constraints

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The answer is guaranteed to fit in a **32-bit integer**.

---

## Follow-up

Can you solve it in **O(1)** extra space?

> **Note:** The output array does **not** count as extra space.

---

# Intuition

For every index `i`, we need:

```text
Product of all elements except nums[i]
```

Instead of multiplying every other element for each index (**O(n²)**), we precompute:

- **Left Product:** Product of all elements before index `i`
- **Right Product:** Product of all elements after index `i`

Then,

```text
answer[i] = left[i] × right[i]
```

This satisfies:

- No division
- Linear time

---

# Approach

## Step 1: Build Left Product Array

`left[i]` stores the product of all elements before index `i`.

Example:

```text
nums  = [1,2,3,4]

left:

Index 0 -> 1
Index 1 -> 1
Index 2 -> 1×2 = 2
Index 3 -> 1×2×3 = 6

left = [1,1,2,6]
```

---

## Step 2: Build Right Product Array

`right[i]` stores the product of all elements after index `i`.

```text
nums = [1,2,3,4]

right:

Index 3 -> 1
Index 2 -> 4
Index 1 -> 3×4 = 12
Index 0 -> 2×3×4 = 24

right = [24,12,4,1]
```

---

## Step 3: Multiply Left and Right

```text
answer[i] = left[i] × right[i]
```

Example:

| Index | Left | Right | Answer |
|------:|-----:|------:|-------:|
| 0 | 1 | 24 | 24 |
| 1 | 1 | 12 | 12 |
| 2 | 2 | 4 | 8 |
| 3 | 6 | 1 | 6 |

Final Answer:

```text
[24,12,8,6]
```

---

# Dry Run

### Input

```text
nums = [1,2,3,4]
```

### Build Left

| i | left |
|---|------|
|0|1|
|1|1|
|2|2|
|3|6|

```text
left = [1,1,2,6]
```

---

### Build Right

| i | right |
|---|-------|
|3|1|
|2|4|
|1|12|
|0|24|

```text
right = [24,12,4,1]
```

---

### Final Multiplication

```text
left  = [1,1,2,6]
right = [24,12,4,1]

result:

1×24 = 24
1×12 = 12
2×4  = 8
6×1  = 6
```

Final Output

```text
[24,12,8,6]
```

---

# Code

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        left = [1] * n
        right = [1] * n

        # Build left products
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        # Build right products
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        # Compute final answer
        result = []

        for i in range(n):
            result.append(left[i] * right[i])

        return result
```

---

# Complexity Analysis

| Complexity | Value |
|------------|-------|
| **Time** | **O(n)** |
| **Space** | **O(n)** |

Reason:

- One pass for `left`
- One pass for `right`
- One pass for `result`

Total:

```text
O(n) + O(n) + O(n) = O(n)
```

---

# Follow-up: O(1) Extra Space

We can optimize the solution by:

1. Using the output array to store the left products.
2. Traversing from the right while maintaining a running suffix product.
3. Multiplying the suffix product into the output array.

This removes the need for the separate `left` and `right` arrays.

- **Time:** `O(n)`
- **Extra Space:** `O(1)` (excluding the output array)

---

# Key Takeaways

- No division is used.
- Prefix (left) and suffix (right) products avoid repeated computation.
- Each element is processed a constant number of times.
- Easily optimized from **O(n)** extra space to **O(1)** extra space.