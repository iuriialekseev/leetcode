class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        w = len(image)
        h = len(image[0])
        source = image[sr][sc]

        if source == color:
            return image

        def fill(x, y):
            if 0 <= x < w and 0 <= y < h and image[x][y] == source:
                image[x][y] = color
                fill(x - 1, y)
                fill(x + 1, y)
                fill(x, y - 1)
                fill(x, y + 1)

        fill(sr, sc)
        return image
