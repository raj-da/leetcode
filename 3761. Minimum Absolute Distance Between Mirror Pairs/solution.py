class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(num):
            res = 0
            while num > 0:
                res = res*10 + num%10
                num //= 10
            return res
        
        hash = {}
        res = inf
        for ind, num in enumerate(nums):
            if num in hash:
                if num in hash:
                    res = min(res, ind - hash[num])
            hash[reverse(num)] = ind
        
        return res if res < inf else -1
