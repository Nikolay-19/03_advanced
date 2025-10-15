def all_collected(matrix, collected=False):
    list1 = []
    for row in range(rows):
        for col in range(cols):
            list1.append(matrix[row][col])
    if "D" not in list1 and "G" not in list1 and "C" not in list1:
        collected = True
        return collected


rows, cols = [int(el) for el in input().split(", ")]
matrix = []
cur_row = 0
cur_col = 0
gifts = 0
cookies = 0
decorations = 0

for row in range(rows):
    matrix.append([el for el in input().split()])

for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == "Y":
            cur_row = row
            cur_col = col

while True:
    if all_collected(matrix):
        matrix[cur_row][cur_col] = "Y"
        break
    command = input().split("-")
    if command[0] == "End":
        matrix[cur_row][cur_col] = "Y"
        break
    direction = command[0]
    steps = int(command[1])

    if direction == "up":
        for _ in range(steps):
            matrix[cur_row][cur_col] = "x"
            if cur_row - 1 < 0:
                cur_row = rows - 1
            else:
                cur_row -= 1
            element = matrix[cur_row][cur_col]
            if element == "D":
                decorations += 1
            elif element == "G":
                gifts += 1
            elif element == "C":
                cookies += 1
            matrix[cur_row][cur_col] = "x"

    elif direction == "down":
        for _ in range(steps):
            matrix[cur_row][cur_col] = "x"
            if cur_row + 1 > rows - 1:
                cur_row = 0
            else:
                cur_row += 1
            element = matrix[cur_row][cur_col]
            if element == "D":
                decorations += 1
            elif element == "G":
                gifts += 1
            elif element == "C":
                cookies += 1
            matrix[cur_row][cur_col] = "x"

    elif direction == "left":
        for _ in range(steps):
            matrix[cur_row][cur_col] = "x"
            if cur_col - 1 < 0:
                cur_col = cols - 1
            else:
                cur_col -= 1
            element = matrix[cur_row][cur_col]
            if element == "D":
                decorations += 1
            elif element == "G":
                gifts += 1
            elif element == "C":
                cookies += 1
            matrix[cur_row][cur_col] = "x"

    elif direction == "right":
        for _ in range(steps):
            matrix[cur_row][cur_col] = "x"
            if cur_col + 1 > cols - 1:
                cur_col = 0
            else:
                cur_col += 1
            element = matrix[cur_row][cur_col]
            if element == "D":
                decorations += 1
            elif element == "G":
                gifts += 1
            elif element == "C":
                cookies += 1
            matrix[cur_row][cur_col] = "x"

if all_collected(matrix):
    print("Merry Christmas!")

print(f"You've collected:\n"
      f"- {decorations} Christmas decorations\n"
      f"- {gifts} Gifts\n"
      f"- {cookies} Cookies")

for row in matrix:
    print(*row, sep=" ")
