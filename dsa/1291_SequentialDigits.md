# 1291. Sequential Digits

## Problem Statement

An integer has **sequential digits** if and only if each digit is exactly **one greater** than the previous digit.

For example:

```text
1234   ✓
4567   ✓
789    ✓
1245   ✗
1357   ✗
```

Given two integers `low` and `high`, return a **sorted list** of all integers in the inclusive range `[low, high]` that have sequential digits.

---

## Examples

### Example 1

**Input**

```text
low = 100
high = 300
```

**Output**

```text
[123,234]
```

---

### Example 2

**Input**

```text
low = 1000
high = 13000
```

**Output**

```text
[1234,2345,3456,4567,5678,6789,12345]
```

---

## Constraints

```text
10 <= low <= high <= 10^9
```
```python
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # List to store all valid sequential digit numbers
        ans = []

        # Generate sequential numbers of lengths from 2 to 9
        # (A single digit is not considered sequential)
        for length in range(2, 10):

            # Choose the starting digit.
            # The maximum valid starting digit depends on the length
            # so that the sequence does not exceed 9.
            # Example:
            # length = 3 -> start can be 1 to 7 (123 ... 789)
            for start in range(1, 11 - length):

                # Build the sequential number digit by digit
                nums = 0
                for digit in range(start, start + length):
                    # Shift existing digits left and append the next digit
                    nums = nums * 10 + digit

                # Add the number if it lies within the given range
                if low <= nums <= high:
                    ans.append(nums)

        # The generated numbers are naturally in ascending order
        return ans
```