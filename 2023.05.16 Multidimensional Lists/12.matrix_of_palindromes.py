rows, cols = [int(el) for el in input().split()]
matrix = []

for row in range(rows):
    sub_list = []
    for col in range(cols):
        sub_list.append(chr(97 + row))
        sub_list.append(chr(97 + col + row))
        sub_list.append(chr(97 + row))
        print(chr(97 + row) + chr(97 + col + row) + chr(97 + row), end=" ")
        matrix.append(sub_list)
        sub_list = []
    print()
