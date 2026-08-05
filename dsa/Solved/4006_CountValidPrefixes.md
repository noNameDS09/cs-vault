# [4006. Count Valid Prefixes](https://leetcode.com/problems/count-valid-prefixes/)

## Problem Statement

You are given a binary string `s`.

A **prefix** of `s` is considered **valid** if its characters can be rearranged to form an **alternating string**.

Return the **number of valid prefixes** of `s`.

A string is considered **alternating** if no two adjacent characters are equal.

---

## Examples

### Example 1

**Input**

```text
s = "00101"
```

**Output**

```text
3
```

**Explanation**

The valid prefixes are:

```text
"0"
```

It is already an alternating string.

```text
"001"
```

It can be rearranged into:

```text
"010"
```

which is alternating.

```text
"00101"
```

It can be rearranged into:

```text
"01010"
```

which is alternating.

Thus, the answer is:

```text
3
```

---

### Example 2

**Input**

```text
s = "101"
```

**Output**

```text
3
```

**Explanation**

```text
All prefixes of "101" are already alternating strings.

Therefore, the answer is 3.
```

---

## Constraints

```text
1 <= s.length <= 100
s consists only of '0' and '1'.
```

## Code

**Approach 1 Brute Force O(n<sup>3</sup>)**
```python
class Solution:
    def countValidPrefixes(self, s: str) -> int:
        n = len(s)
        # from collections import Counter
        
        def alter(pre):
            # print(pre)
            if len(pre) == 1: return True
            one = pre.count('1')
            zero = pre.count('0')
            n_ = len(pre)
            # print(pre, one, zero)
            if one == zero:
                return True
            
            if n_ % 2 != 0:
                if abs(one-zero) == 1:
                    return True
            
            return False

        ans = 0

        for i in range(1):
            for j in range(n):
                if alter(s[i:j+1]):
                    ans += 1
        
        return ans
```

**Better Approach O(n)**
```python
class Solution:
	def countValidPrefixes(self, s: str) -> int:
		ans = 0
		one, zero = 0, 0
		for i in s:
			if i == '1':
				one += 1
			else:
				zero += 1
			
			if one == zero or abs(one - zero) == 1:
				ans += 1
		return ans
```