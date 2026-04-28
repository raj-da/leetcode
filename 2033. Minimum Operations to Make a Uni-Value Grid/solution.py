class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = [grid[r][c] for r in range(len(grid)) for c in range(len(grid[0]))]
        rem = nums[0] % x
        # Check if equalizing is possible 
        for num in nums:
            if num % x != rem:
                return -1
        
        nums.sort()
        # Find midean value
        n = len(nums)
        val = nums[n//2]

        res = 0
        for num in nums:
            res += abs(val - num) // x
        
        return res
