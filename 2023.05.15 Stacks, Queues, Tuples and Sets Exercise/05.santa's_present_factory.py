from collections import deque

materials = deque([int(el) for el in input().split()])
magics = deque([int(el) for el in input().split()])
doll = 150
train = 250
bear = 300
bicycle = 400
doll_qt = 0
train_qt = 0
bear_qt = 0
bicycle_qt = 0

while materials and magics:
    material = materials.pop() if magics[0] or not materials[0] else 0
    magic = magics.popleft() if material or not magics[0] else 0
    result = material * magic
    
    if not magic:
        continue
    elif result < 0:
        result = material + magic
        materials.append(result)
    elif material == 0:
        magics.appendleft(magic)
        continue
    elif magic == 0:
        materials.append(material)
        continue
    elif material == 0 and magic == 0:
        continue
    elif result == doll:
        doll_qt += 1
    elif result == train:
        train_qt += 1
    elif result == bear:
        bear_qt += 1
    elif result == bicycle:
        bicycle_qt += 1
    else:
        materials.append(material + 15)

if (doll_qt >= 1 and train_qt >= 1) or (bear_qt >= 1 and bicycle_qt >= 1):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join(str(el) for el in reversed(materials))}")
if magics:
    print(f"Magic left: {', '.join(str(el) for el in magics)}")
if bicycle_qt:
    print(f"Bicycle: {bicycle_qt}")
if doll_qt:
    print(f"Doll: {doll_qt}")
if bear_qt:
    print(f"Teddy bear: {bear_qt}")
if train_qt:
    print(f"Wooden train: {train_qt}")
