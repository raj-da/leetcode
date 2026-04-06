class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        left = defaultdict(int)
        right = Counter(nums)
        
        dom = -1
        for ind in range(n-1):
            count += 1
            left[nums[ind]] += 1
            right[nums[ind]] -= 1
            if right[nums[ind]] == 0:
                del right[nums[ind]]

            if left[nums[ind]] > count // 2:
                dom = nums[ind]
                if right[dom] > (n - count) // 2:
                    return ind

        return -1  
