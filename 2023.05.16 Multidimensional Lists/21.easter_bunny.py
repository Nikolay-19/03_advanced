import sys

size = int(input())

matrix = []
bunny_row = 0
bunny_col = 0

for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)

    for col in range(size):
        if row_elements[col] == "B":
            bunny_row = row
            bunny_col = col

directions = {"right": lambda r, c: (r, c + 1),
              "left": lambda r, c: (r, c - 1),
              "up": lambda r, c: (r - 1, c),
              "down": lambda r, c: (r + 1, c)}

best_sum = float(-sys.maxsize)
best_dir = ""
best_path = []

for direction in directions:
    current_sum = 0
    current_path = []
    row, col = directions[direction](bunny_row, bunny_col)

    while 0 <= row < size and 0 <= col < size and matrix[row][col] != "X":
        current_path.append([row, col])
        current_sum += int(matrix[row][col])
        row, col = directions[direction](row, col)

    if current_sum > best_sum and current_path:
        best_dir = direction
        best_sum = current_sum
        best_path = current_path

print(best_dir)
print(*best_path, sep="\n")
print(best_sum)
