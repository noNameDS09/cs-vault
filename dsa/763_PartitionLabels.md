# 763. Partition Labels

## Problem Statement

You are given a string `s`. Partition `s` into as many parts as possible so that **each letter appears in at most one part**.

Return a list of integers where each integer represents the **size** of the corresponding partition.

---

## Constraints

- `1 <= s.length <= 500`
- `s` consists of lowercase English letters.

---

## Examples

### Example 1

**Input**

```text
s = "ababcbacadefegdehijhklij"
```

**Output**

```text
[9,7,8]
```

**Explanation**

The partition is:

```text
"ababcbaca", "defegde", "hijhklij"
```

---

### Example 2

**Input**

```text
s = "eccbbbbdec"
```

**Output**

```text
[10]
```

---

## Intuition

For each character, we only care about its **last occurrence** in the string.

While building a partition starting at index `i`, we must extend the partition until we reach the last occurrence of **every character** that appears inside it.

---

## Approach

### Step 1: Store last index of each character

For every character `c`, compute:

- `last[c] = last position where c appears in s`

### Step 2: Greedily form partitions

- Start a partition at `i`
- Let `end = last[s[i]]`
- Move `j` forward, updating `end` to include the last occurrence of any new character encountered
- When `j == end`, the current partition is complete

---

## Dry Run (Example 1)

`s = "ababcbacadefegdehijhklij"`

- Partition begins at `i=0` (`'a'`), so initial `end = last['a'] = 8`
- Scanning updates `end` as other characters appear
- When the scan reaches `end`, we output the partition size (`end - i + 1 = 9`)

Repeat for remaining characters.

---

## Code (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> partitionLabels(string s) {
        unordered_map<char, int> last;

        for (int i = 0; i < (int)s.size(); i++) {
            last[s[i]] = i;
        }

        vector<int> ans;
        int i = 0, j = 0;
        int n = (int)s.size();

        while (i < n) {
            int end = last[s[i]];

            while (j < n && j < end) {
                end = max(end, last[s[j]]);
                j++;
                if (end == j) break;
            }

            ans.push_back(j - i + 1);
            i = j + 1;
        }

        return ans;
    }
};
```

---

## Complexity Analysis

| Complexity | Value |
|-----------|-------|
| Time | **O(n)** |
| Space | **O(1)** (at most 26 letters) |

---

## Key Takeaways

- Precompute the last occurrence index for each character.
- Greedily grow a partition until all characters inside are fully contained.
- Each index is processed at most once → linear time.

