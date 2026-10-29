class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        
        
        
        LOG = max(1, n.bit_length())

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        tin = [0] * n
        tout = [0] * n
        up = [[0] * n for _ in range(LOG)]

        timer = 0

        # Iterative DFS: Euler tour + binary lifting table
        stack = [(0, -1, False)]

        while stack:
            node, parent, processed = stack.pop()

            if processed:
                tout[node] = timer
                timer += 1
                continue

            tin[node] = timer
            timer += 1
            up[0][node] = node if parent == -1 else parent

            stack.append((node, parent, True))

            for child in graph[node]:
                if child != parent:
                    stack.append((child, node, False))

        for k in range(1, LOG):
            for v in range(n):
                up[k][v] = up[k - 1][up[k - 1][v]]

        def is_ancestor(a: int, b: int) -> bool:
            return tin[a] <= tin[b] and tout[b] <= tout[a]

        def lca(a: int, b: int) -> int:
            if is_ancestor(a, b):
                return a
            if is_ancestor(b, a):
                return b

            for k in range(LOG - 1, -1, -1):
                if not is_ancestor(up[k][a], b):
                    a = up[k][a]

            return up[0][a]

        # Fenwick tree over the full Euler tour
        tree = [0] * (2 * n + 1)

        def update(index: int, value: int) -> None:
            index += 1
            while index <= 2 * n:
                tree[index] ^= value
                index += index & -index

        def prefix_xor(index: int) -> int:
            index += 1
            result = 0
            while index > 0:
                result ^= tree[index]
                index -= index & -index
            return result

        def char_mask(c: str) -> int:
            return 1 << (ord(c) - ord('a'))

        node_mask = [char_mask(c) for c in s]

        # IMPORTANT: add each node's mask at BOTH tin and tout
        for node in range(n):
            update(tin[node], node_mask[node])
            update(tout[node], node_mask[node])

        def root_to_node_mask(node: int) -> int:
            # XOR of masks of all ancestors of node, including node
            return prefix_xor(tin[node])

        answer = []

        for query in queries:
            parts = query.split()

            if parts[0] == "update":
                node = int(parts[1])
                new_mask = char_mask(parts[2])
                old_mask = node_mask[node]

                if new_mask != old_mask:
                    update(tin[node], old_mask ^ new_mask)
                    update(tout[node], old_mask ^ new_mask)
                    node_mask[node] = new_mask

            else:
                u = int(parts[1])
                v = int(parts[2])
                l = lca(u, v)

                path_mask = (
                    root_to_node_mask(u)
                    ^ root_to_node_mask(v)
                    ^ node_mask[l]
                )

                answer.append(path_mask.bit_count() <= 1)

        return answer