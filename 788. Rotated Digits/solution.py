class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid = {'0':'0', '1':'1', '8':'8', '2':'5', '5':'2', '6':'9', '9':'6'}
                
        def isValid(n):
            orig = str(n)
            rot = ''
            for dig in orig:
                if dig not in valid:
                    return False
                rot += valid[dig]
            return rot != orig

        
        return sum(isValid(i) for i in range(1, n + 1))
        
