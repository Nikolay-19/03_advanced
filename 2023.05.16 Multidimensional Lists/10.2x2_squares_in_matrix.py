rows, cols = [int(el) for el in input().split()]
matrix = []
total = 0

for _ in range(rows):
    matrix.append([el for el in input().split()])

for row in range(rows - 1):
    for col in range(cols - 1):
        
        current = matrix[row][col]
        next_el = matrix[row][col + 1]
        below = matrix[row + 1][col]
        diagonal = matrix[row + 1][col + 1]

        if current == next_el == below == diagonal:
            total += 1

print(total)
