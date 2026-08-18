---
tags:
  - array
  - hash-table
  - union-find
---

# 128. Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
```
Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```
```
Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```
```
Example 3:
Input: nums = [1,0,1,2]
Output: 3
 ```

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109

## Brute force
### Time -> O(n^2), Space -> O(1)
```python
class Solution:
    def ls(self, nums, x):
        for i in nums:
            if i == x:
                return True
            
        return False

    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)
        ans = 0

        for i in range(n):
            curr = nums[i]
            l = 1

            while(self.ls(nums, curr+1)):
                curr += 1
                l += 1
            
            ans = max(ans, l)
        
        return ans
```

## Better approach 
### Time -> O(n) , Space -> O(n)
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        ans = 1
        st = set(nums)

        # for i in nums:
        #     st.add(i)
        
        for i in st:
            if i-1 not in st:
                cnt = 1
                x = i
                while x+1 in st:
                    x += 1
                    cnt += 1
                
                ans = max(ans, cnt)

        return ans
```