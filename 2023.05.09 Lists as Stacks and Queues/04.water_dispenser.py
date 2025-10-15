from collections import deque

water = int(input())
queue1 = deque()

while True:
    command = input()
    if command == "Start":
        break
    queue1.append(command)

while True:
    command = input().split()
    if command[0].isdecimal():
        if int(command[0]) <= water:
            name = queue1.popleft()
            print(f"{name} got water")
            water -= int(command[0])
        else:
            name = queue1.popleft()
            print(f"{name} must wait")

    elif command[0] == "refill":
        water += int(command[1])

    elif command[0] == "End":
        print(f"{water} liters left")
        break
