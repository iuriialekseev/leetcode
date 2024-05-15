class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)

        for n in range(1, n + 1):
            ans[n] = ans[n >> 1] + (n & 1)

        return ans
