class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        LIMIT=(len(blocked)*(len(blocked)-1))//2
        N=1000000
        def bfs(start, target):
            q = deque([start])
            visited = {start}
            d=[(1,0),(0,1),(-1,0),(0,-1)]

            while q:

                r, c = q.popleft()

                if (r, c) == target:
                    return True

                if len(visited) > LIMIT:
                    return True

                for dr, dc in d:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < N and 0 <= nc < N:
                        if (nr, nc) in blocked:
                            continue

                        if (nr, nc) not in visited:
                            visited.add((nr, nc))
                            q.append((nr, nc))

            return False
        sx,sy=source
        tx,ty=target
        blocked={tuple(x) for x in blocked}
        return bfs((sx,sy),(tx,ty)) and bfs((tx,ty),(sx,sy))