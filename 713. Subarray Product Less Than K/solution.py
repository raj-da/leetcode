class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        # Edge case: If k is 0 or 1, no product of positive integers can be < k
        if k <= 1:
            return 0

        l = 0              # Left pointer of the sliding window
        product = 1        # Current product of the window
        count = 0          # Total number of valid subarrays

        # Iterate over each element using the right pointer
        for r in range(len(nums)):
            product *= nums[r]  # Expand the window by multiplying the current element

            # While the product is greater than or equal to k, shrink the window from the left
            while product >= k:
                product /= nums[l]
                l += 1

            # For each valid window, the number of subarrays ending at index r is (r - l + 1)
            # This is because all subarrays from l to r, (l+1) to r, ..., r to r are valid
            count += (r - l + 1)

        return count

# Time Complexity: O(n) — Each element is visited at most twice (once by r, once by l)
# Space Complexity: O(1) — Uses constant extra space
