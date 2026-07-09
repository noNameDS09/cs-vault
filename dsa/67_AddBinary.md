# 67. Add Binary

## Problem Statement

Given two binary strings `a` and `b`, return their sum as a **binary string**.

---

## Examples

### Example 1

**Input**

```text
a = "11"
b = "1"
```

**Output**

```text
"100"
```

**Explanation**

```text
11₂ + 1₂ = 100₂
```

---

### Example 2

**Input**

```text
a = "1010"
b = "1011"
```

**Output**

```text
"10101"
```

**Explanation**

```text
1010₂ + 1011₂ = 10101₂
```

---

## Constraints

```text
1 <= a.length, b.length <= 10^4
1 <= b.length <= 10^4
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the number "0" itself.
```
```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
```