
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 or (i, j) in visited:
                    continue

                stack = [(i, j)]
                visited.add((i, j))
                total = 0

                while stack:
                    x, y = stack.pop()
                    total += grid[x][y]

                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy

                        if (0 <= nx < n and 0 <= ny < m
                                and grid[nx][ny] != 0
                                and (nx, ny) not in visited):
                            visited.add((nx, ny))
                            stack.append((nx, ny))

                if total % k == 0:
                    count += 1

        return count
