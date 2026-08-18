---
tags:
  - string
  - hash-table
  - sorting
---

## 242. Valid Anagram

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

### Examples

**Example 1:**
- Input: `s = "anagram"`, `t = "nagaram"`
- Output: `true`

**Example 2:**
- Input: `s = "rat"`, `t = "car"`
- Output: `false`

### Constraints
- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

### Solution (Frequency Counting)

Use a frequency array of size 26 to count character occurrences in `s`, then decrement counts using `t`. If all counts return to zero, the strings are anagrams.

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        for ch in t:
            freq[ord(ch) - ord('a')] -= 1

        return all(count == 0 for count in freq)
```

