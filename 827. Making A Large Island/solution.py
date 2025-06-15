class UnionFind:
    def __init__(self):
        self.size = defaultdict(lambda: 1)  # Tracks size of each component
        self.parent = {}  # Maps a node to its parent

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x]  # Ensure default size is initialized
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])  # Path compression
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
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 4-connected directions
        visited = set()
        island = UnionFind()

        # DFS to group all connected 1's using Union-Find
        def dfs(node):
            r, c = node
            island.union((r, c), (r, c))  # Initialize union for this node
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < rows and 0 <= new_c < columns:
                    if grid[new_r][new_c] == 1 and (new_r, new_c) not in visited:
                        visited.add((new_r, new_c))
                        island.union((r, c), (new_r, new_c))  # Union with neighbor
                        dfs((new_r, new_c))

        # 1. Build island components using Union-Find
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1 and (r, c) not in visited:
                    visited.add((r, c))
                    dfs((r, c))

        largest_size = 0  # Will track max island size after possible flip

        # 2. Try flipping each 0 to 1 and compute resulting island size
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 0:
                    size = 0
                    parents = set()
                    for dr, dc in directions:
                        new_r, new_c = r + dr, c + dc
                        if 0 <= new_r < rows and 0 <= new_c < columns:
                            if grid[new_r][new_c] == 1:
                                parents.add(island.find((new_r, new_c)))
                    # Sum sizes of all unique neighboring islands
                    for parent in parents:
                        size += island.size[parent]
                    largest_size = max(largest_size, size + 1)  # +1 for flipped cell

        # 3. Handle case where grid has no zeroes (already full of 1s)
        return max(largest_size, max(island.size.values(), default=0))
