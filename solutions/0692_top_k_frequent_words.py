from collections import defaultdict
import heapq


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        counter = defaultdict(int)

        for word in words:
            counter[word] += 1

        max_heap = [(-count, word) for word, count in counter.items()]
        heapq.heapify(max_heap)

        result = []
        for _ in range(k):
            _, word = heapq.heappop(max_heap)
            result.append(word)

        return result
