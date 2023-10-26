class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        def backtrack(combination, sum, next):
            if len(combination) == k:
                if sum == 0:
                    answers.append(combination.copy())
                return

            for i in range(next, 10):
                if i <= sum:
                    combination.append(i)
                    backtrack(combination, sum - i, i + 1)
                    combination.pop()

        answers = []
        backtrack([], n, 1)

        return answers
