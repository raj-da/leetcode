class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums = set(nums)

        res = ""
        def backtrack(s):
            nonlocal res
            if len(s) == len(nums):
                if s not in nums:
                    res = s
                return
            
            backtrack(s + '0')
            backtrack(s + '1')

        backtrack("")
        return res
