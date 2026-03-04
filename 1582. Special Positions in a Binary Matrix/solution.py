class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])

        rowPrifix = [[0]*cols for _ in range(rows)]
        colPrifix = [[0]*cols for _ in range(rows)]

        # row prifix
        for r in range(rows):
            for c in range(cols):
                rowPrifix[r][c] += rowPrifix[r][c-1] + mat[r][c]
        
        # column prifix
        for r in range(rows):
            for c in range(cols):
                colPrifix[r][c] += colPrifix[r-1][c] + mat[r][c]
        
        result = 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1:
                    result += int(rowPrifix[r][cols-1] == 1 and colPrifix[rows-1][c] == 1)
        
        return result
