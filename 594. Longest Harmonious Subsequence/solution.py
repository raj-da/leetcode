class Solution:
    def findLHS(self, nums: List[int]) -> int:
        frequency = Counter(nums)  # Count frequency of each number
        result = 0  # Initialize result to store max length

        for num in frequency:
            # Check if num - 1 exists, to form a harmonious pair
            if num - 1 in frequency:
                # Update result with max of current or new pair length
                result = max(result, frequency[num] + frequency[num - 1])

        return result


# Time Complexity: O(n)
# Space Complexity: O(n)