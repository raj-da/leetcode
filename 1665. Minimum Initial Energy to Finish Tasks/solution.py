class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda task: task[1] - task[0], reverse=True)
        l, r = 0, 0
        for _, minimum in tasks:
            l = max(l, minimum)
            r += minimum
        
        def isValid(val):
            for actual, minimum in tasks:
                if val < minimum:
                    return False
                val -= actual
            return True
        
        while l <= r:
            m = (l + r)//2
            if isValid(m):
                r = m - 1
            else:
                l = m + 1
        return r + 1
