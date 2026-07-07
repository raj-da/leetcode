class Solution:
    def sumAndMultiply(self, n: int) -> int:
        _sum = 0
        xDigits = []
        
        while n > 0:
            digit = n % 10
            n //= 10

            if digit > 0:
                _sum += digit
                xDigits.append(digit)
        
        x = 0
        for ind in range(len(xDigits)-1, -1, -1):
            x = x*10 + xDigits[ind]

        return x * _sum
