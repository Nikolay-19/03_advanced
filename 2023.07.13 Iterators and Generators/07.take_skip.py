class TakeSkip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.iter = 0
        self.num = -self.step

    def __iter__(self):
        return self

    def __next__(self):
        self.iter += 1
        if self.iter > self.count:
            raise StopIteration
        self.num += self.step
        return self.num
