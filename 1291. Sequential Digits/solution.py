class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        res = []

        for s in range(len(str(low)), len(str(high)) + 1):
            l = 0
            for r in range(s, len(digits)+1):
                t = int(digits[l:r])
                if low <= t <= high:
                    res.append(int(digits[l:r]))
                l += 1
        
        return res
