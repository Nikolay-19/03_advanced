from collections import deque

food = int(input())
queue1 = deque([int(el) for el in input().split()])
completed = []

print(max(queue1))

for el in queue1:
    if el <= food:
        food -= el
        completed.append(el)
    else:
        break

if len(queue1) != len(completed):
    for _ in range(len(completed)):
        queue1.popleft()
    print(f"Orders left: ", end="")
    for el in queue1:
        print(el, end=" ")
else:
    print("Orders complete")
