from math import floor

string1 = [el for el in input().split()]
queue1 = []

for char in string1:
    if char == "+":
        while len(queue1) > 1:
            queue1[0] = queue1[0] + queue1[1]
            queue1.pop(1)
            
    elif char == "-":
        while len(queue1) > 1:
            queue1[0] = queue1[0] - queue1[1]
            queue1.pop(1)
            
    elif char == "*":
        while len(queue1) > 1:
            queue1[0] = queue1[0] * queue1[1]
            queue1.pop(1)
            
    elif char == "/":
        while len(queue1) > 1:
            queue1[0] = floor(queue1[0] / queue1[1])
            queue1.pop(1)
            
    else:
        queue1.append(int(char))

print(queue1[0])
