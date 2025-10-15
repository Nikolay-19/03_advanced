class Circle:
    def __init__(self, radius):
        self.radius = radius

    pi = 3.14

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        area = Circle.pi * self.radius * self.radius
        return round(area, 2)

    def get_circumference(self):
        circumference = 2 * Circle.pi * self.radius
        return round(circumference, 2)
