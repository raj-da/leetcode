class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        count = 0
        res = ""
        string = []

        def backtrack(ind):
            nonlocal res, count
            if count == k:
                return

            if ind == n:
                count += 1
                res = ''.join(string) if count == k else ""
                return

            
            for char in ['a', 'b', 'c']:
                if (not string) or (string[-1] != char):
                    string.append(char)
                    backtrack(ind+1)
                    string.pop()

        backtrack(0)
        return res
