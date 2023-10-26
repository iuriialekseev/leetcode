class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        def valid(num):
            if len(num) > 1 and num[0] == "0":
                return False

            return 0 <= int(num) <= 255

        def backtrack(comb, left, right):
            if len(comb) == 4:
                if right == len(s):
                    results.append(".".join(list(comb)))
                return

            for i in range(1, 4):
                if right + i <= len(s):
                    next = s[left : right + i]
                    if valid(next):
                        comb.append(next)
                        backtrack(comb, right + i, right + i)
                        comb.pop()

        results = []
        backtrack([], 0, 0)

        return results
