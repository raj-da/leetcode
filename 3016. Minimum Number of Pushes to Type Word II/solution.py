class Solution:
    def minimumPushes(self, word: str) -> int:
        charCount = Counter(word)
        sortedKeys = sorted(charCount.keys(), key= lambda char: -charCount[char])

        pushCount = 0
        for ind in range(1, len(sortedKeys)+1):
            charPosition = ceil(ind/8)
            char = sortedKeys[ind-1]
            pushCount += charCount[char]*charPosition
        
        return pushCount
