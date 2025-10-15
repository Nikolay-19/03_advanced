rows, cols = [int(el) for el in input().split(",")]

matrix = []
cheese = 0
flag = False
mouse_row = 0
mouse_col = 0

for row in range(rows):
    temp = []
    temp.extend(input())
    matrix.append(temp)

for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == "M":
            mouse_row = row
            mouse_col = col
        elif matrix[row][col] == "C":
            cheese += 1

while True:
    command = input()
    if command == "danger":
        if cheese > 0:
            print("Mouse will come back later!")
        break

    elif command == "up":
        if mouse_row - 1 < 0:
            matrix[mouse_row][mouse_col] = "M"
            print("No more cheese for tonight!")
            break
        else:
            matrix[mouse_row][mouse_col] = "*"
            mouse_row -= 1
            element = matrix[mouse_row][mouse_col]
            if element == "C":
                cheese -= 1
                if cheese == 0:
                    matrix[mouse_row][mouse_col] = "M"
                    print("Happy mouse! All the cheese is eaten, good night!")
                    break
            elif element == "T":
                matrix[mouse_row][mouse_col] = "M"
                print("Mouse is trapped!")
                break
            elif element == "@":
                mouse_row += 1
                matrix[mouse_row][mouse_col] = "M"
                continue

    elif command == "down":
        if mouse_row + 1 > rows - 1:
            matrix[mouse_row][mouse_col] = "M"
            print("No more cheese for tonight!")
            break
        else:
            matrix[mouse_row][mouse_col] = "*"
            mouse_row += 1
            element = matrix[mouse_row][mouse_col]
            if element == "C":
                cheese -= 1
                if cheese == 0:
                    matrix[mouse_row][mouse_col] = "M"
                    print("Happy mouse! All the cheese is eaten, good night!")
                    break
            elif element == "T":
                matrix[mouse_row][mouse_col] = "M"
                print("Mouse is trapped!")
                break
            elif element == "@":
                mouse_row -= 1
                matrix[mouse_row][mouse_col] = "M"
                continue

    elif command == "left":
        if mouse_col - 1 < 0:
            matrix[mouse_row][mouse_col] = "M"
            print("No more cheese for tonight!")
            break
        else:
            matrix[mouse_row][mouse_col] = "*"
            mouse_col -= 1
            element = matrix[mouse_row][mouse_col]
            if element == "C":
                cheese -= 1
                if cheese == 0:
                    matrix[mouse_row][mouse_col] = "M"
                    print("Happy mouse! All the cheese is eaten, good night!")
                    break
            elif element == "T":
                matrix[mouse_row][mouse_col] = "M"
                print("Mouse is trapped!")
                break
            elif element == "@":
                mouse_col += 1
                matrix[mouse_row][mouse_col] = "M"
                continue

    elif command == "right":
        if mouse_col + 1 > cols - 1:
            matrix[mouse_row][mouse_col] = "M"
            print("No more cheese for tonight!")
            break
        else:
            matrix[mouse_row][mouse_col] = "*"
            mouse_col += 1
            element = matrix[mouse_row][mouse_col]
            if element == "C":
                cheese -= 1
                if cheese == 0:
                    matrix[mouse_row][mouse_col] = "M"
                    print("Happy mouse! All the cheese is eaten, good night!")
                    break
            elif element == "T":
                matrix[mouse_row][mouse_col] = "M"
                print("Mouse is trapped!")
                break
            elif element == "@":
                mouse_col -= 1
                matrix[mouse_row][mouse_col] = "M"
                continue

for row in matrix:
    print(*row, sep="")
