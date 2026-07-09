class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        parent = [node for node in range(n)]
        count = [1] * (n)

        def find(node):
            if parent[node] == node:
                return node
            
            parent[node] = find(parent[node])
            return parent[node]
        
        def join(n1, n2):
            p1, p2 = find(n1), find(n2)
            if count[p1] >= count[p2]:
                parent[p2] = p1
                count[p1] += count[p2]
            else:
                parent[p1] = p2
                count[p2] += count[p1]
        
        for ind in range(1, n):
            if nums[ind] - nums[ind-1] <= maxDiff:
                join(ind-1, ind)
        
        return [find(node1) == find(node2) for node1, node2 in queries]
