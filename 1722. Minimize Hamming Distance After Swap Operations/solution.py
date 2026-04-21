class UnionFind:
    def __init__(self):
        self.size = defaultdict(lambda:1)
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            return x
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            if self.size[x] >= self.size[y]:
                self.parent[y] = x
                self.size[x] += self.size[y]
            else:
                self.parent[x] = y
                self.size[y] += self.size[x]

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:

        n = len(source)
        uf = UnionFind()

        for i, j in allowedSwaps:
            uf.union(i, j)

        components = defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            components[root].append(i)

        mismatch_count = 0
        for indices in components.values():
            source_count = Counter(source[i] for i in indices)
            target_count = Counter(target[i] for i in indices)

            for value in source_count:
                unmatched = source_count[value] - target_count[value]
                if unmatched > 0:
                    mismatch_count += unmatched

        return mismatch_count
