# 20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
```
Example 1:
Input: s = "()"
Output: true
```
```
Example 2:
Input: s = "()[]{}"
Output: true
```
```
Example 3:
Input: s = "(]"
Output: false
```
```
Example 4:
Input: s = "([])"
Output: true
```
```
Example 5:
Input: s = "([)]"
Output: false
```
Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

```python
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack = []

        for ch in s:
            if ch in pairs.values(): # If opening bracket -> push in stack
                stack.append(ch)
            else:
                if not stack or stack.pop() != pairs[ch]: # if empty stack or not corresponding closing bracket -> return False
                    return False
        
        return len(stack) == 0
```