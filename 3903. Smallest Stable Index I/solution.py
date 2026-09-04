class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxPrefix = nums[:]
        minPrefix = nums[:]
        for ind in range(1, n):
            maxPrefix[ind] = max(nums[ind], maxPrefix[ind-1])
            minPrefix[n - 1 - ind] = min(nums[n - 1 - ind], minPrefix[n - ind])
        
        for ind in range(n):
            if maxPrefix[ind] - minPrefix[ind] <= k:
                return ind
        
        return -1
