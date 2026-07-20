# 2963. Count the Number of Good Partitions

## Problem Statement

You are given a 0-indexed array of positive integers `nums`.

A partition of `nums` into one or more contiguous subarrays is called **good** if:

> No two subarrays contain the same number.

Return the **total number of good partitions** of `nums` modulo `10^9 + 7`.

---

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

---

## Examples

### Example 1

```text
nums = [1,2,3,4]
```

Output:

```text
8
```

Explanation: 8 valid partitions.

---

### Example 2

```text
nums = [1,1,1,1]
```

Output:

```text
1
```

Only the whole array is valid.

---

### Example 3

```text
nums = [1,2,1,3]
```

Output:

```text
2
```

---

## Intuition

For a good partition, whenever a number repeats, those occurrences must be in the **same** subarray.

So, for each index `i`, we need to know how far we must extend the current partition to include **all occurrences** of numbers seen so far.

Let:

- `last[x]` = last index where value `x` appears.

While scanning left to right, maintain:

- `j` = the maximum last index among all numbers in the current segment.

When `i == j`, the segment is closed, meaning we have a “cut point”.

At each cut point (except the final forced end), we can decide:

- cut here → start a new segment
- or keep going → but only if the segment is already closed

This yields powers of 2.

---

## Approach

1. Compute `last` index for every value.
2. Start scanning with:
   - `ans = 1`
   - `i = 0`
   - `j = last[nums[i]]`
3. For each `i`:
   - update `j = max(j, last[nums[i]])`
   - if `i > j_prev` (effectively when we complete a segment), multiply answer by 2.

(Implementation detail below follows the logic from the provided code.)

---

## Code (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numberOfGoodPartitions(vector<int>& nums) {
        const int MOD = 1000000007;

        int ans = 1;
        int n = (int)nums.size();

        unordered_map<int, int> last;
        last.reserve(n * 2);

        for (int i = 0; i < n; i++) last[nums[i]] = i;

        int i = 0;
        int j = last[nums[i]];

        while (i < n) {
            if (i > j) {
                ans = (ans * 2LL) % MOD;
            }
            j = max(j, last[nums[i]]);
            i++;
        }

        return ans;
    }
};
```

---

## Complexity Analysis

| Complexity | Value |
|-----------|-------|
| Time | **O(n)** |
| Space | **O(n)** |

---

## Key Takeaways

- Use last occurrence positions to know when a segment can end.
- Each time you can safely “cut” between independent segments, multiply by 2.
- Answer is computed modulo `10^9 + 7`.

