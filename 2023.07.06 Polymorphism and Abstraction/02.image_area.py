class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __lt__(self, other):
        if self.get_area() < other.get_area():
            return True
        return False

    def __le__(self, other):
        if self.get_area() <= other.get_area():
            return True
        return False

    def __eq__(self, other):
        if self.get_area() == other.get_area():
            return True
        return False
