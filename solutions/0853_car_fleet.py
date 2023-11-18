class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        bottleneck = -1

        for position, speed in cars:
            hours = (target - position) / speed
            if hours > bottleneck:
                fleets += 1
                bottleneck = hours

        return fleets
