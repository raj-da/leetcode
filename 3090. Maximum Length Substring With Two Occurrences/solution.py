class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_len = 0
        charCount = defaultdict(int)

        left = 0
        for right, char in enumerate(s):
            charCount[char] += 1
            while charCount[char] > 2:
                charCount[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len
