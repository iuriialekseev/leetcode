class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        length = len(candidates)

        def backtrack(sum, start, path):
            if sum > target:
                return
            if sum == target:
                answer.append(path)
                return

            for i in range(start, length):
                backtrack(sum + candidates[i], i, path + [candidates[i]])

        answer = []
        backtrack(0, 0, [])
        return answer
