# 7. Reverse Integer

## Problem Statement

Given a signed **32-bit** integer `x`, return `x` with its digits reversed.

If reversing `x` causes the value to go outside the signed 32-bit integer range:

```text
[-2^31, 2^31 - 1]
```

then return `0`.

> Assume the environment does **not** allow you to store 64-bit integers (signed or unsigned).

---

## Examples

### Example 1

**Input**

```text
x = 123
```

**Output**

```text
321
```

---

### Example 2

**Input**

```text
x = -123
```

**Output**

```text
-321
```

---

### Example 3

**Input**

```text
x = 120
```

**Output**

```text
21
```

---

## Constraints

```text
-2^31 <= x <= 2^31 - 1
```

## Code

```python
class Solution:
	def reverse(self, x: int) -> int:
		flag = x < 0
		x = abs(x)
		
		x = int(str(x)[::-1])
		
		if flag:
			x = -x
		
		if x < -2**31 or x > (2**31-1):
			return 0
		
		return x
```