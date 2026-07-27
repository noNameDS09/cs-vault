# 2315. Count Asterisks

## Problem Statement

You are given a string `s`, where every two consecutive vertical bars `'|'` form a pair. That is:

- The 1st and 2nd `'|'` form the first pair.
- The 3rd and 4th `'|'` form the second pair.
- And so on.

Return the **number of `'*'` characters** in `s`, **excluding** the asterisks that appear between each pair of `'|'`.

Each `'|'` belongs to exactly one pair.

---

## Examples

### Example 1

**Input**

```text
s = "l|*e*et|c**o|*de|"
```

**Output**

```text
2
```

**Explanation**

```text
The characters between the first and second '|' are ignored.
The characters between the third and fourth '|' are also ignored.
Only 2 asterisks outside these paired sections are counted.
```

---

### Example 2

**Input**

```text
s = "iamprogrammer"
```

**Output**

```text
0
```

**Explanation**

```text
There are no asterisks in the string.
```

---

### Example 3

**Input**

```text
s = "yo|uar|e**|b|e***au|tifu|l"
```

**Output**

```text
5
```

**Explanation**

```text
Ignore the characters between each pair of '|'.

There are 5 asterisks outside the ignored sections.
```

---

## Constraints

```text
1 <= s.length <= 1000
s consists of lowercase English letters, vertical bars '|', and asterisks '*'.
s contains an even number of vertical bars '|'.
```

## Code 

```python
class Solution:
    def countAsterisks(self, s: str) -> int:
        ans = 0
        flag = False

        for i in s:
            if flag and i == '|':
                flag = False
            elif not flag and i == '|':
                flag = True
            elif not flag and i == '*':
                ans += 1
        
        return ans
```