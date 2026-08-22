class Solution:
    def checkDivisibility(self, n: int) -> bool:
        def divisors(n):
            _sum = 0
            _product = 1
            while n > 0:
                lastDigit = n % 10
                _sum += lastDigit
                _product *= lastDigit
                n //= 10
            
            return _sum, _product

        _sum, _product = divisors(n)
        return n % (_sum + _product) == 0
