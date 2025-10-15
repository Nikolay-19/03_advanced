size = int(input())
nuts = 0
matrix = []
squirrel_row = 0
squirrel_col = 0
flag = False

commands = [el for el in input().split(", ")]
for _ in range(size):
    el = input()
    a = []
    for char in el:
        a.append(char)
    matrix.append(a)

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "s":
            squirrel_row = row
            squirrel_col = col

for command in commands:
    if nuts > 2:
        break

    if command == "up":
        if squirrel_row - 1 < 0:
            print("The squirrel is out of the field.")
            flag = True
            break
        else:
            squirrel_row -= 1
        el = matrix[squirrel_row][squirrel_col]
        if el == "h":
            nuts += 1
            matrix[squirrel_row][squirrel_col] = "*"
        elif el == "t":
            print("Unfortunately, the squirrel stepped on a trap...")
            flag = True
            break

    elif command == "down":
        if squirrel_row + 1 > size - 1:
            print("The squirrel is out of the field.")
            flag = True
            break
        else:
            squirrel_row += 1
        el = matrix[squirrel_row][squirrel_col]
        if el == "h":
            nuts += 1
            matrix[squirrel_row][squirrel_col] = "*"
        elif el == "t":
            print("Unfortunately, the squirrel stepped on a trap...")
            flag = True
            break

    elif command == "left":
        if squirrel_col - 1 < 0:
            print("The squirrel is out of the field.")
            flag = True
            break
        else:
            squirrel_col -= 1
        el = matrix[squirrel_row][squirrel_col]
        if el == "h":
            nuts += 1
            matrix[squirrel_row][squirrel_col] = "*"
        elif el == "t":
            print("Unfortunately, the squirrel stepped on a trap...")
            flag = True
            break

    elif command == "right":
        if squirrel_col + 1 > size - 1:
            print("The squirrel is out of the field.")
            flag = True
            break
        else:
            squirrel_col += 1
        el = matrix[squirrel_row][squirrel_col]
        if el == "h":
            nuts += 1
            matrix[squirrel_row][squirrel_col] = "*"
        elif el == "t":
            print("Unfortunately, the squirrel stepped on a trap...")
            flag = True
            break

if nuts < 3 and not flag:
    print("There are more hazelnuts to collect.")
elif nuts >= 3 and not flag:
    print("Good job! You have collected all hazelnuts!")
print(f"Hazelnuts collected: {nuts}")
