class Solution:
    def digitProduct(self, num):
        product = min(num , 1)
        while num > 0:
            product *= num % 10
            num //= 10
        
        return product

    def smallestNumber(self, n: int, t: int) -> int:
        for num in range(n, n+11):
            if self.digitProduct(num) % t == 0:
                return num
