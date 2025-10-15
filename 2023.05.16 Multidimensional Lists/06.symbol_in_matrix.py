rows = int(input())
matrix = []
flag = False

for _ in range(rows):
    matrix.extend([el for el in input().split()])

symbol = input()
for row in range(rows):
    for el in matrix[row]:
        if symbol == el:
            print(f"({row}, {matrix[row].index(el)})")
            flag = True
            break
    if flag:
        break

if not flag:
    print(f"{symbol} does not occur in the matrix")
