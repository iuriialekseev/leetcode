class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {'+', '-', '*', '/'}

        for token in tokens:
            if token in operands:
                b = int(stack.pop())
                a = int(stack.pop())

                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))

            else:
                stack.append(int(token))

        return stack.pop()
