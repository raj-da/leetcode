class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])

        # Row prefix sum
        for r in range(n):
            for c in range(1, m):
                grid[r][c] += grid[r][c-1]

        # Column prefix sum
        for r in range(1, n):
            for c in range(m):
                grid[r][c] += grid[r-1][c]

        # Horozontal Cut
        for r in range(n-1):
            if grid[-1][-1] == 2*grid[r][-1]:
                return True

        # Vertical Cut
        for c in range(m-1):
            if grid[-1][-1] == 2*grid[-1][c]:
                return True
        
        return False
