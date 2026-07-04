#______________________Union Find__________________________#
class UnionFind:
    def __init__(self, n):
        # Initialize size, parent, and weight arrays for Union-Find
        self.size = [1 for _ in range(n + 1)]  # Size of each component
        self.parent = [i for i in range(n + 1)]  # Initially, each node is its own parent
        self.weight = [float('inf') for i in range(n + 1)]  # Minimum edge weight in the component

    def find(self, x):
        # Path compression: find the root of x and flatten the tree
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])  # Recursively find and compress
        return self.parent[x]

    def union(self, x, y, weight):
        # Union two sets and maintain the minimum edge weight in the resulting component
        x, y = self.find(x), self.find(y)
        if x != y:
            if self.size[x] >= self.size[y]:
                # Attach smaller tree under larger one
                self.parent[y] = x
                # Update the min edge weight in the new component
                self.weight[x] = min(self.weight[x], self.weight[y], weight)
                self.size[x] += self.size[y]
            else:
                self.parent[x] = y
                self.weight[y] = min(self.weight[x], self.weight[y], weight)
                self.size[y] += self.size[x]
        else:
            # If they are already connected, still update the min weight
            self.weight[x] = min(self.weight[x], weight)

    def min_weight(self, x):
        # Return the minimum weight in the component that includes x
        parent = self.find(x)
        return self.weight[parent]

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Approach: Union-Find
        tree = UnionFind(n)
        # Union all roads into connected components
        for node1, node2, weight in roads:
            tree.union(node1, node2, weight)

        # Return the minimum edge weight in the component of city 1
        return tree.min_weight(1)

        # Alternative Approach: BFS
        # graph = defaultdict(list)
        # for node1, node2, weight in roads:
        #     graph[node1].append((node2, weight))
        #     graph[node2].append((node1, weight))

        # score = float('inf')
        # visited = set([1])
        # que = deque([1])

        # while que:
        #     for _ in range(len(que)):
        #         node = que.popleft()
        #         for neighbour, weight in graph[node]:
        #             score = min(score, weight)
        #             if neighbour not in visited:
        #                 visited.add(neighbour)
        #                 que.append(neighbour)

        # return score


# Union Find without Class object
# class Solution:
#     def minScore(self, n: int, roads: List[List[int]]) -> int:

#         # --- Union Find ---
#         parent = [node for node in range(n + 1)]
#         count = [1] * (n+1)

#         def findParent(node):
#             if node == parent[node]:
#                 return node
            
#             parent[node] = findParent(parent[node])
#             return parent[node]

        
#         def connect(node1, node2):
#             parent1 = findParent(node1)
#             parent2 = findParent(node2)
            
#             if count[parent1] >= count[parent2]:
#                 count[parent1] += count[parent2]
#                 parent[parent2] = parent1 
#             else:
#                 count[parent2] += count[parent1]
#                 parent[parent1] = parent2
        
#         def connected(node1, node2):
#             return findParent(node1) == findParent(node2)
        

#         # --- Solution ---
        
#         for node1, node2, _ in roads:
#             connect(node1, node2)
        
#         minValue = inf
#         for node1, node2, value in roads:
#             if connected(1, node1):
#                 minValue = min(minValue, value)
        
#         return minValue
