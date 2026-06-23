class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = []
    
    def add(self, child: Node):
        self.children.append(child)

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        # Build the tree
        nodes = {}
        for u, v in edges:
            nodeU = nodes[u] if u in nodes else Node(u)
            nodeV = nodes[v] if v in nodes else Node(v)

            # Connect nodes
            nodeV.add(nodeU)
            nodeU.add(nodeV)
            
            if u not in nodes:
                nodes[u] = nodeU
            if v not in nodes:
                nodes[v] = nodeV


        MOD = 10**9 + 7
        visited = [False] * (len(edges) + 2) # offset index by 1 for node (1 to n)
        que = deque([nodes[1]])

        visited[1] = True
        maxLevel = 0
        while que:
            for _ in range(len(que)):
                node = que.popleft()
                for child in node.children:
                    if not visited[child.val]:
                        visited[child.val] = True
                        que.append(child)
            maxLevel += 1
        
        maxLevel -= 1
        return 2**(maxLevel - 1) % MOD
