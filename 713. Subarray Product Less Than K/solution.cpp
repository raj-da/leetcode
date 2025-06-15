class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        // Edge case: If k is 0 or 1, no product of positive integers can be less than k
        if (k <= 1) {
            return 0;
        }

        int l = 0;         // Left pointer of the sliding window
        int product = 1;   // Current product of elements in the window
        int count = 0;     // Total count of valid subarrays

        // Iterate through the array with the right pointer
        for (int r = 0; r < nums.size(); r++) {
            product *= nums[r];  // Include nums[r] in the product

            // Shrink the window from the left until the product is less than k
            while (product >= k) {
                product /= nums[l];
                l++;
            }

            // For each valid window, the number of subarrays ending at index r is (r - l + 1)
            count += (r - l + 1);
        }

        return count;
    }
};
