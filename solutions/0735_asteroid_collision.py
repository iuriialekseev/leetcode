class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for x in asteroids:
            if x > 0:
                ans.append(x)
            else:
                while ans and ans[-1] > 0 and ans[-1] < abs(x):
                    ans.pop()
                if not ans or ans[-1] < 0:
                    ans.append(x)
                elif ans[-1] == abs(x):
                    ans.pop()
        return ans
