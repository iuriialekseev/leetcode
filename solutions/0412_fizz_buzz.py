class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = []
        keys = {3: "Fizz", 5: "Buzz"}
        nums = [3, 5]

        for i in range(1, n + 1):
            temp = []
            for num in nums:
                if i % num == 0:
                    temp.append(keys[num])

            if not temp:
                temp.append(str(i))

            answer.append("".join(temp))


        return answer
