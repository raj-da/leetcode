class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx = 0
        prefixGcd = []
        for num in nums:
            mx = max(mx, num)
            prefixGcd.append(gcd(num, mx))
        prefixGcd.sort()
        
        res = 0
        l, r = 0, len(prefixGcd) - 1
        while l < r:
            res += gcd(prefixGcd[l], prefixGcd[r])
            l += 1
            r -= 1

        return res
