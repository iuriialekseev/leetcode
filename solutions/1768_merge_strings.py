class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = []

        p1 = p2 = 0
        is_p1 = True

        while p1 < len(word1) and p2 < len(word2):
            if is_p1:
                answer.append(word1[p1])
                p1 += 1
            else:
                answer.append(word2[p2])
                p2 += 1

            is_p1 = not is_p1

        while p1 < len(word1):
            answer.append(word1[p1])
            p1 += 1

        while p2 < len(word2):
            answer.append(word2[p2])
            p2 += 1

        return "".join(answer)
