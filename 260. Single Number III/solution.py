class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: XOR all numbers to get xor_result = a ^ b (where a and b are the unique ones)
        xor_result = reduce(xor, nums)

        # Step 2: Find any bit that is different between a and b
        # This bit will be set in xor_result, so we find the rightmost set bit
        distinguishing_bit = 1
        while xor_result & distinguishing_bit == 0:
            distinguishing_bit <<= 1

        # Step 3: Divide numbers into two groups based on distinguishing bit
        num1 = 0
        num2 = 0
        for num in nums:
            if num & distinguishing_bit:
                num1 ^= num  # Group 1
            else:
                num2 ^= num  # Group 2

        return [num1, num2]

# Time-Complexity: O(n)
# Space-Complexity: O(1)