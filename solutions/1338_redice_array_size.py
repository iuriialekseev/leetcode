from collections import defaultdict
import heapq


class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        hash = defaultdict(int)
        for item in arr:
            hash[item] += 1

        heap = [(-val, key) for key, val in hash.items()]
        heapq.heapify(heap)

        length = len(arr)
        half = length // 2
        ans = 0

        while heap:
            val, _ = heapq.heappop(heap)

            if length > half:
                length -= -val
                ans += 1
            else:
                break

        return ans


Solution().minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7])
