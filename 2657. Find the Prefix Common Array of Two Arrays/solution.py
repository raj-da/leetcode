class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        freq = [0]*(n+1)
        res = [0]*n

        for ind in range(n):
            freq[A[ind]] += 1
            if freq[A[ind]] == 2:
                res[ind] += 1

            freq[B[ind]] += 1
            if freq[B[ind]] == 2:
                res[ind] += 1
            
            if ind > 0:
                res[ind] += res[ind-1]
        
        return res
        
