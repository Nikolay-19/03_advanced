from collections import deque

rows, cols = [int(el) for el in input().split()]
string1 = input()
string2 = deque(string1)

for row in range(rows):
    while len(string2) < cols:
        string2.extend(string1)

    if row % 2 == 0:
        print(*[string2.popleft() for _ in range(cols)], sep="")
    else:
        print(*[string2.popleft() for _ in range(cols)][::-1], sep="")
