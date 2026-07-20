# 838. Push Dominoes

## Problem Statement

You are given a string `dominoes` representing the initial state of `n` dominoes.

- `dominoes[i] = 'L'` if the `i`-th domino is pushed to the left.
- `dominoes[i] = 'R'` if the `i`-th domino is pushed to the right.
- `dominoes[i] = '.'` if the `i`-th domino is not pushed.

After each second:

- Every domino falling to the left pushes its adjacent domino on the left.
- Every domino falling to the right pushes its adjacent domino on the right.

If a domino gets forces from both sides, it stays upright.

Return the final state of `dominoes`.

---

## Constraints

- `n == dominoes.length`
- `1 <= n <= 10^5`
- `dominoes[i]` is `'L'`, `'R'`, or `'.'`.

---

## Examples

### Example 1

**Input**

```text
dominoes = "RR.L"
```

**Output**

```text
"RR.L"
```

---

### Example 2

**Input**

```text
dominoes = ".L.R...LR..L.."
```

**Output**

```text
"LL.RR.LLRRLL.."
```

---

## Intuition

For every position `i` that is `'.'`, only the nearest **left force** (an `'L'`) and the nearest **right force** (an `'R'`) matter.

- If only one side has a force, that force determines the result.
- If both sides exist, compare distances:
  - closer to `'R'` → becomes `'R'`
  - closer to `'L'` → becomes `'L'`
  - equal distances → stays `'.'`

---

## Approach

### Step 1: Precompute nearest left force

Create `leftR[i]` storing the index of the closest `'R'` to the left of `i` (including `i` if it's `'R'`), otherwise `-1`.

### Step 2: Precompute nearest right force

Create `rightL[i]` storing the index of the closest `'L'` to the right of `i` (including `i` if it's `'L'`), otherwise `-1`.

### Step 3: Decide each position

For each `i`:

- If `dominoes[i] != '.'`, keep it as is.
- Let `l = leftR[i]`, `r = rightL[i]`.
  - `l == -1 && r == -1` → `'.'`
  - `l == -1` → `'L'`
  - `r == -1` → `'R'`
  - else compare `distL = i - l` vs `distR = r - i`

---

## Dry Run (short)

For an index `i` inside a segment like:

```text
R....L
```

- `l` points to the `'R'` position
- `r` points to the `'L'` position
- distance comparison decides which side wins (or tie → '.')

---

## Code (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string pushDominoes(string dom) {
        int n = (int)dom.size();
        vector<int> leftR(n, -1);
        vector<int> rightL(n, -1);

        // nearest 'R' to the left
        for (int i = 0; i < n; i++) {
            if (dom[i] == 'R') leftR[i] = i;
            else if (dom[i] == 'L') leftR[i] = -1;
            else if (i > 0) leftR[i] = leftR[i - 1];
        }

        // nearest 'L' to the right
        for (int i = n - 1; i >= 0; i--) {
            if (dom[i] == 'L') rightL[i] = i;
            else if (dom[i] == 'R') rightL[i] = -1;
            else if (i < n - 1) rightL[i] = rightL[i + 1];
        }

        string res;
        res.reserve(n);

        for (int i = 0; i < n; i++) {
            if (dom[i] != '.') {
                res.push_back(dom[i]);
                continue;
            }

            int l = leftR[i];
            int r = rightL[i];

            if (l == -1 && r == -1) res.push_back('.');
            else if (l == -1) res.push_back('L');
            else if (r == -1) res.push_back('R');
            else {
                int distL = i - l; // distance from nearest R
                int distR = r - i; // distance from nearest L

                if (distL < distR) res.push_back('R');
                else if (distR < distL) res.push_back('L');
                else res.push_back('.');
            }
        }

        return res;
    }
};
```

---

## Complexity Analysis

| Complexity | Value |
|-----------|-------|
| Time | **O(n)** |
| Space | **O(n)** |

---

## Key Takeaways

- Precompute nearest forces from both directions.
- Use distance comparison to resolve conflicts.
- Linear time processing over the string.

