class Vowels:
    def __init__(self, string1):
        self.string1 = string1
        self.vowels = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
        self.idx = -1
        self.a = ""

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        if self.idx <= len(self.string1) - 1:
            if self.string1[self.idx] in self.vowels:
                return self.string1[self.idx]
            return self.__next__()
        else:
            raise StopIteration
