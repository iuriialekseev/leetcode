from collections import defaultdict


class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        cities = defaultdict(str)
        for out, into in paths:
            cities[out] = into

        curr = paths[0][0]
        while cities[curr] != "":
            curr = cities[curr]

        return curr
