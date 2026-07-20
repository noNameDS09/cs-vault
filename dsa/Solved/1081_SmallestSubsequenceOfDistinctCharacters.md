Given a string `s`, return _the_ _lexicographically smallest_ _subsequence_ _of_ `s` _that contains all the distinct characters of_ `s` _exactly once_.

**Example 1:**

**Input:** s = "bcabc"
**Output:** "abc"

**Example 2:**

**Input:** s = "cbacdcbc"
**Output:** "acdb"

**Constraints:**

- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters.

**Note:** This question is the same as 316: [https://leetcode.com/problems/remove-duplicate-letters/](https://leetcode.com/problems/remove-duplicate-letters/)


```python
class Solution:

    def smallestSubsequence(self, s: str) -> str:
        from collections import Counter
        mp = Counter(s)
        stack = []
        st = set()

        for ch in s:
            mp[ch] -= 1

            if ch in st:
                continue              

            while stack and stack[-1] > ch and mp[stack[-1]] > 0:
                st.remove(stack.pop())

            stack.append(ch)
            st.add(ch)

        return "".join(stack)
```
