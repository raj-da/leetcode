class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        res = 0
        for num in range(max(101, num1), num2+1):
            num = str(num)
            for ind in range(1, len(num)-1):
                if num[ind] > num[ind-1] and num[ind] > num[ind+1]:
                    res += 1
                elif num[ind] < num[ind-1] and num[ind] < num[ind+1]:
                    res += 1
        
        return res
