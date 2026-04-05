class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dirCount = Counter(moves)
        return (dirCount['L'] == dirCount['R']) and (dirCount['U'] == dirCount['D'])
