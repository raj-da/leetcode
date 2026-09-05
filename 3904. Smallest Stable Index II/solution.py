class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        minPrefix = nums[:]
        for ind in range(1, n):
            minPrefix[n - 1 - ind] = min(nums[n - 1 - ind], minPrefix[n - ind])
        
        max_ = 0
        for ind in range(n):
            max_ = max(max_, nums[ind])
            if max_ - minPrefix[ind] <= k:
                return ind
        
        return -1
