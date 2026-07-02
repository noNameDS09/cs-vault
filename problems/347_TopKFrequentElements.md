347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]

 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


## Code
```python
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num for num, count in Counter(nums).most_common(k)]
```

## Example
Sure! Here's the same style with **4 elements**.

### Input

```python
nums = [1,1,1,1,2,2,2,3,3,4]
k = 2
```

Frequency:

```python
1 -> 4
2 -> 3
3 -> 2
4 -> 1
```

### Dry Run

```text
heap = []

push (4,1)
heap = [(4,1)]

push (3,2)
heap = [(3,2), (4,1)]

push (2,3)
heap = [(2,3), (4,1), (3,2)]

size > k
pop -> removes (2,3)

heap = [(3,2), (4,1)]

push (1,4)
heap = [(1,4), (4,1), (3,2)]

size > k
pop -> removes (1,4)

heap = [(3,2), (4,1)]
```

### Final Answer

```python
[(3,2), (4,1)]
```

Extract the second values:

```python
[2, 1]
```

---

### Remember

The tuple is:

```python
(frequency, number)
```

So:

* `(4,1)` → number `1` appears `4` times
* `(3,2)` → number `2` appears `3` times
* `(2,3)` → number `3` appears `2` times
* `(1,4)` → number `4` appears `1` time

The heap always removes the **smallest frequency** whenever its size becomes greater than `k`, leaving only the `k` most frequent elements.
