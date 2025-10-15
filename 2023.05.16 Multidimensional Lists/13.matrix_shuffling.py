rows, cols = [int(el) for el in input().split()]
matrix = []

for _ in range(rows):
    matrix.append([el for el in input().split()])

while True:
    command = input().split()
    if command[0] == "END":
        break
    if command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
        continue

    row1 = int(command[1])
    col1 = int(command[2])
    row2 = int(command[3])
    col2 = int(command[4])

    if row1 < 0 or row1 > rows or row2 < 0 or row2 > rows or col1 < 0 or col1 > cols or col2 < 0 or col2 > cols:
        print("Invalid input!")
        continue

    else:
        temp = matrix[row1][col1]
        matrix[row1][col1] = matrix[row2][col2]
        matrix[row2][col2] = temp
        temp = ""
        for row in matrix:
            print(*row, sep=" ")
