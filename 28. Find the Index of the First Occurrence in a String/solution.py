class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        MOD = 10**9 + 7
        base = 27

        def encode(char):
            return ord(char) - 96
        
        def add_last(hash_value, char):
            return ((hash_value * base) + encode(char)) % MOD
        
        def poll_first(hash_value, char, base_power):
            return (hash_value - (encode(char) * base_power)) % MOD
        
        n, h = len(needle), len(haystack)
        if n > h:
            return -1
        
        # --- Precompute base powers ---
        base_power = [1]*(n+1)
        for ind in range(1, n+1):
            base_power[ind] = (base_power[ind-1] * base) % MOD
        
        # --- Hash needle and first window ---
        target, windowHash = 0, 0
        for ind in range(n):
            target = add_last(target, needle[ind])
            windowHash = add_last(windowHash, haystack[ind])
        
        # --- Check first window ---
        if target == windowHash:
            if needle == haystack[:n]:
                return 0
        
        # --- Slide the window ---
        l = 0
        for r in range(n, h):
            windowHash = add_last(windowHash, haystack[r])
            windowHash = poll_first(windowHash, haystack[l], base_power[n])
            l += 1

            # --- Check if we have a match ---
            if target == windowHash:
                if needle == haystack[l:r+1]:
                    return l
        return -1

