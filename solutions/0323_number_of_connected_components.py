from collections import defaultdict


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        ans = 0
        seen = set()

        def dfs(curr):
            if curr in seen:
                return

            seen.add(curr)

            for next in graph[curr]:
                dfs(next)

            return

        for node in range(0, n):
            if node not in seen:
                ans += 1
                dfs(node)

        return ans
