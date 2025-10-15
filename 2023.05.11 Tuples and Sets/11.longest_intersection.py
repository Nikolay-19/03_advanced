import sys

sets_qt = int(input())
first_set = set()
second_set = set()
intersections = []
max_length = -sys.maxsize
max_intersection = []

for _ in range(sets_qt):
    command = input().split("-")
    first_range = command[0].split(",")
    second_range = command[1].split(",")
    first_start = int(first_range[0])
    first_end = int(first_range[1])
    second_start = int(second_range[0])
    second_end = int(second_range[1])

    for i in range(first_start, first_end + 1):
        first_set.add(i)
    for j in range(second_start, second_end + 1):
        second_set.add(j)

    intersections.append(first_set.intersection(second_set))
    first_set = set()
    second_set = set()

for intersection in intersections:
    if len(intersection) > max_length:
        max_length = len(intersection)
        max_intersection = list(intersection)

print(f"Longest intersection is {max_intersection} with length {max_length}")
