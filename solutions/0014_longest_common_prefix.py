class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ""
        level = 0

        while level >= len(strs[0]):
            char = strs[0][level]

            for i in range(1, len(strs)):
                if level >= len(strs[i]) or strs[i][level] != char:
                    return result

            result += char
            level += 1

        return result
