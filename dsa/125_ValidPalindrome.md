# 125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
```
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```
```
Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```
```
Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

```python
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s) # removes non alphanumeric chars
        s = s.lower() # lowercase the string
        n = len(s)
        l, r = 0, n-1  # two pointers
        # print(s)
        while(l <= r):
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
```