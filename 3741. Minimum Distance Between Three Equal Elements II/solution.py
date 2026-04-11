class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indexs = defaultdict(list)
        for ind, num in enumerate(nums):
            indexs[num].append(ind)

        result = inf
        for array in indexs.values():
            n = len(array)
            l = 0
            while n - l >= 3:
                dis = (array[l+1] - array[l]) + (array[l+2] - array[l+1]) + (array[l+2] - array[l])
                result = min(result, dis)
                l += 1

        return result if result < inf else -1
