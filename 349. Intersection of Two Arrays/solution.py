class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        a = set(nums1)
        b = set(nums2)

        for num in nums1:
            if num in a and num in b:
                res.add(num)
        
        return list(res)
