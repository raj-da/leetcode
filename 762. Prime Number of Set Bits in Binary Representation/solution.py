class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prims = [2,3,5,7,11,13,17,19]

        count = 0
        for num in range(left, right+1):
            bits = bin(num).count("1")
            if bits in prims:
                count += 1
        return count
