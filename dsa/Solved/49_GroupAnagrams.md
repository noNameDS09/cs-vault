---
tags:
  - array
  - hash-table
  - string
  - sorting
---

# Group Anagrams

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

---

### Example 1

**Input:**

```text
strs = ["eat","tea","tan","ate","nat","bat"]
```

**Output:**

```text
[["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Explanation:**

* There is no string in `strs` that can be rearranged to form `"bat"`.
* The strings `"nat"` and `"tan"` are anagrams of each other.
* The strings `"ate"`, `"eat"`, and `"tea"` are anagrams of each other.

### Example 2

**Input:**

```text
strs = [""]
```

**Output:**

```text
[[""]]
```

### Example 3

**Input:**

```text
strs = ["a"]
```

**Output:**

```text
[["a"]]
```

---

### Constraints

* `1 <= strs.length <= 10^4`
* `0 <= strs[i].length <= 100`
* `strs[i]` consists of lowercase English letters.

---

## Intuition

Two strings are anagrams if they contain the same characters with the same frequencies. Sorting the characters of an anagram always produces the same string, making it an ideal key for grouping.

## Approach

* Create a hash map where:

  * **Key:** Sorted version of a string.
  * **Value:** List of strings having the same sorted representation.
* Iterate through each string in the input.
* Sort the string to generate its canonical key.
* Append the original string to the corresponding list.
* Return all grouped values.

---

## Implementation

```python
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            groups[key].append(word)

        return list(groups.values())
```

---

## Complexity Analysis

* **Time Complexity:** `O(n × k log k)`

  * `n` = number of strings
  * `k` = maximum length of a string
  * Each string is sorted once.

* **Space Complexity:** `O(n × k)`

  * The hash map stores every string, and the sorted keys require additional space.

---

## Key Insight

The sorted form of a string acts as a unique signature for its anagram group. Strings with identical signatures are guaranteed to be anagrams and are therefore grouped under the same hash map key.
