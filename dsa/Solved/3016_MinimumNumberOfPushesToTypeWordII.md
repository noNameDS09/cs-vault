# 3016. Minimum Number of Pushes to Type Word II

## Problem Statement

You are given a string `word` consisting of lowercase English letters.

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
word = "xyzxyzxyzxyz"
```

**Output**

```text
12
```

**Explanation**

```text
An optimal remapping is:

x → 1 push
y → 1 push
z → 1 push

Each letter appears 4 times.

Total pushes =
1 × 4 + 1 × 4 + 1 × 4 = 12

It is not necessary to assign letters to every key.
```

---

### Example 3

**Input**

```text
word = "aabbccddeeffgghhiiiiii"
```

**Output**

```text
24
```

**Explanation**

```text
An optimal remapping is:

a → 1 push
b → 1 push
c → 1 push
d → 1 push
e → 1 push
f → 1 push
g → 1 push
h → 2 pushes
i → 1 push

Total pushes =
1×2 + 1×2 + 1×2 + 1×2 + 1×2 +
1×2 + 1×2 + 2×2 + 1×6 = 24
```

---

## Constraints

```text
1 <= word.length <= 10^5
word consists of lowercase English letters.
```

## Code

```python
class Solution:
    def minimumPushes(self, word: str) -> int:
        from collections import Counter

        # Count the frequency of each character.
        freq = Counter(word)
        ans = 0

        # Sort characters by descending frequency.
        # Every group of 8 characters requires one extra key press.
        for i, (_, count) in enumerate(freq.most_common()):
            presses = i // 8 + 1
            ans += count * presses

        return ans
```