from collections import defaultdict


class Solution:
    def validPath(
        self, n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = [False] * n

        def dfs(current):
            if current == destination:
                return True

            if not seen[current]:
                seen[current] = True
                for next in graph[current]:
                    if dfs(next):
                        return True

            return False

        return dfs(source)
