from collections import deque

queue1 = deque(input().split())
boom = int(input()) - 1

while len(queue1) > 1:
    queue1.rotate(-boom)
    name = queue1.popleft()
    print(f"Removed {name}")

print(f"Last is {queue1[0]}")
