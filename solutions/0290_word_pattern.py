class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(words) != len(pattern):
            return False

        char_map = {}
        word_map = {}

        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]

            if char in char_map and char_map[char] != word:
                return False
            if word in word_map and word_map[word] != char:
                return False

            char_map[char] = word
            word_map[word] = char

        return True
