class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        count = Counter(moves)
        return abs(count['L'] - count['R']) + count['_']
