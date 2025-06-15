class Solution:
    def countSubarrays(self, nums, k: int) -> int:
        max_val = max(nums)  # Find the maximum element in the array
        total_subarrays = 0  # To store the final count of valid subarrays
        max_count_in_window = 0  # Number of times max_val appears in current window
        left = 0  # Left pointer of the sliding window
        extra_left_elements = 0  # Count of extra elements before the first max_val in current window
        n = len(nums)

        # Iterate with the right pointer
        for right in range(n):
            if nums[right] == max_val:
                max_count_in_window += 1

            # When we have exactly k max_val elements in window
            if max_count_in_window == k:
                # Move left pointer to the first max_val
                while nums[left] != max_val:
                    extra_left_elements += 1
                    left += 1

                # Now we found the first max_val, shrink the window
                left += 1
                max_count_in_window -= 1

                # Count subarrays using current window:
                # (extra_left_elements + 1) options on the left
                # (n - right - 1 + 1) = (n - right) options on the right
                remaining_right_options = n - right - 1
                total_subarrays += (extra_left_elements + 1) * (remaining_right_options + 1)

                # Reset extra left elements for next window
                extra_left_elements = 0

        return total_subarrays
