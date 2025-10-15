command = input().split()
length_a = int(command[0])
length_b = int(command[1])
set_a = set()
set_b = set()

for _ in range(length_a):
    num = int(input())
    set_a.add(num)

for _ in range(length_b):
    num = int(input())
    set_b.add(num)

for el in set_a.intersection(set_b):
    print(el)
