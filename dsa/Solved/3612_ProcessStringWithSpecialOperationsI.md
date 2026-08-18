---
tags:
  - array
  - string
  - simulation
---

# 3612. Process String with Special Operations I

## Problem Statement

You are given a string `s` consisting of lowercase English letters and the special characters:

```text
*, #, %
```

Build a new string `result` by processing `s` from **left to right** according to the following rules:

- If the character is a lowercase English letter, append it to `result`.
- If the character is `'*'`, remove the last character from `result`, if it exists.
- If the character is `'#'`, duplicate the current `result` and append it to itself.
- If the character is `'%'`, reverse the current `result`.

Return the final string `result` after processing all characters in `s`.

---

## Examples

### Example 1

**Input**

```text
s = "a#b%*"
```

**Output**

```text
"ba"
```

**Explanation**

| i | s[i] | Operation | Current result |
|---|---|---|---|
| 0 | `'a'` | Append `'a'` | `"a"` |
| 1 | `'#'` | Duplicate result | `"aa"` |
| 2 | `'b'` | Append `'b'` | `"aab"` |
| 3 | `'%'` | Reverse result | `"baa"` |
| 4 | `'*'` | Remove last character | `"ba"` |

Thus, the final result is:

```text
"ba"
```

---

### Example 2

**Input**

```text
s = "z*#"
```

**Output**

```text
""
```

**Explanation**

| i | s[i] | Operation | Current result |
|---|---|---|---|
| 0 | `'z'` | Append `'z'` | `"z"` |
| 1 | `'*'` | Remove last character | `""` |
| 2 | `'#'` | Duplicate result | `""` |

Thus, the final result is:

```text
""
```

---

## Constraints

```text
1 <= s.length <= 20
s consists only of lowercase English letters and the special characters '*', '#', and '%'.
```

## Code

```python
class Solution:
	'''
	This is simulation problem since the constraints are low
	'''
    def processStr(self, s: str) -> str:
        res = ""
        for c in s:
            if c.isalpha():
                res += c
            elif c == '*':
                if res:
                    res = res[:-1]
            elif c == '#':
                res += res
            elif c == '%':
                res = res[::-1]
        
        return res
```