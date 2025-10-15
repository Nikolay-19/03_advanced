import sys

rows, cols = [int(el) for el in input().split(", ")]
matrix = []
max_sum = -sys.maxsize
max_matrix = []

for _ in range(rows):
    matrix.append([int(el) for el in input().split(", ")])

for row in range(rows - 1):
    for col in range(cols - 1):
        current = matrix[row][col]
        next_el = matrix[row][col + 1]
        below = matrix[row + 1][col]
        diagonal = matrix[row + 1][col + 1]
        sub_sum = current + next_el + below + diagonal

        if sub_sum > max_sum:
            max_sum = sub_sum
            max_matrix = [[current, next_el], [below, diagonal]]

print(*max_matrix[0])
print(*max_matrix[1])
print(max_sum)
