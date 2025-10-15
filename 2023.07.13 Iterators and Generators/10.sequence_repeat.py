class SequenceRepeat:
    def __init__(self, string1, count):
        self.string1 = string1
        self.count = count + 1
        self.list1 = []
        self.list1.extend(string1 * 100)

    def __iter__(self):
        return self

    def __next__(self):
        self.count -= 1
        if self.count == 0:
            raise StopIteration

        for _ in self.list1:
            char = self.list1.pop(0)
            return char
