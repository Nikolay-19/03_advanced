from collections import deque

queue1 = deque([])

while True:
    command = input()
    if command == "End":
        print(f"{len(queue1)} people remaining.")
        break
    elif command == "Paid":
        while queue1:
            name = queue1.popleft()
            print(name)
    else:
        queue1.append(command)
