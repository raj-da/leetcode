class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        mat = [grid[row][:] for row in range(rows)]

        # Column prefix sum
        for r in range(rows):
            for c in range(1, cols):
                mat[r][c] += mat[r][c-1]
        
        # Row prefix sum
        for r in range(1, rows):
            for c in range(cols):
                mat[r][c] += mat[r-1][c]
        
        subMatricsCount = sum([mat[r][c] <= k for r in range(rows) for c in range(cols)])
        return subMatricsCount
