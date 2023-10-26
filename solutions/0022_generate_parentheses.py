class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def backtrack(combination, left, right):
            if len(combination) == n * 2:
                answers.append("".join(combination))
                return

            if left < n:
                combination.append("(")
                backtrack(combination, left + 1, right)
                combination.pop()

            if right < left:
                combination.append(")")
                backtrack(combination, left, right + 1)
                combination.pop()

        answers = []
        backtrack([], 0, 0)

        return answers
