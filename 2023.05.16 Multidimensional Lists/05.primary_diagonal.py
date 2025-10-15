rows = int(input())
matrix = []
diagonal = 0

for _ in range(rows):
    matrix.append([int(el) for el in input().split()])

for row in range(rows):
    for col in range(rows):
        if row == col:
            diagonal += matrix[row][col]

print(diagonal)
