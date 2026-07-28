class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        charCount = Counter(s)
        sortedKeys = sorted(charCount.keys())

        result = [""]*n
        midIndex = n//2

        ind = 0
        for char in sortedKeys:
            count = charCount[char]

            if count % 2 != 0:
                result[midIndex] = char
                count -= 1
            
            for _ in range(count//2):
                result[ind] = char
                result[n - ind - 1] = char
                ind += 1
        
        return ''.join(result)
