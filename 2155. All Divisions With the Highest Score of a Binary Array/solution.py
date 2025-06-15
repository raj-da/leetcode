class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Compute prefix sum of 1s
        prefix_ones = [0] * (n + 1)
        for i in range(n):
            prefix_ones[i + 1] = prefix_ones[i] + nums[i]

        max_score = -1
        result_indices = []

        total_ones = prefix_ones[-1]

        # Try all possible split positions from 0 to n
        for i in range(n + 1):
            left_zeros = i - prefix_ones[i]
            right_ones = total_ones - prefix_ones[i]
            score = left_zeros + right_ones

            if score > max_score:
                max_score = score
                result_indices = [i]
            elif score == max_score:
                result_indices.append(i)

        return result_indices
