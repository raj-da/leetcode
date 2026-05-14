class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        nums.sort()
        n = len(nums) - 1

        val = 1
        for ind in range(n):
            if nums[ind] != val:
                return False
            val += 1

        return nums[-1] == nums[-2]
