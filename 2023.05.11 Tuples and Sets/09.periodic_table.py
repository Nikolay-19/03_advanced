elements_qt = int(input())
elements = set()

for _ in range(elements_qt):
    command = input().split()
    while command:
        elements.add(command[-1])
        command.pop()

print(*[el for el in elements], sep="\n")
