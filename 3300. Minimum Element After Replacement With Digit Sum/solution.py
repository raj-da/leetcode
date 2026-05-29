class Solution:
    def minElement(self, nums: List[int]) -> int:
        def digitSum(num):
            res = 0
            while num > 0:
                res += num%10
                num //= 10
            return res
        
        minElement = inf
        for num in nums:
            minElement = min(minElement, digitSum(num))
        
        return minElement
