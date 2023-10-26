class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []

        letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "r", "q", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def backtrack(combination):
            if len(combination) == len(digits):
                combinations.append("".join(combination))
                return

            digit = digits[len(combination)]
            for letter in letters[digit]:
                combination.append(letter)
                backtrack(combination)
                combination.pop()

        combinations = []
        backtrack([])

        return combinations
