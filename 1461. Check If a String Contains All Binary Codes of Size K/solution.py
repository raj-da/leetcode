class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        if k > len(s):
            return False
        
        sett = set([s[:k]])

        l = 1
        for r in range(k, len(s)):
            sett.add(s[l:r+1])
            l += 1
        
        return len(sett) == 2**k
