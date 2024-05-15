class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length = len(s1)
        s2_length = len(s2)

        if s1_length > s2_length:
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(s1_length):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        if s1_count == s2_count:
            return True

        for i in range(s1_length, s2_length):
            s2_count[ord(s2[i]) - ord('a')] += 1
            s2_count[ord(s2[i - s1_length]) - ord('a')] -= 1

            if s1_count == s2_count:
                return True

        return False
