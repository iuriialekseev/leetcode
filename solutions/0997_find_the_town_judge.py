class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        counts = [0] * (n + 1)

        for out, into in trust:
            counts[out] -= 1
            counts[into] += 1

        for i in range(1, n + 1):
            if counts[i] == n - 1:
                return i

        return -1
