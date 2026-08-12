class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        subArrayCharCount = defaultdict(int)
        longestLength = 1
        
        l = 0
        for r, char in enumerate(nums):
            subArrayCharCount[char] += 1
            while subArrayCharCount[char] > k:
                subArrayCharCount[nums[l]] -= 1
                l += 1
        
            longestLength = max(longestLength, r - l + 1)
        
        return longestLength
