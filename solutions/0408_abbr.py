class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        pw = pa = 0

        while pw < len(word) and pa < len(abbr):
            if abbr[pa].isdigit():
                if abbr[pa] == '0':
                    return False

                shift = 0
                while pa < len(abbr) and abbr[pa].isdigit():
                    shift = (shift*10)+int(abbr[pa])
                    pa += 1

                pw += shift
            else:
                if word[pw] != abbr[pa]:
                    return False

                pw += 1
                pa += 1

        return pw == len(word) and pa == len(abbr)
