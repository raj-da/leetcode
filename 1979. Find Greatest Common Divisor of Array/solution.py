class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = max(nums)
        b = min(nums)

        if a == b:
            return a
        
        def gdc(a, b):
            if b == 0:
                return a
            
            return gdc(b, a%b)
        
        return gdc(a, b)
