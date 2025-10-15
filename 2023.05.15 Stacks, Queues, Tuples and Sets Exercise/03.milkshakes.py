from collections import deque
chocolates = deque([int(x) for x in input().split(", ")])
cups = deque([int(y) for y in input().split(", ")])
shakes = 0

while shakes != 5 and chocolates and cups:
    chocolate = chocolates.pop()
    cup = cups.popleft()
    
    if chocolate <= 0 and cup <= 0:
        continue
    elif chocolate <= 0:
        cups.appendleft(cup)
        continue
    elif cup <= 0:
        chocolates.append(chocolate)
        continue
        
    if chocolate == cup:
        shakes += 1
    else:
        cups.append(cup)
        chocolates.append(chocolate - 5)
        
if shakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
    
print(f"Chocolate: {', '.join(str(s)for s in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(a) for a in cups) or 'empty'}")