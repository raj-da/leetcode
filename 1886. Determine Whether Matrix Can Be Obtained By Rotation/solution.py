class Solution:

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        # before rotation
        n = len(mat)
        same = True
        for r in range(n):
            for c in range(n):
                if mat[r][c] != target[r][c]:
                    same = False
                    break
            if not same:
                break


        if not same:
            # 1st rotation
            same = True
            for r in range(n):
                for c in range(n):
                    if mat[n - 1 - c][r] != target[r][c]:
                        same = False
                        break
                if not same:
                    break

        if not same:
            # 2nd rotation
            same = True
            for r in range(n):
                for c in range(n):
                    if mat[n - 1 -r][n - 1 - c] != target[r][c]:
                        same = False
                        break
                if not same:
                    break

        if not same:
            # 3rd rotation
            same = True
            for r in range(n):
                for c in range(n):
                    if mat[c][n - 1 - r] != target[r][c]:
                        same = False
                        break
                if not same:
                    break

        if same:
            return True
        else:
            return False

        
