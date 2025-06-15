class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_ = weights[0]
        max_ = 0
        for weight in weights:
            min_ = max(min_, weight)
            max_ += weight

        # helper function to validate a weight
        def is_valid(value):
            count = 0
            sum_ = 0
            for weight in weights:
                sum_ += weight
                if sum_ > value:
                    count += 1
                    sum_ = weight
            return count + 1

        l, r = min_, max_
        while l <= r:
            m = (l + r)//2
            val = is_valid(m)
            if val > days:
                l = m + 1
            else:
                ans = m
                r = m - 1
        return ans
    

# Time complexity: O(nlogm) n for len(weight) and k for max_
# space complexity: O(1)