class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = [0] * size
        self.count = 0
        self.sum = 0

    def next(self, val: int) -> float:
        idx = self.count % self.size

        self.sum -= self.queue[idx]
        self.queue[idx] = val
        self.sum += val
        self.count += 1

        return self.sum / min(self.count, self.size)
