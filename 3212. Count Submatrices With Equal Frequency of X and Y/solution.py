class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        charToInt = {'X': -1, 'Y': 1, '.': 0}
        mat = [[charToInt[grid[r][c]] for c in range(cols)] for r in range(rows)]
        xCount = [[1 if grid[r][c] == 'X' else 0 for c in range(cols)] for r in range(rows)]

        # Column Prefix sum
        for r in range(rows):
            for c in range(1, cols):
                mat[r][c] += mat[r][c-1]
                xCount[r][c] += xCount[r][c-1]
        
        # Row Prefix sum
        for r in range(1, rows):
            for c in range(cols):
                mat[r][c] += mat[r-1][c]
                xCount[r][c] += xCount[r-1][c]
        
        subMatricesCount = sum([mat[r][c] == 0 and xCount[r][c] >= 1 for r in range(rows) for c in range(cols)])
        return subMatricesCount
