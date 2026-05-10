class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)

        memo = [None for _ in range(n)]
        def dp(i):
            if i == n - 1:
                return 0
            
            if memo[i]:
                return memo[i]
            
            res = -inf
            for j in range(i + 1, n):
                if -target <= nums[j] - nums[i] <= target:
                    res = max(res, dp(j))
            
            memo[i] = res + 1
            
            return res + 1
        
        return max(-1, dp(0))
