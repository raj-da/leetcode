class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        value_indices_map = defaultdict(list)
        total_pairs = 0

        for current_index, value in enumerate(nums):
            # For each previous index with the same value, check the condition
            for prev_index in value_indices_map[value]:
                if (current_index * prev_index) % k == 0:
                    total_pairs += 1
            # Store current index for this value
            value_indices_map[value].append(current_index)
        
        return total_pairs
