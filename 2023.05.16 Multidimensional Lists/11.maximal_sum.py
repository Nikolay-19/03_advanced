import sys

rows, cols = [int(el) for el in input().split()]
matrix = []
max_sum = -sys.maxsize
max_matrix = 0

for _ in range(rows):
    matrix.append([int(el) for el in input().split()])

for row in range(rows - 2):
    for col in range(cols - 2):
        above_left = matrix[row][col]
        above_center = matrix[row][col + 1]
        above_right = matrix[row][col + 2]
        middle_left = matrix[row + 1][col]
        midle_center = matrix[row + 1][col + 1]
        middle_right = matrix[row + 1][col + 2]
        below_left = matrix[row + 2][col]
        below_center = matrix[row + 2][col + 1]
        below_right = matrix[row + 2][col + 2]

        sub_sum = above_left + above_center + above_right + middle_left + midle_center + middle_right + below_left + \
                  below_center + below_right

        if sub_sum > max_sum:
            max_sum = sub_sum
            max_matrix = [[above_left, above_center, above_right],
                          [middle_left, midle_center, middle_right],
                          [below_left, below_center, below_right]]

print(f"Sum = {max_sum}\n"
      f"{' '.join(str(el) for el in max_matrix[0])}\n"
      f"{' '.join(str(el) for el in max_matrix[1])}\n"
      f"{' '.join(str(el) for el in max_matrix[2])}")
