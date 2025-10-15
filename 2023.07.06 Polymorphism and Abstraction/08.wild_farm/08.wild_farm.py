from project.animals.birds import Hen, Owl
from project.animals.mammals import Mouse, Cat, Dog, Tiger
from project.food import Fruit, Vegetable, Meat, Seed

a = Hen("B", 10, "C")

c = Vegetable(2)
d = Fruit(2)
e = Seed(2)
f = Meat(2)
print(a.feed(c))
print(a.feed(d))
print(a.feed(e))
print(a.feed(f))
print(a.make_sound())
