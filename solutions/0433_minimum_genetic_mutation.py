from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        seen = set(startGene)
        valid = set(bank)
        queue: deque[tuple[str, int]] = deque([(startGene, 0)])

        while queue:
            node, steps = queue.popleft()

            if node == endGene:
                return steps

            for protein in "ACTG":
                for i in range(len(node)):
                    mutated = node[:i] + protein + node[i + 1 :]
                    if mutated in valid and mutated not in seen:
                        queue.append((mutated, steps + 1))

        return -1
