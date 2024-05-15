class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)

        if length == 1:
            return cost[0]
        if length == 2:
            return min(cost[0], cost[1])

        memo = [0] * length
        memo[0] = cost[0]
        memo[1] = cost[1]

        for i in range(2, length):
            memo[i] = cost[i] + min(memo[i - 1], memo[i - 2])

        return min(memo[-1], memo[-2])
