class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions = {
            1: [(0, -1), (0, 1)],  # Street 1: Horizontal (left, right)
            2: [(1, 0), (-1, 0)],  # Street 2: Vertical (down, up)
            3: [(0, -1), (1, 0)],  # Street 3: Left-Down (left, down)
            4: [(0, 1), (1, 0)],   # Street 4: Right-Down (right, down)
            5: [(0, -1), (-1, 0)], # Street 5: Left-Up (left, up)
            6: [(0, 1), (-1, 0)]   # Street 6: Right-Up (right, up)
        }

        valid = {
            1: [(1, 4, 6), (1, 3, 5)],  # Street 1: Valid connections for left and right
            2: [(2, 5, 6), (2, 3, 4)],  # Street 2: Valid connections for down and up
            3: [(1, 4, 6), (2, 5, 6)],  # Street 3: Valid connections for left and down
            4: [(1, 3, 5), (2, 5, 6)],  # Street 4: Valid connections for right and down
            5: [(1, 4, 6), (2, 3, 4)],  # Street 5: Valid connections for left and up
            6: [(1, 3, 5), (2, 3, 4)]   # Street 6: Valid connections for right and up
        }

        

        n, m = len(grid), len(grid[0])
        start, target = (0, 0), (n-1, m-1)
        que = deque([start])
        visited = set(start)

        if n == m == 1:
            return True

        while que:
            for _ in range(len(que)):
                r, c = que.popleft()
                for dr, dc in directions[grid[r][c]]:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited:
                        if (dr, dc) == directions[grid[r][c]][0] and grid[nr][nc] in valid[grid[r][c]][0] or grid[nr][nc] in valid[grid[r][c]][1]:
                            if (nr, nc) == target:
                                return True
                            que.append((nr, nc))
                            visited.add((nr, nc))

        return False
