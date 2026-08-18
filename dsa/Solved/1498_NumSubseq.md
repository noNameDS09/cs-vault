---
tags:
  - array
  - two-pointers
  - sorting
  - math
  - modulo
---

# 1498. Number of Subsequences That Satisfy the Given Sum Condition

## Problem Statement

You are given an array of integers `nums` and an integer `target`.

Return the number of non-empty subsequences such that:

```text
(min(subseq) + max(subseq)) <= target
```

Since the answer can be very large, return it modulo `10^9 + 7`.

---

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^6`
- `1 <= target <= 10^6`

---

## Examples

### Example 1

```text
nums = [3,5,6,7], target = 9
```

Output:

```text
4
```

---

### Example 2

```text
nums = [3,3,6,8], target = 10
```

Output:

```text
6
```

---

### Example 3

```text
nums = [2,3,3,4,6,7], target = 12
```

Output:

```text
61
```

---

## Intuition

Sort the array.

For a chosen minimum `nums[l]` and maximum `nums[r]`:

- If `nums[l] + nums[r] <= target`, then **all subsequences** using this `l` with any subset of elements from `(l+1 ... r)` will also satisfy the condition (because the maximum remains `<= nums[r]`).
- Otherwise, we must decrease the maximum (move `r` left).

---

## Approach

1. Sort `nums`.
2. Use two pointers `l` and `r`.
3. Precompute powers of 2 modulo `MOD`:
   - `power[k] = 2^k % MOD`
4. While `l <= r`:
   - If `nums[l] + nums[r] <= target`:
     - add `2^(r-l)` subsequences to answer
     - move `l++` (try a larger minimum)
   - else move `r--`.

---

## Code (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numSubseq(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        const int MOD = 1000000007;

        int n = (int)nums.size();

        vector<int> power(n);
        power[0] = 1;
        for (int i = 1; i < n; i++) {
            power[i] = (power[i - 1] * 2LL) % MOD;
        }

        long long ans = 0;
        int l = 0, r = n - 1;

        while (l <= r) {
            long long sum = (long long)nums[l] + nums[r];
            if (sum <= target) {
                ans = (ans + power[r - l]) % MOD;
                l++;
            } else {
                r--;
            }
        }

        return (int)ans;
    }
};
```

---

## Complexity Analysis

| Complexity | Value |
|-----------|-------|
| Time | **O(n log n)** (sorting) + **O(n)** (two pointers) |
| Space | **O(n)** |

---

## Key Takeaways

- Sorting + two pointers.
- When `min+max` is valid, count many subsequences at once using `2^(r-l)`.
- Modulo arithmetic for large counts.

