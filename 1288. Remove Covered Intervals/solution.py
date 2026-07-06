class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda interval: (interval[0], -interval[1]))
        
        count = 1
        cur = 0
        for ind in range(1, len(intervals)):
            if intervals[ind][0] < intervals[cur][0] or intervals[ind][1] > intervals[cur][1]:
                cur = ind
                count += 1
        return count
