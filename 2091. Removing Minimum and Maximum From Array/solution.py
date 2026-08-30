class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        
        minInd, maxInd = 0, 0
        for ind, num in enumerate(nums):
            if num < nums[minInd]:
                minInd = ind
            if num > nums[maxInd]:
                maxInd = ind
        
        left = min(minInd, maxInd)
        right = max(minInd, maxInd)

        return min(left + 1 + n - right, right + 1, n - left)
