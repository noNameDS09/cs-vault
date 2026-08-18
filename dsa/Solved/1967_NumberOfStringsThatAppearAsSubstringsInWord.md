---
tags:
  - array
  - string
  - trie
  - hash-table
---

# 1967. Number of Strings That Appear as Substrings in Word

## Problem Statement

You are given an array of strings `patterns` and a string `word`.

Return the **number of strings** in `patterns` that appear as a **substring** of `word`.

A **substring** is a contiguous sequence of characters within a string.

---

## Examples

### Example 1

**Input**

```text
patterns = ["a","abc","bc","d"]
word = "abc"
```

**Output**

```text
3
```

**Explanation**

```text
"a" appears as a substring in "abc".
"abc" appears as a substring in "abc".
"bc" appears as a substring in "abc".
"d" does not appear as a substring in "abc".

Therefore, 3 strings from patterns appear as substrings in word.
```

---

### Example 2

**Input**

```text
patterns = ["a","b","c"]
word = "aaaaabbbbb"
```

**Output**

```text
2
```

**Explanation**

```text
"a" appears as a substring in "aaaaabbbbb".
"b" appears as a substring in "aaaaabbbbb".
"c" does not appear as a substring in "aaaaabbbbb".

Therefore, 2 strings from patterns appear as substrings in word.
```

---

### Example 3

**Input**

```text
patterns = ["a","a","a"]
word = "ab"
```

**Output**

```text
3
```

**Explanation**

```text
Each occurrence of "a" in patterns is counted separately because it appears as a substring of "ab".

Therefore, the answer is 3.
```

---

## Constraints

```text
1 <= patterns.length <= 100
1 <= patterns[i].length <= 100
1 <= word.length <= 100
patterns[i] and word consist of lowercase English letters.
```

## Code

```python
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ans = 0

        for i in patterns:
            if i in word:
                ans += 1

        return ans
```