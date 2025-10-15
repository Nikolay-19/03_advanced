rows = int(input())
matrix = []

for _ in range(rows):
    matrix.extend([int(el) for el in input().split(", ")])

print(matrix)
