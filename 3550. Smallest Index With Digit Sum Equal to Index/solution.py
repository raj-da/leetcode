class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digitSum(num):
            res = 0
            while num > 0:
                res += num % 10
                num //= 10
            return res
        
        for ind, num in enumerate(nums):
            if ind == digitSum(num):
                return ind
        
        return -1
