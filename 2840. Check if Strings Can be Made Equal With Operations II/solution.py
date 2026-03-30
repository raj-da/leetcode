class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1Even = sorted([s1[ind] for ind in range(0, n, 2)])
        s1Odd = sorted([s1[ind] for ind in range(1, n, 2)])

        s2Even = sorted([s2[ind] for ind in range(0, n, 2)])
        s2Odd = sorted([s2[ind] for ind in range(1, n, 2)])

        return s1Even == s2Even and s1Odd == s2Odd
