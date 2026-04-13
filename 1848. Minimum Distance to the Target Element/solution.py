class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = inf
        for ind, num in enumerate(nums):
            if num == target:
                res = min(res, abs(ind - start))
        return res
