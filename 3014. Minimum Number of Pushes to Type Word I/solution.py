class Solution:
    def minimumPushes(self, word: str) -> int:
        pushCount = 0
        for ind in range(1, len(word) + 1):
            pushCount += ceil(ind/8)

        return pushCount
