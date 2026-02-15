class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        n, m = len(a), len(b)

        res = []
        rem = '0'
        for ind in range(1, min(n, m) + 1):
            if a[-ind] == b[-ind] == '1':
                res.append(rem)
                rem = '1'
            else:
                if a[-ind] != b[-ind]:
                    if rem == '1':
                        res.append('0')
                    else:
                        res.append('1')
                        rem = '0'
                else:
                    res.append(rem)
                    rem = '0'
        
        start = abs(n - m) - 1
        if max(n, m) <= len(a):
            for ind in range(start, -1, -1):
                if rem == a[ind] == '1':
                    res.append('0')
                elif rem == '1' or a[ind] == '1':
                    res.append('1')
                    rem = '0'
                else:
                    res.append('0')
                    rem = '0'

        if max(n, m) <= len(b):
            for ind in range(start, -1, -1):
                if rem == b[ind] == '1':
                    res.append('0')
                elif rem == '1' or b[ind] == '1':
                    res.append('1')
                    rem = '0'
                else:
                    res.append('0')
                    rem = '0'
        
        if rem == '1':
            res.append(rem)
        
        res.reverse()
        return ''.join(res)