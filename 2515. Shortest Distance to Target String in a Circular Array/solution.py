class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)

        def toTheRight(ind):
            if startIndex <= ind:
                return ind - startIndex
            else:
                return (n - startIndex) + ind
        
        def toTheLeft(ind):
            if startIndex >= ind:
                return startIndex - ind
            else:
                return (n - ind) + startIndex

        # store all indexs where a word is found
        indexs = defaultdict(list)
        for ind, word in enumerate(words):
            indexs[word].append(ind)

        # find min distance from startIndex to any target
        result = inf
        for ind in indexs[target]:
            result = min(result, toTheRight(ind)) # find min distance from the right
            result = min(result, toTheLeft(ind)) # find min distance from the left
        
        return result if result < inf else -1
        
