class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        for i in range(0, len(s), k):
            group = ""
            j = i
            while j < len(s) and j - i < k:
                group += s[j]
                j += 1
            group += fill*(k - len(group))
            res.append(group)
        
        return res
