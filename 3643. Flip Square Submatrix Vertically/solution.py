class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for c in range(y, y + k):
            u, b = x, x + k - 1
            while u < b:
                grid[u][c], grid[b][c] = grid[b][c], grid[u][c]
                u += 1
                b -= 1
        
        return grid
