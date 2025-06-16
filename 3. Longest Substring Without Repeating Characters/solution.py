class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()  # To store characters in the current window
        longest = 0   # Track the maximum length found

        l = 0  # Left pointer of the sliding window
        for r in range(len(s)):  # Right pointer moves over each character
            while s[r] in seen:
                seen.remove(s[l])  # Remove characters from the left until s[r] is not in seen
                l += 1
            seen.add(s[r])  # Add current character to the set
            longest = max(longest, r - l + 1)  # Update max length
        return longest
    
# Time-Complexity: O(n)
# Space-Complexity: O(1) at worst it is going to be O(26) which is going to be constant space