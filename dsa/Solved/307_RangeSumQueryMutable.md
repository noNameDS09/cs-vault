# [307. Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/)

Given an integer array `nums`, handle multiple queries of the following types:

1. **Update** the value of an element in `nums`.
2. Calculate the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** where `left <= right`.

Implement the `NumArray` class:

- `NumArray(int[] nums)` Initializes the object with the integer array `nums`.
- `void update(int index, int val)` **Updates** the value of `nums[index]` to be `val`.
- `int sumRange(int left, int right)` Returns the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** (i.e. `nums[left] + nums[left + 1] + ... + nums[right]`).

**Example 1:**

**Input**
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
**Output**
[null, 9, null, 8]

**Explanation**
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8

**Constraints:**

- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `0 <= index < nums.length`
- `-100 <= val <= 100`
- `0 <= left <= right < nums.length`
- At most `3 * 10^4` calls will be made to `update` and `sumRange`.

## Code

```python
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.tree = [0] * (4*self.n)
        self.build(1, 0, self.n-1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.nums[start]
            return
        
        mid = (start + end) // 2

        self.build(2*node, start, mid)
        self.build(2*node+1, mid+1, end)

        self.tree[node] = self.tree[2*node] + self.tree[2*node+1]
        return
    
    def up(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            self.nums[idx] = val
            return
        
        mid = (start+end) // 2

        if idx <= mid:
            self.up(2*node, start, mid, idx, val)
        else:
            self.up(2*node+1, mid+1, end, idx, val)
        
        self.tree[node] = self.tree[2*node] + self.tree[2*node+1]
        return

    def update(self, index: int, val: int) -> None:
        self.up(node=1, start=0, end=self.n-1, idx=index, val=val)

    def query(self, node, start, end, left, right):
        if end < left or start > right:
            return 0
        
        if start >= left and end <= right:
            return self.tree[node]
        
        mid = (start+end) // 2

        left_sum = self.query(2*node, start, mid, left, right)
        right_sum = self.query(2*node+1, mid+1, end, left, right)
        return left_sum + right_sum

    def sumRange(self, left: int, right: int) -> int:
        return self.query(node=1, start=0, end=self.n-1, left=left, right=right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
```