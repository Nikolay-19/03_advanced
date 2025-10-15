stack1 = [int(el) for el in input().split()]
capacity = int(input())
first_cap = capacity
racks = 1

while stack1:
    if capacity >= stack1[-1]:
        capacity -= stack1[-1]
        stack1.pop()
        if capacity == 0 and stack1:
            capacity = first_cap
            racks += 1

    else:
        capacity = first_cap
        capacity -= stack1[-1]
        stack1.pop()
        racks += 1

print(racks)
