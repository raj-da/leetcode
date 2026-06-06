class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]*(n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]

        answer = [0 for _ in range(n)]
        for i in range(1, n + 1):
            left = prefix[i - 1]
            right = prefix[n] - prefix[i]
            answer[i - 1] = abs(left - right)

        return answer
