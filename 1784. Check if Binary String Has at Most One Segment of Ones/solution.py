class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # n = len(s)
        # segmentCount = 0

        # l, r = 0, 0
        # while r < n:
        #     while l < n and s[l] != '1':
        #         l += 1
        #     r = l
        #     while r < n and s[r] != '0':
        #         r += 1
        #     if r - l > 0:
        #         segmentCount += 1
        #     l = r 

        # return segmentCount <= 1

        return '01' not in s
