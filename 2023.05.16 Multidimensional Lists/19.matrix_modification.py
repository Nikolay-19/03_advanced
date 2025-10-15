rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append([int(el) for el in input().split()])

while True:
    command = input().split()
    if command[0] == "END":
        break

    row = int(command[1])
    col = int(command[2])
    value = int(command[3])

    if row > len(matrix) - 1 or col > len(matrix) - 1 or row < 0 or col < 0:
        print("Invalid coordinates")
        continue
    elif command[0] == "Add":
        matrix[row][col] += value
    elif command[0] == "Subtract":
        matrix[row][col] -= value

for row in matrix:
    print(f" ".join(str(el) for el in row))
