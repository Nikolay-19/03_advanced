rows, cols = [int(el) for el in input().split(", ")]
matrix = []

for _ in range(rows):
    matrix.append([int(el) for el in input().split()])

for col in range(cols):
    sum_col = 0
    for row in range(rows):
        el = matrix[row][col]
        sum_col += el
    print(sum_col)
