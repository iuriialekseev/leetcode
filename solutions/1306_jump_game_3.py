from collections import deque


class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        seen = {start}
        queue = deque([start])

        while queue:
            curr = queue.popleft()
            val = arr[curr]

            if val == 0:
                return True

            for next in [curr + val, curr - val]:
                if 0 <= next < len(arr) and next not in seen:
                    seen.add(next)
                    queue.append(next)

        return False
