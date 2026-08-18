---
tags:
  - array
  - string
  - greedy
  - hash-table
---

# 3517. Smallest Palindromic Rearrangement I

## Problem Statement

You are given a **palindromic** string `s`.

Return the **lexicographically smallest palindromic permutation** of `s`.

---

## Examples

### Example 1

**Input**

```text
s = "z"
```

**Output**

```text
"z"
```

**Explanation**

```text
A string containing only one character is already the
lexicographically smallest palindrome.
```

---

### Example 2

**Input**

```text
s = "babab"
```

**Output**

```text
"abbba"
```

**Explanation**

```text
Rearranging "babab" to "abbba" produces the
lexicographically smallest palindrome.
```

---

### Example 3

**Input**

```text
s = "daccad"
```

**Output**

```text
"acddca"
```

**Explanation**

```text
Rearranging "daccad" to "acddca" produces the
lexicographically smallest palindrome.
```

---

## Constraints

```text
1 <= s.length <= 10^5
s consists of lowercase English letters.
s is guaranteed to be palindromic.
```

## Code

```python
class Solution:
	'''
	Given a string which must be palindrome.
	So we can sort the first half of the string and store it.
	If string is of odd length then get the middle char.
	Reverse the first half and store it.
	Concatinate the strings.
	'''
    def smallestPalindrome(self, s: str) -> str:
        mid = len(s) // 2

        f = sorted(s[:mid])    # first half
        m = [s[mid]] if len(s) % 2 == 1 else []    # if odd len then middle element else []
        e = f[::-1]    # construct the second half

        return "".join(f + m + e)
```