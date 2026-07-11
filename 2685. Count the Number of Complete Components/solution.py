class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()

        for nd, negh in edges:
            graph[nd].append(negh)
            graph[negh].append(nd)

        # # Recursive solution
        # def dfs(node):
        #     visited.add(node)
        #     c = 1
        #     e = len(graph[node])
        #     for ng in graph[node]:
        #         if ng not in visited:
        #             dc, de = dfs(ng)
        #             c += dc
        #             e += de
        #     return c, e           

        # ans = 0
        # for i in range(n):
        #     if i not in visited:
        #         nodes, edges = dfs(i)
        #         if edges//2 == (nodes * (nodes - 1))//2:
        #             ans += 1
        # return ans

        # # iterative implimentation using stack
        # def itr(node):
        #     stack = [node]
        #     e = 0
        #     c = 0
        #     while stack:
        #         a = stack.pop()
        #         e += len(graph[a])
        #         c += 1
        #         visited.add(a)
        #         for nd in graph[a]:
        #             if nd not in visited:
        #                 visited.add(nd)
        #                 stack.append(nd)
        #     return e, c

        # ans = 0
        # for i in range(n):
        #     if i not in visited:
        #         edges, nodes = itr(i)
        #         if edges//2 == (nodes * (nodes - 1))//2:
        #             ans += 1
        # return ans

        # iterative approach using bfs
        def bfs(node):
            que = deque([node])
            visited.add(node)
            c = 1
            e = 0
            while que:
                n = len(que)
                for _ in range(n):
                    a = que.popleft()
                    for nd in graph[a]:
                        if nd not in visited:
                            visited.add(nd)
                            que.append(nd)
                            c += 1
                        else:
                            e += 1
                e += len(que)
            return e, c

        ans = 0
        for i in range(n):
            if i not in visited:
                edges, nodes = bfs(i)
                print(i, edges, nodes)
                if edges//2 == (nodes * (nodes - 1))//2:
                    ans += 1
        return ans
