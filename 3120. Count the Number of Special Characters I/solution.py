class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        chars = set(word)
        res = 0

        s = set()
        for char in chars:
            if char.lower() in s:
                res += 1
            s.add(char.lower())
        return res
