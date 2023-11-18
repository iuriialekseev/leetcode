class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gi = si = 0

        while gi < len(g) and si < len(s):
            if s[si] >= g[gi]:
                gi += 1
                si += 1
            else:
                si += 1

        return gi
