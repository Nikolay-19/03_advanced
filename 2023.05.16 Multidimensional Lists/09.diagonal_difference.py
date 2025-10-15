rows = int(input())
matrix = []
left_diagonal = []
right_diagonal = []
left_diagonal_sum = 0
right_diagonal_sum = 0

for row in range(rows):
    matrix.append([int(el) for el in input().split()])

for row in range(rows):
    for col in range(rows):
        if row == col:
            left_diagonal.append(matrix[row][col])
            left_diagonal_sum += matrix[row][col]

matrix.reverse()

for row in range(rows):
    for col in range(rows):
        if row == col:
            right_diagonal.append(matrix[row][col])
            right_diagonal_sum += matrix[row][col]

print(abs(left_diagonal_sum - right_diagonal_sum))
