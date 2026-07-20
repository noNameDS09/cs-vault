# 🟢 Contains Duplicate

> **Difficulty:** Easy  
> **Topics:** Array, Hash Table, Sorting

---

## 📖 Problem Statement

Given an integer array `nums`, return:

- `true` if **any value appears at least twice** in the array.
- `false` if **every element is distinct**.

---

## 📝 Examples

### Example 1

**Input**

```text
nums = [1,2,3,1]
```

**Output**

```text
true
```

**Explanation**

The number `1` appears more than once (indices `0` and `3`).

---

### Example 2

**Input**

```text
nums = [1,2,3,4]
```

**Output**

```text
false
```

**Explanation**

Every element is unique.

---

### Example 3

**Input**

```text
nums = [1,1,1,3,3,4,3,2,4,2]
```

**Output**

```text
true
```

**Explanation**

Multiple numbers occur more than once.

---

## 🔒 Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

# 💡 Approach

We use a **Hash Set** to keep track of numbers we've already seen.

### Algorithm

1. Create an empty set.
2. Traverse each number in the array.
3. If the number already exists in the set:
   - Return `True`.
4. Otherwise, insert it into the set.
5. If the loop finishes without finding duplicates, return `False`.

---

## 🎯 Why This Works

A **set** only stores **unique elements**.

- If an element is already in the set, we've encountered it before.
- Therefore, the array contains a duplicate.

---

# 🧠 Dry Run

### Input

```text
nums = [1,2,3,1]
```

| Step | Current Number | Set Before | Duplicate? | Set After |
|------|----------------|------------|------------|-----------|
| 1 | 1 | {} | ❌ | {1} |
| 2 | 2 | {1} | ❌ | {1,2} |
| 3 | 3 | {1,2} | ❌ | {1,2,3} |
| 4 | 1 | {1,2,3} | ✅ Yes | Return `True` |

---

# ✅ Python Solution

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
```

# ⏱️ Complexity Analysis

| Operation | Complexity |
|-----------|------------|
| Time | **O(n)** |
| Space | **O(n)** |

### Time Complexity: **O(n)**

- Each element is visited exactly once.
- Set lookup and insertion take **O(1)** on average.

### Space Complexity: **O(n)**

- In the worst case (all distinct elements), every element is stored in the set.

---

# ✅ Key Idea

Instead of comparing every pair of elements (**O(n²)**), use a **Hash Set** to remember previously seen numbers.

- Seen before → **Duplicate found**
- Not seen → **Store it**

This reduces the solution to **linear time**.

---

# 🚀 Final Solution

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
```

---

## 📌 Takeaways

- ✔️ Use a **Hash Set** for fast membership checking.
- ✔️ Membership test in a set is **O(1)** on average.
- ✔️ Ideal solution for detecting duplicates in linear time.
- ✔️ Common interview pattern: **Hashing + Single Pass**.