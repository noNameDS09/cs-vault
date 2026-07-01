# KMP - Pattern Search (LPS / Prefix Function)

## Problem Statement

Given a text string `s` and a pattern string `p`, find all starting indices where `p` occurs in `s`.

This file contains a classic **KMP (Knuth–Morris–Pratt)** implementation using the **LPS (Longest Prefix Suffix)** array.

---

## Intuition

KMP avoids re-checking characters that we already know match via previously computed prefix information.

If a mismatch occurs after matching `j` characters, we can shift the pattern so that the next comparison continues from `lps[j-1]` instead of restarting from 0.

---

## Approach

### Step 1: Build LPS array for pattern `p`

`lps[i]` = length of the longest proper prefix of `p[0..i]` that is also a suffix of `p[0..i]`.

### Step 2: Scan text `s`

Maintain:

- `i` for index in `s`
- `j` for index in `p`

When `s[i] == p[j]`, advance both.

When `j == m` (full match), store the match start index `i - j` and continue using `j = lps[j-1]`.

On mismatch:

- if `j > 0`, set `j = lps[j-1]`
- else increment `i`

---

## Code (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> kmp(string s, string p) {
    int n = (int)s.size(), m = (int)p.size();
    int i = 0, j = 0;
    vector<int> lps(m), ans;

    // Build LPS
    for (int i = 1, j = 0; i < m;) {
        if (p[i] == p[j]) {
            lps[i] = ++j;
            i++;
        } else if (j) {
            j = lps[j - 1];
        } else {
            lps[i] = 0;
            i++;
        }
    }

    // Search
    i = 0, j = 0;
    while (i < n) {
        if (s[i] == p[j]) {
            i++;
            j++;
        }

        if (j == m) {
            ans.push_back(i - j);
            j = lps[j - 1];
        } else if (i < n && s[i] != p[j]) {
            if (j) j = lps[j - 1];
            else i++;
        }
    }

    return ans;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string s, p;
    cin >> s >> p;

    for (int x : kmp(s, p)) cout << x << " ";
}
```

---

## Complexity Analysis

| Complexity | Value |
|-----------|-------|
| Time | **O(n + m)** |
| Space | **O(m)** |

---

## Key Takeaways

- KMP builds LPS once, then performs a single linear scan.
- Prevents worst-case O(n*m) behavior.

