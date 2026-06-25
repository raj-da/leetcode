class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = 0
        for l in range(n):
            count = 0
            for r in range(l, n):
                if nums[r] == target:
                    count += 1
                if count > (r - l + 1)//2:
                    res += 1
        
        return res
