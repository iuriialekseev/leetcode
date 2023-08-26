class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        dict = {}

        for winner, loser in matches:
            if winner not in dict:
                dict[winner] = 0

            if loser not in dict:
                dict[loser] = 0

            dict[loser] += 1

        zero, one = [], []
        for player, loses in dict.items():
            if loses == 0:
                zero.append(player)
            elif loses == 1:
                one.append(player)

        return [sorted(zero), sorted(one)]
