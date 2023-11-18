class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0

        for i in range(len(pushed)):
            stack.append(pushed[i])

            while stack and j < len(popped) and popped[j] == stack[-1]:
                stack.pop()
                j += 1

        return j == len(popped)
