class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []
        length = len(s)

        def is_palindrome(word):
            return word == word[::-1]

        def backtrack(start, path):
            if start == length:
                results.append(path[:])
                return

            for end in range(start + 1, length + 1):
                if is_palindrome(s[start:end]):
                    path.append(s[start:end])
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return results
