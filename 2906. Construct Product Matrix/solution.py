class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        rows, cols = len(grid), len(grid[0])
        result = [[1]*cols for _ in range(rows)]

        suffix = 1
        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                result[r][c] = suffix
                suffix = (suffix * grid[r][c]) % MOD

        postfix = 1
        for r in range(rows):
            for c in range(cols):
                result[r][c] = (result[r][c] * postfix) % MOD 
                postfix = (postfix * grid[r][c]) % MOD

        return result
