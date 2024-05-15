class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        for ch in s:
            if ch in pairs:
                if stack and pairs[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return len(stack) == 0
