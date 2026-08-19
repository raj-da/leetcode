class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        s = set()

        # Check the first window
        for right in range(k):
            if nums[right] not in s:
                counts[nums[right]] += 1
                s.add(nums[right])
                
        
        # Shift the window
        left = 1
        for right in range(k, len(nums)):
            s.clear()
            for ind in range(left, right + 1):
                if nums[ind] not in s:
                    counts[nums[ind]] += 1
                    s.add(nums[ind])
            left += 1
        
        # Find largest almost missing integer
        x = -1
        for num in nums:
            if counts[num] == 1:
                x = max(x, num)
        
        return x
