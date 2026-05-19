class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        l, r = 0, 0
        n, m = len(nums1), len(nums2)
        while l < n and r < m:
            a, b = nums1[l], nums2[r]
            if a == b:
                return nums1[l]
            elif a > b:
                r += 1
            else:
                l += 1
        
        return -1
