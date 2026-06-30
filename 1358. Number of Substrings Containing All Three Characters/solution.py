class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        charCount = defaultdict(int)

        l, r = 0, 0

        while r < n:
            # Expand untile valid substring
            while r < n and len(charCount) < 3:
                charCount[s[r]] += 1
                r += 1
            
            # Add if valid substring
            if len(charCount) == 3:
                count += n - r + 1
            
            # Shrink while its a valid substring
            while len(charCount) == 3:
                charCount[s[l]] -= 1
                if charCount[s[l]] == 0:
                    del charCount[s[l]]
                
                if len(charCount) == 3:
                    count += n - r + 1
                
                l += 1
        return count
    
# Time complexity: O(n)
# Space complexity: O(1)
