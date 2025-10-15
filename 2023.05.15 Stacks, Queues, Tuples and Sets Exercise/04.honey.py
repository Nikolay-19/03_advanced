from collections import deque

bees = deque([int(el) for el in input().split()])
nectars = deque([int(el) for el in input().split()])
symbols = deque(el for el in input().split())
honey = 0

while bees and nectars:
    bee = bees.popleft()
    nectar = nectars.pop()

    if nectar < bee:
        bees.appendleft(bee)
    elif nectar > bee:
        symbol = symbols.popleft()
        if symbol == "+":
            honey += abs(bee + nectar)
        elif symbol == "-":
            honey += abs(bee - nectar)
        elif symbol == "*":
            honey += abs(bee * nectar)
        elif symbol == "/":
            honey += abs(bee / nectar)

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join(str(el) for el in bees)}")
if nectars:
    print(f"Nectar left: {', '.join(str(el) for el in nectars)}")
