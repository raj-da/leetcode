class Solution:
    def minChanges(self, s: str) -> int:
        c = 0
        for r in range(1, len(s), 2):
            if s[r] != s[r - 1]:
                c += 1

        return c
             