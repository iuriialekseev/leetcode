class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        stack = []

        for br in list(s):
            if stack and br in match and stack[-1] == match[br]:
                stack.pop()
            else:
                stack.append(br)

        return len(stack) == 0
