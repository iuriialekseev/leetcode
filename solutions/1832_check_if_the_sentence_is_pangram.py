class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        chars = set(sentence)

        return len(chars) == 26
