class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        ans = 0

        for boxType in boxTypes:
            boxes, items = boxType
            capacity = min(truckSize, boxes)

            ans += capacity * items
            truckSize -= capacity

            if truckSize == 0:
                break

        return ans
