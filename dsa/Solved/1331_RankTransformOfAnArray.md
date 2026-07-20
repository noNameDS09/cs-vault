# 1331. Rank Transform of an Array

## Problem Statement

Given an array of integers `arr`, replace each element with its **rank**.

The rank represents how large the element is and follows these rules:

- Rank is an integer starting from **1**.
- The larger the element, the larger its rank.
- If two elements are equal, they must have the **same rank**.
- Ranks should be assigned as small as possible.

Return the transformed array after replacing each element with its rank.

---

## Examples

### Example 1

**Input**

```text
arr = [40,10,20,30]
```

**Output**

```text
[4,1,2,3]
```

**Explanation**

```text
40 is the largest element.
10 is the smallest.
20 is the second smallest.
30 is the third smallest.
```

---

### Example 2

**Input**

```text
arr = [100,100,100]
```

**Output**

```text
[1,1,1]
```

**Explanation**

```text
All elements are equal, so they share the same rank.
```

---

### Example 3

**Input**

```text
arr = [37,12,28,9,100,56,80,5,12]
```

**Output**

```text
[5,3,4,2,8,6,7,1,3]
```

---

## Constraints

```text
0 <= arr.length <= 10^5
-10^9 <= arr[i] <= 10^9
```
```python

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        if not arr:
            return []

        n = len(arr)
        if n == 1:
            return [1]

        mp = dict()
        newarr = sorted(arr) # Sort the array
        mp[newarr[0]] = 1   # Start from 1. The first element will be always smaller of all so assign it 1
        count = 2  # start numbering from 2
        for i in range(n):
            if newarr[i] != newarr[i-1]: # assign the next counter if different element is found
                mp[newarr[i]] = count -1
                count += 1  # increase the counter
        newarr = []

        for i in range(n):
            newarr.append(mp[arr[i]]) # build the answer
            
        return newarr
```