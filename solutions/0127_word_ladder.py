from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        def toKey(word, i):
            return word[:i] + "*" + word[i + 1 :]

        length = len(beginWord)

        transformations = defaultdict(list)
        for word in wordList:
            for i in range(length):
                key = toKey(word, i)
                transformations[key].append(word)

        seen = set(beginWord)
        queue: deque[tuple[str, int]] = deque([(beginWord, 1)])

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            for i in range(length):
                key = toKey(word, i)
                for next in transformations[key]:
                    if next not in seen:
                        seen.add(next)
                        queue.append((next, steps + 1))

        return 0
