from collections import defaultdict, deque


class Solution:
    def reachableNodes(
        self, n: int, edges: list[list[int]], restricted: list[int]
    ) -> int:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        seen = [False] * n
        for node in restricted:
            seen[node] = True

        ans = 0
        queue = deque([0])
        seen[0] = True

        while queue:
            curr = queue.popleft()
            ans += 1

            for next in graph[curr]:
                if not seen[next]:
                    seen[next] = True
                    queue.append(next)

        return ans
