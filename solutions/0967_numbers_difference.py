class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        def valid(n):
            return 0 <= n <= 9

        def backtrack(num, i):
            if i + 1 == n:
                answers.add(num)
                return

            last = num % 10
            for next in [last + k, last - k]:
                if valid(next):
                    backtrack(num * 10 + next, i + 1)

        answers = set()
        for i in range(1, 10):
            backtrack(i, 0)

        return list(answers)
