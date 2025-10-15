class Cup:
    def __init__(self, size, quantity):
        self.size = int(size)
        self.quantity = int(quantity)

    def fill(self, qt):
        if self.quantity < self.size:
            self.quantity += int(qt)

    def status(self):
        return abs(self.size - self.quantity)
