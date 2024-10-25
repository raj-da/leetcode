from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        P_length = len(p)
        # List to store the starting indices of anagrams found
        anagram_indices  = []
        # Dictionary to count the frequency of characters in 'p'
        p_count = Counter(p)
        # Dictionary to count the frequency of characters in the current window of 's'
        window_count = {}

        # If 'p' is longer than 's' return an empty list
        if P_length > len(s):
            return []
        
        # Creating the first window
        l = 0
        for r in range(P_length):
            window_count[s[r]] = 1 + window_count.get(s[r], 0)

        # Check if the first window matches the character count in 'p'
        if window_count == p_count:
            anagram_indices .append(l)

        # Shifting the window to check for anagrams in the rest of the string
        for r in range(P_length, len(s)):
            # Add the next character to the window
            window_count[s[r]] = 1 + window_count.get(s[r], 0)
            # Remove the leftmost character from the window
            window_count[s[l]] -= 1
            if window_count[s[l]] == 0:
                window_count.pop(s[l])

            # Move the left pointer
            l += 1
            
            # check if the current window mathces the character count in 'p'
            if window_count == p_count:
                anagram_indices .append(l)

        return anagram_indices 