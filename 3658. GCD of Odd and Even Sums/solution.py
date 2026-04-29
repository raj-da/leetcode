class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = 0
        for num in range(1, 2*n, 2):
            sumOdd += num
        
        sumEven = 0
        for num in range(2, 2*n + 1, 2):
            sumEven += num

        return gcd(sumOdd, sumEven)
