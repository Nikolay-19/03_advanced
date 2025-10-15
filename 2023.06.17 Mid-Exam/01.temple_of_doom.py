from collections import deque

tools = deque(int(el) for el in input().split())       # FIFO
substances = deque(int(el) for el in input().split())  # LIFO
challenges = deque(int(el) for el in input().split())

while tools and substances:
    tool = tools.popleft()
    substance = substances.pop()

    if tool * substance in challenges:
        challenges.remove(tool * substance)
    else:
        tool += 1
        substance -= 1
        tools.append(tool)
        if substance > 0:
            substances.append(substance)

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
if tools:
    print(f"Tools: {', '.join((str(el) for el in tools))}")
if substances:
    print(f"Substances: {', '.join((str(el) for el in substances))}")
if challenges:
    print(f"Challenges: {', '.join((str(el) for el in challenges))}")
