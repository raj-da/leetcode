class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        low, high = 100, 1
        numbers = set(nums)
        
        for num in nums:
            low = min(num, low)
            high = max(num, high)
        
        missingNumbers = []
        for num in range(low, high+1):
            if num not in numbers:
                missingNumbers.append(num)

        return missingNumbers
