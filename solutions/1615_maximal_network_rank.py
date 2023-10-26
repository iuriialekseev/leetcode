class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        degrees = [0] * n
        for a, b in roads:
            degrees[a] += 1
            degrees[b] += 1

        road_set = set(tuple(road) for road in roads)

        result = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = degrees[i] + degrees[j]
                if (i, j) in road_set or (j, i) in road_set:
                    rank -= 1
                result = max(result, rank)

        return result
