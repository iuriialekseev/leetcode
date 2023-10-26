class Solution:
    def maximum69Number(self, num: int) -> int:
        chars = list(str(num))

        for i in range(len(chars)):
            if chars[i] == "6":
                chars[i] = "9"
                break

        return int("".join(chars))
