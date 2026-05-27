class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowerIndex = {}
        upperIndex = defaultdict(lambda: -1)

        for ind, char in enumerate(word):
            if char.isupper():
                if char not in upperIndex:
                    upperIndex[char.upper()] = ind
            else:
                lowerIndex[char] = ind
        
        res = 0
        for char in set(word):
            if char.islower():
                res += lowerIndex[char] < upperIndex[char.upper()]

        return res
