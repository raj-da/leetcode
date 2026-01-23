class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0
        for ind, char in enumerate(s):
            result += (ind + 1)*(26 - (ord(char) - 97))
        return result