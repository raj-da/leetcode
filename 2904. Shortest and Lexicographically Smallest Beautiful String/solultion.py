class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)

        def compare(current, previous):
            if len(current) < len(previous):
                return current
            elif len(current) > len(previous):
                return previous

            for ind in range(len(current)):
                if current[ind] == '0' and previous[ind] == '1':
                    return current
                elif current[ind] == '1' and previous[ind] == '0':
                    return previous
            
            return previous


        # First Beautiful String
        left, right, count = 0, 0, 0
        while count < k and right < len(s):
            if s[left] == '0':
                left += 1
            if s[right] == '1':
                count += 1
            right += 1
        
        result = s[left:right] if count == k else ""
        
        # Search for smallest Beautiful String
        for right in range(right, n):
            count += int(s[right])
            while count > k or s[left] == '0':
                if s[left] == '1':
                    count -= 1
                left += 1
            
            result = compare(result, s[left:right+1])
        
        return result
