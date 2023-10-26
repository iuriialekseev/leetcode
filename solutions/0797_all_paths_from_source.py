class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        start = 0
        end = len(graph) - 1
        answers = []

        def backtrack(path):
            node = path[-1]

            if node == end:
                answers.append(path[:])
                return

            for next in graph[node]:
                path.append(next)
                backtrack(path)
                path.pop()

        backtrack([start])

        return answers
