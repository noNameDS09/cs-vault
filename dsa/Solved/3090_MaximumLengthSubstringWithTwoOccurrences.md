# [3090. Maximum Length Substring With Two Occurrences](https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/)

Given a string `s`, return the **maximum** length of a substring such that it contains _at most two occurrences_ of each character.

**Example 1:**
**Input:** s = `"bcbbbcba"`
**Output:** 4
**Explanation:**
The following substring has a length of 4 and contains at most two occurrences of each character: `"bcbbbcba"`.

**Example 2:**
**Input:** s = `"aaaa"`
**Output:** 2
**Explanation:**
The following substring has a length of 2 and contains at most two occurrences of each character: `"aaaa"`.

**Constraints:**

- `2 <= s.length <= 100`
	- `s` consists only of lowercase English letters. 

## Code

**Use Khandani Sliding Window Template**
```python
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        freq = defaultdict(int)
        ans = 0
        for r in range(n):

            freq[s[r]] += 1

            while freq[s[r]] > 2:
                freq[s[l]] -= 1
                l += 1
            
            ans = max(ans, r-l+1)
        
        return ans
```