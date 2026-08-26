class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums.sort()

        result = k
        for num in nums:
            if num == result:
                result += k
            elif num > result:
                return result
        
        return result
