---
tags:
  - array
  - binary-search
  - greedy
  - string
---

# [3302. Find the Lexicographically Smallest Valid Sequence](https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/)

You are given two strings `word1` and `word2`.

A string `x` is called **almost equal** to `y` if you can change **at most** one character in `x` to make it _identical_ to `y`.

A sequence of indices `seq` is called **valid** if:

- The indices are sorted in **ascending** order.
- _Concatenating_ the characters at these indices in `word1` in **the same** order results in a string that is **almost equal** to `word2`.

Return an array of size `word2.length` representing the lexicographically smallest **valid** sequence of indices. If no such sequence of indices exists, return an **empty** array.

**Note** that the answer must represent the _lexicographically smallest array_, **not** the corresponding string formed by those indices.

**Example 1:**

**Input:** word1 = "vbcca", word2 = "abc"

**Output:** [0,1,2]

**Explanation:**

The lexicographically smallest valid sequence of indices is `[0, 1, 2]`:

- Change `word1[0]` to `'a'`.
- `word1[1]` is already `'b'`.
- `word1[2]` is already `'c'`.

**Example 2:**

**Input:** word1 = "bacdc", word2 = "abc"

**Output:** [1,2,4]

**Explanation:**

The lexicographically smallest valid sequence of indices is `[1, 2, 4]`:

- `word1[1]` is already `'a'`.
- Change `word1[2]` to `'b'`.
- `word1[4]` is already `'c'`.

**Example 3:**

**Input:** word1 = "aaaaaa", word2 = "aaabc"

**Output:** []

**Explanation:**

There is no valid sequence of indices.

**Example 4:**

**Input:** word1 = "abc", word2 = "ab"

**Output:** [0,1]

**Constraints:**

- `1 <= word2.length < word1.length <= 3 * 105`
- `word1` and `word2` consist only of lowercase English letters.

## Code

```python
class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n1 = len(word1)
        n2 = len(word2)

        ans = []

        # suffix[i] stores the maximum number of characters of word2
        # that can be matched as a subsequence using word1[i:].
        #
        # This helps us decide whether we can afford to use word1[i]
        # as the one mismatched character.
        suffix = [0] * (n1 + 1)

        i, j = n1 - 1, n2 - 1

        # Build the suffix array from right to left.
        #
        # We greedily match word2 from the end while traversing word1
        # from the end. Whenever the characters match, we increase
        # the number of matched characters.
        while i >= 0:
            # Initially, carry forward the number of matches possible
            # from word1[i + 1:].
            suffix[i] = suffix[i + 1]

            # If the current characters match, we can match one more
            # character of word2.
            if j >= 0 and word1[i] == word2[j]:
                suffix[i] += 1
                j -= 1

            i -= 1

        # Reset pointers for the main left-to-right traversal.
        i, j = 0, 0

        # `flag` tells us whether we have already used our one
        # allowed mismatched character.
        flag = True

        while i < n1 and j < n2:

            # Case 1: Current characters match.
            # We can directly use word1[i] to match word2[j].
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Case 2: Characters don't match.
            #
            # We can use this character as the one allowed mismatch,
            # but only if the remaining suffix of word1 is sufficient
            # to match all remaining characters of word2.
            elif flag and suffix[i + 1] >= n2 - j - 1:
                ans.append(i)

                # We have now used our one mismatch.
                flag = False

                # Treat word1[i] as matching word2[j] through
                # the allowed mismatch.
                j += 1

            # Move to the next character in word1.
            i += 1

        # If we managed to match all characters of word2,
        # return their indices. Otherwise, no valid sequence exists.
        if j != n2:
            return []

        return ans
```