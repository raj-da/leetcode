class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        array = [grid[r][c] for r in range(rows) for c in range(cols)]

        n = len(array)
        shifted_array =  array[n-(k%n):] + array[:n-(k%n)]
        
        return [shifted_array[r*cols:(r*cols+cols)] for r in range(rows)]
