from collections import deque
queue1 = deque([el for el in input().split()])
main_clrs = ["red", "yellow", "blue", "orange", "purple", "green"]
combined_clrs = {"orange": {"yellow", "red"}, "purple": {"red", "blue"}, "green": {"yellow", "blue"}}
colors = []

while queue1:
    first = queue1.popleft()
    last = queue1.pop() if queue1 else ""
    
    for color in (first + last, last + first):
        if color in main_clrs:
            colors.append(color)
            break
            
    else:
        for el in (first[:-1], last[:-1]):
            if el:
                queue1.insert(len(queue1) // 2, el)
                
for color in set(combined_clrs.keys()).intersection(colors):
    if not combined_clrs[color].issubset(colors):
        colors.remove(color)
print(colors)