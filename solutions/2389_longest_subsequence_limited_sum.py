class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        def binary_search_right(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return right

        nums.sort()
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]

        answers = []
        for query in queries:
            answer = binary_search_right(nums, query) + 1
            answers.append(answer)

        return answers


Solution().answerQueries([4, 5, 2, 1], [3, 10, 21])
