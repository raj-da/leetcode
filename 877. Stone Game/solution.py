class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True

        # ---------- Botton up ------
        # n = len(piles)
        # dp = [[0] * n for _ in range(n)]

        # for diag in range(1, n):  # diagnoal number i.e r - l
        #     for l in range(n - diag):
        #         r = l + diag
        #         left = piles[l] if (r - l + 1)%2 == 0 else 0
        #         right = piles[r] if (r - l + 1)%2 == 0 else 0

        #         dp[l][r] = max(dp[l+1][r] + left, dp[l][r-1] + right)
        # return dp[0][n-1] > sum(piles)//2


        # ---------- Top Down --------
        # memo = {}
        # def dp(l, r):
        #     if l > r:
        #         return 0
            
        #     if (l,r) in memo:
        #         return memo[(l,r)]

        #     left = piles[l] if (r - l + 1) % 2 == 0 else 0
        #     right = piles[r] if (r - l + 1) % 2 == 0 else 0

        #     memo[(l,r)] = max(dp(l + 1, r) + left, dp(l, r - 1) + right)
        #     return memo[(l,r)]
        
        # return dp(0, len(piles) - 1) > sum(piles)//2
