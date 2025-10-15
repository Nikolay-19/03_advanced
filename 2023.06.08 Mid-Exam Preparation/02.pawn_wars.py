def get_next_pos(row, col, direction, matrix):
    if direction == "up_left":
        return matrix[row - 1][col - 1]
    if direction == "up":
        return matrix[row - 1][col]
    if direction == "up_right":
        return matrix[row - 1][col + 1]
    if direction == "down_left":
        return matrix[row + 1][col - 1]
    if direction == "down":
        return matrix[row + 1][col]
    if direction == "down_right":
        return matrix[row + 1][col + 1]

move = 0
board = []
matrix = []
white_row = 0
white_col = 0
black_row = 0
black_col = 0

for _ in range(8):
    matrix.append([el for el in input().split()])

for row in range(8):
    for col in range(8):
        if matrix[row][col] == "w":
            white_row = row
            white_col = col
        elif matrix[row][col] == "b":
            black_row = row
            black_col = col

for row in range(8, 0, -1):
    b = []
    for col in range(97, 105):
        b.append(f"{chr(col)}{row}")
    board.append(b)

while True:
    if move % 2 == 0:
        if 0 <= white_row - 1 < 8:
            white_next = get_next_pos(white_row, white_col, "up", matrix)
            if white_row - 1 == 0:
                print(f"Game over! White pawn is promoted to a queen at {board[white_row - 1][white_col]}.")
                break

        if 0 <= white_row - 1 < 8 and 0 <= white_col - 1 < 8:
            white_left = get_next_pos(white_row, white_col, "up_left", matrix)
            if white_left == "b":
                print(f"Game over! White win, capture on {board[white_row - 1][white_col - 1]}.")
                break

        if 0 <= white_row - 1 < 8 and 0 <= white_col + 1 < 8:
            white_right = get_next_pos(white_row, white_col, "up_right", matrix)
            if white_right == "b":
                print(f"Game over! White win, capture on {board[white_row - 1][white_col + 1]}.")
                break

    else:
        if 0 <= black_row + 1 < 8:
            black_next = get_next_pos(black_row, black_col, "down", matrix)
            if black_row + 1 == 7:
                print(f"Game over! Black pawn is promoted to a queen at {board[black_row + 1][black_col]}.")
                break

        if 0 <= black_row + 1 < 8 and 0 <= black_col - 1 < 8:
            black_left = get_next_pos(black_row, black_col, "down_left", matrix)
            if black_left == "w":
                print(f"Game over! Black win, capture on {board[black_row + 1][black_col - 1]}.")
                break

        if 0 <= black_row + 1 < 8 and 0 <= black_col + 1 < 8:
            black_right = get_next_pos(black_row, black_col, "down_right", matrix)
            if black_right == "w":
                print(f"Game over! Black win, capture on {board[black_row + 1][black_col + 1]}.")
                break

    matrix[white_row][white_col] = "-"
    matrix[black_row][black_col] = "-"

    if move % 2 == 0:
        white_row -= 1
    else:
        black_row += 1

    move += 1
    matrix[white_row][white_col] = "w"
    matrix[black_row][black_col] = "b"
