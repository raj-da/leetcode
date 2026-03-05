class Solution:
    def minOperations(self, s: str) -> int:
        def operations(pattern):
            count = 0
            for ind in range(len(s)):
                if s[ind] != pattern[ind]:
                    count += 1
            return count
        
        pattern1 = ['0']
        pattern2 = ['1']

        for _ in range(len(s) - 1):
            pattern1.append(str((int(pattern1[-1]) + 1)%2))
            pattern2.append(str((int(pattern2[-1]) + 1)%2))

        return min(operations(pattern1), operations(pattern2))
