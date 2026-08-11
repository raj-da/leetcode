class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefixSum = nums[0]
        for ind in range(1, len(nums)):
            if nums[ind] == nums[ind-1] + 1:
                prefixSum += nums[ind]
            else:
                break
        
        nums.sort()
        x = prefixSum
        for num in nums:
            x += int(x == num)
        
        return x
