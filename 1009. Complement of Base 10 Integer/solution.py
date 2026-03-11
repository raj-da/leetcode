class Solution:
    def bitwiseComplement(self, n: int) -> int:
        compliment = 0 if n > 0 else 1
        bit = 0
        while 2**bit <= n:
            if n & (1 << bit) == 0:
                compliment += 2**bit
            bit += 1

        return compliment   
