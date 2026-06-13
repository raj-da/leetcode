class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = ''
        for word in words:
            val = sum(weights[ord(char) - 97]  for char in word) % 26
            res += chr(97 + 25 - val)
        
        return res
