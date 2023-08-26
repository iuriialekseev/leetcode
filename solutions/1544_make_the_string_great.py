class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for curr in s:
            if len(stack) == 0:
                stack.append(curr)
            else:
                prev = stack[-1]
                if prev == curr or prev.lower() != curr.lower():
                    stack.append(curr)
                else:
                    stack.pop()

        return "".join(stack)
