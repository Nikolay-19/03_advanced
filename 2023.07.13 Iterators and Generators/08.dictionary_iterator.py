class DictionaryIter:
    def __init__(self, dict1):
        self.dict1 = dict1
        self.idx = -1
        self.length = len(dict1)

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        if self.idx > self.length - 1:
            raise StopIteration
        for key in self.dict1:
            removed = self.dict1.pop(key)
            return key, removed
