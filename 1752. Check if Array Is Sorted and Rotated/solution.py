class Solution:
    def check(self, nums: List[int]) -> bool:
        original = sorted(nums)
        x = 0
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                x = i
                break

        for i in range(len(original)):
            if original[i] != nums[(i+x) % len(original)]:
                return False

        return True
