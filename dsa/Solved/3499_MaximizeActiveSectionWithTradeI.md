# 3499. Maximize Active Section with Trade I

## Problem Statement

You are given a binary string `s` of length `n`, where:

- `'1'` represents an **active** section.
- `'0'` represents an **inactive** section.

You may perform **at most one trade** to maximize the number of active sections.

A trade consists of two steps:

1. Convert a **contiguous block of `'1'`s** that is **surrounded by `'0'`s** into all `'0'`s.
2. Then, convert a **contiguous block of `'0'`s** that is **surrounded by `'1'`s** into all `'1'`s.

Return the **maximum number of active sections** after performing the optimal trade.

> **Note:** Treat the string as if it is augmented with a `'1'` at both ends:
>
> ```text
> t = "1" + s + "1"
> ```
>
> The augmented `'1'`s are used only for determining valid surrounded blocks and **do not** count toward the final answer.

---

## Examples

### Example 1

**Input**

```text
s = "01"
```

**Output**

```text
1
```

**Explanation**

```text
There is no block of '1's surrounded by '0's, so no valid trade can be made.

The maximum number of active sections remains 1.
```

---

### Example 2

**Input**

```text
s = "0100"
```

**Output**

```text
4
```

**Explanation**

```text
Original:
0100

Augmented:
101001

Choose the substring "0100".

101001
→ 100001   (convert surrounded '1's to '0's)
→ 111111   (convert surrounded '0's to '1's)

Removing the augmented ends gives:

1111
```

The maximum number of active sections is:

```text
4
```

---

### Example 3

**Input**

```text
s = "1000100"
```

**Output**

```text
7
```

**Explanation**

```text
Original:
1000100

Augmented:
110001001

Choose the substring "000100".

110001001
→ 110000001
→ 111111111

Removing the augmented ends gives:

1111111
```

The maximum number of active sections is:

```text
7
```

---

### Example 4

**Input**

```text
s = "01010"
```

**Output**

```text
4
```

**Explanation**

```text
Original:
01010

Augmented:
1010101

Choose the substring "010".

1010101
→ 1000101
→ 1111101

Removing the augmented ends gives:

11110
```

The maximum number of active sections is:

```text
4
```

---

## Constraints

```text
1 <= n == s.length <= 10^5
s consists only of the characters '0' and '1'.
```

```python
class Solution:
	'''
	Algorithm:
	1. Generate a list of zeros-ones eg. 0010 -> [00, 1, 0], 101110 -> [1, 0, 111, 0].
	2. For every 1's surrounded by 0's calculate the number of 0's on both sides eg. [00, 1, 0] -> 3 ( 00(2) + 0(1) )
	3. Calculate the maximum
	'''
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        
        n = len(s)

        arr = []   # array for splitting 0's and 1's

        i = 0
        while i<n: # while loop for appending the strings
            temp = s[i]
            while i+1 < n and s[i] == s[i+1]:
                temp += s[i]
                i += 1
            arr.append(temp)
            i += 1
        
        ans = 0

        if len(arr) <= 2: # if lenght of array or characters are less that 2, it is impossible to apply the operation hense return total 1's
            for i in s:
                if i == '1':
                    ans += 1
            return ans
        
        i,j = 0, 2
        while j < len(arr):
            if arr[i][0] == '0':
                ans = max(ans, len(arr[i]) + len(arr[j])) # calculate the number of 0's around 1's
            i += 1
            j += 1
        
        for i in s: # add original 1's
            if i == '1':
                ans += 1
        
        return ans
```