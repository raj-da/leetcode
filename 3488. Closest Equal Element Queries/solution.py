class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)

        def disToTheRight(startIndex, ind):
            ''' find distance from startIndex to ind index moving to the right '''
            if startIndex <= ind:
                return ind - startIndex
            else:
                return (n - startIndex) + ind
        
        def disToTheLeft(startIndex, ind):
            ''' find distance from startIndex to ind index moving to the left '''
            if startIndex >= ind:
                return startIndex - ind
            else:
                return (n - ind) + startIndex
        
        # map a number to its indexs
        indexs = defaultdict(list)
        for ind, num in enumerate(nums):
            indexs[num].append(ind)
        
        result = []
        for query in queries:
            num = nums[query]
            inds = indexs[num]
            m = len(inds)
            if m == 0:
                result.append(-1)
            else:
                curr = bisect_left(inds, query)
                dis = disToTheRight(query, (curr + 1) % m)
                dis = min(dis, disToTheLeft(query, curr - 1))
                result.append(dis)


        return result
