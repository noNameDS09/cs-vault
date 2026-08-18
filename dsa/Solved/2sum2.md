---
tags:
  - array
  - two-pointers
  - binary-search
---

# 167. Two Sum II - Input Array Is Sorted

## Problem Statement

Given an array of integers `numbers` that is already **sorted in non-decreasing order** and an integer `target`, return **indices of the two numbers** such that they add up to `target`.

Return the answer as a pair of integers `[index1, index2]` where:

- `index1` and `index2` are **1-based**.
- `index1 < index2`.

You may assume that **exactly one solution** exists.

---

## Constraints

- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted.
- `-1000 <= target <= 1000`

---

## Examples

### Example 1

**Input**

```text
numbers = [2,7,11,15], target = 9
```

**Output**

```text
[1,2]
```

**Explanation**

`numbers[1] + numbers[2] = 2 + 7 = 9`.

---

## Approach

Because the array is sorted, we can use a **two-pointer** strategy.

- Let `i` start at the beginning.
- Let `j` start at the end.

At each step, compute:

```text
sum = numbers[i] + numbers[j]
```

- If `sum == target` → we found the pair.
- If `sum < target` → move `i` right to increase the sum.
- If `sum > target` → move `j` left to decrease the sum.

---

## Dry Run

For `numbers = [2,7,11,15]`, `target = 9`:

| i | j | numbers[i] | numbers[j] | sum | action |
|---:|---:|------------:|------------:|----:|--------|
| 0 | 3 | 2 | 15 | 17 | sum too big → j-- |
| 0 | 2 | 2 | 11 | 13 | sum too big → j-- |
| 0 | 1 | 2 | 7 | 9 | found |

Answer (1-based) = `[1,2]`.

---

## Code

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i = 0, j = (int)numbers.size() - 1;

        while (i < j) {
            int sum = numbers[i] + numbers[j];
            if (sum == target) return {i + 1, j + 1};
            else if (sum < target) i++;
            else j--;
        }

        return {0, 0}; // should never reach for valid inputs
    }
};
```

---

## Complexity Analysis

| Complexity | Value |
|-----------|-------|
| Time | **O(n)** |
| Space | **O(1)** |

---

## Key Takeaways

- Sorting enables two-pointer traversal.
- Each pointer moves inward at most once.
- Produces the required **1-based** indices.

