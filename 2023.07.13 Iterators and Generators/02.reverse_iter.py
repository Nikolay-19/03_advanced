class ReverseIter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.idx = len(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        self.idx -= 1
        if self.idx < 0:
            raise StopIteration
        return self.iterable[self.idx]
