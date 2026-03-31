class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        return [ind + 1 for ind in range(len(nums)) if ind + 1 not in s]
