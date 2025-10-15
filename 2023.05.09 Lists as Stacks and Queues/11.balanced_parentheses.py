from collections import deque

skobi = deque(input())
otvoreni = deque()

while skobi:
    el = skobi.popleft()

    if el in "([{":
        otvoreni.append(el)
    elif not otvoreni:
        print("NO")
        break
    else:
        if f"{otvoreni.pop() + el}" not in "()[]{}":
            print("NO")
            break
else:
    print("YES")
