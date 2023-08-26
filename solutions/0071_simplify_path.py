class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for part in path.split("/"):
            if part == "." or part == "":
                continue
            elif part == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(part)

        return "/" + "/".join(stack)
