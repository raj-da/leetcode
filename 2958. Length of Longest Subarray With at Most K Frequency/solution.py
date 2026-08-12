class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        max_len = 1
        
        left = 0
        for right, num in enumerate(nums):
            counts[num] += 1

            while counts[num] > k:
                counts[nums[left]] -= 1
                left += 1
        
            max_len = max(max_len, right - left + 1)
        
        return max_len
