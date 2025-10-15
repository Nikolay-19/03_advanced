from collections import deque

bowls = deque(int(el) for el in input().split(", "))  # LIFO
clients = deque(int(el) for el in input().split(", "))  # FIFO

while bowls and clients:
    bowl = bowls.pop()
    client = clients.popleft()

    if bowl == client:
        continue

    elif bowl > client:
        bowl -= client
        bowls.append(bowl)
        continue

    elif client > bowl:
        client -= bowl
        clients.appendleft(client)

if not clients:
    print("Great job! You served all the customers.")
    if bowls:
        print(f"Bowls of ramen left: ", end="")
        print(*bowls, sep=", ")
else:
    print("Out of ramen! You didn't manage to serve all customers.\n"
          "Customers left: ", end="")
    print(*clients, sep=", ")
