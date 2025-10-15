rows = int(input())

matrix = []

for i in range(rows):
    # matrix.append([int(el) for el in input().split(", ") if el % 2 == 0])
    nums = [int(el) for el in input().split(", ")]
    matrix.append([el for el in nums if el % 2 == 0])

print(matrix)
