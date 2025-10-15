rows, cols = [int(el) for el in input().split(", ")]

matrix = []
sum_matrix = 0

for _ in range(rows):
    nums = [int(el) for el in input().split(", ")]
    matrix.append(nums)
    sum_matrix += sum(nums)

print(sum_matrix)
print(matrix)
