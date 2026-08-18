---
tags:
  - array
  - math
  - number-theory
---

# 3867. Sum of GCD of Formed Pairs

## Problem Statement

You are given an integer array `nums` of length `n`.

Construct an array `prefixGcd` where, for each index `i`:

- Let

```text
mxi = max(nums[0], nums[1], ..., nums[i])
```

- Then,

```text
prefixGcd[i] = gcd(nums[i], mxi)
```

After constructing `prefixGcd`:

1. Sort `prefixGcd` in **non-decreasing order**.
2. Form pairs by taking:
   - the **smallest unpaired** element, and
   - the **largest unpaired** element.
3. Repeat until no more pairs can be formed.
4. For each pair, compute the **GCD** of the two elements.
5. If `n` is odd, the middle element remains unpaired and is ignored.

Return the **sum of the GCDs** of all formed pairs.

> Here, `gcd(a, b)` denotes the greatest common divisor of `a` and `b`.

---

## Examples

### Example 1

**Input**

```text
nums = [2,6,4]
```

**Output**

```text
2
```

**Explanation**

Construct `prefixGcd`:

| i | nums[i] | mxi | prefixGcd[i] |
|---|--------:|----:|-------------:|
| 0 | 2 | 2 | 2 |
| 1 | 6 | 6 | 6 |
| 2 | 4 | 6 | 2 |

```text
prefixGcd = [2,6,2]
```

After sorting:

```text
[2,2,6]
```

Form pairs:

```text
gcd(2,6) = 2
```

The remaining middle element `2` is ignored.

```text
Answer = 2
```

---

### Example 2

**Input**

```text
nums = [3,6,2,8]
```

**Output**

```text
5
```

**Explanation**

Construct `prefixGcd`:

| i | nums[i] | mxi | prefixGcd[i] |
|---|--------:|----:|-------------:|
| 0 | 3 | 3 | 3 |
| 1 | 6 | 6 | 6 |
| 2 | 2 | 6 | 2 |
| 3 | 8 | 8 | 8 |

```text
prefixGcd = [3,6,2,8]
```

After sorting:

```text
[2,3,6,8]
```

Form pairs:

```text
gcd(2,8) = 2
gcd(3,6) = 3
```

```text
Answer = 2 + 3 = 5
```

---

## Constraints

```text
1 <= n == nums.length <= 10^5
1 <= nums[i] <= 10^9
```

```python
class Solution:

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        
        return a

    def gcdSum(self, arr: list[int]) -> int:
        n = len(arr)
        prefix = [0] * n

        # pre = [0] * n
        # pre[0] = arr[0]
        # for i in range(1, n):
        #     pre[i] = max(arr[i], pre[i-1])
        
        mxi = 0
        for i in range(n):
            mxi = max(mxi, arr[i])
            prefix[i] = self.gcd(arr[i], mxi)
        
        prefix.sort()

        ans = 0

        i, j = 0, n-1

        while i < j:
            ans += self.gcd(prefix[i], prefix[j])
            i += 1
            j -=1
        
        return ans
```