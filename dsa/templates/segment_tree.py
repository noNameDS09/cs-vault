class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums
        self.tree = [0] * (4 * self.n)
        self.build(1, 0, self.n - 1)

    def build(self, node, start, end) -> None:
        if start == end:
            self.tree[node] = self.nums[start]
            return

        mid = (start + end) // 2

        self.build(2*node, start, mid)
        self.build(2*node + 1, mid+1, end)

        self.tree[node] = self.tree[2*node] + self.tree[2*node + 1]
        return

    def query(self, node, start, end, left, right) -> int:
        if end < left or start > right:
            return 0

        if start >= left and end <= right:
            return self.tree[node]

        mid = (start + end) // 2

        right_sum = self.query(2*node, start, mid, left, right)
        left_sum = self.query(2*node + 1, mid+1, end, left, right)

        return right_sum + left_sum

    def update(self, node, start, end, idx, val) -> None:
        if start == end:
            self.tree[node] = val
            self.nums[idx] = val
            return

        mid = (start + end) // 2

        if idx <= mid:
            self.update(2*node, start, mid, idx, val)
        else:
            self.update(2*node + 1, mid+1, end, idx, val)

        self.tree[node] = self.tree[2*node] + self.tree[2*node + 1]
        return

nums = [2, 4, 3, 1]
seg_tree = SegmentTree(nums)
# print(seg_tree.tree)
# print(seg_tree.query(1, 0, seg_tree.n - 1, 2, 3))
seg_tree.update(1, 0, seg_tree.n - 1, 3, 10)
print(seg_tree.query(1, 0, seg_tree.n - 1, 2, 3))   
