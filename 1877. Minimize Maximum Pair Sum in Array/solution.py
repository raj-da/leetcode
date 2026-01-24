class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        min_max_sum = 0
        
        l, r = 0, len(nums) - 1
        while l < r:
            min_max_sum = max(min_max_sum, nums[r] + nums[l])
            l += 1
            r -= 1

        return min_max_sum