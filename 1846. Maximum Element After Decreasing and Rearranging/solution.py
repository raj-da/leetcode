class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1

        for ind in range(1, len(arr)):
            if abs(arr[ind] - arr[ind-1]) > 1:
                arr[ind] = arr[ind-1] + 1

        return arr[-1]
