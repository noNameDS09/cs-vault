# 3014. Minimum Number of Pushes to Type Word I

## Problem Statement

You are given a string `word` consisting of **distinct** lowercase English letters.

A telephone keypad contains keys numbered **2** to **9**, each of which can be mapped to a distinct collection of lowercase English letters.

To type a letter:

- If it is the **1st** letter assigned to a key, press the key **once**.
- If it is the **2nd** letter assigned to the same key, press the key **twice**.
- If it is the **3rd** letter assigned to the same key, press the key **three times**, and so on.

You may **remap** the letters to the keys numbered **2** through **9** in any way, subject to the following rules:

- Each letter is assigned to **exactly one** key.
- Each key may contain **any number of letters**.
- Different keys must have **distinct** letter assignments.

Return the **minimum number of key presses** required to type `word` after choosing an optimal remapping.

---

## Examples

### Example 1

**Input**

```text
word = "abcde"
```

**Output**

```text
5
```

**Explanation**

```text
An optimal remapping assigns each letter to be the first
letter on a different key.

a → 1 push
b → 1 push
c → 1 push
d → 1 push
e → 1 push

Total pushes = 5.
```

---

### Example 2

**Input**

```text
word = "xycdefghij"
```

**Output**

```text
12
```

**Explanation**

```text
One optimal remapping is:

x → 1 push
y → 2 pushes
c → 1 push
d → 2 pushes
e → 1 push
f → 1 push
g → 1 push
h → 1 push
i → 1 push
j → 1 push

Total pushes = 12.
```

---

## Constraints

```text
1 <= word.length <= 26
word consists of lowercase English letters.
All letters in word are distinct.
```

## Code

```python
class Solution:
    def minimumPushes(self, word: str) -> int:
		'''
		All chars are distint -> main point
		'''
        ans = 0

        for i in range(len(word)):
            if i < 8:
                ans += 1
            elif i < 16:
                ans += 2
            elif i < 24:
                ans += 3
            else:
                ans += 4

        return ans
```