class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_freq = 0
        dic = {'T': 0, 'F': 0}
        max_len = 0

        l = 0
        for r in range(len(answerKey)):
            dic[answerKey[r]] += 1
            max_freq = max(dic[answerKey[r]], max_freq)

            if (r - l + 1) - max_freq > k:
                dic[answerKey[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len
    
# Time complexity: O(n) for n = len(answerKey)
# Spacr complexity: O(1)