def add_element(element, row, col):
    if element == "W":
        materials_found["W"].append([row, col])
        print(f"Water deposit found at ({row}, {col})")
    elif element == "M":
        materials_found["M"].append([row, col])
        print(f"Metal deposit found at ({row}, {col})")
    elif element == "C":
        materials_found["C"].append([row, col])
        print(f"Concrete deposit found at ({row}, {col})")


matrix = []
rover_row = 0
rover_col = 0
materials = ["W", "M", "C"]
materials_found = {"W": [], "M": [], "C": []}

for _ in range(6):
    matrix.append(input().split())

commands = input().split(", ")

for row in range(6):
    for col in range(6):
        if matrix[row][col] == "E":
            rover_row = row
            rover_col = col

for command in commands:
    if command == "up":
        matrix[rover_row][rover_col] = "-"
        if rover_row - 1 < 0:
            rover_row = 5
        else:
            rover_row -= 1
        element = matrix[rover_row][rover_col]
        if element == "R":
            print(f"Rover got broken at ({rover_row}, {rover_col})")
            break
        else:
            add_element(element, rover_row, rover_col)
        matrix[rover_row][rover_col] = "E"

    elif command == "down":
        matrix[rover_row][rover_col] = "-"
        if rover_row + 1 > 5:
            rover_row = 0
        else:
            rover_row += 1
        element = matrix[rover_row][rover_col]
        if element == "R":
            print(f"Rover got broken at ({rover_row}, {rover_col})")
            break
        else:
            add_element(element, rover_row, rover_col)
        matrix[rover_row][rover_col] = "E"

    elif command == "left":
        matrix[rover_row][rover_col] = "-"
        if rover_col - 1 < 0:
            rover_col = 5
        else:
            rover_col -= 1
        element = matrix[rover_row][rover_col]
        if element == "R":
            print(f"Rover got broken at ({rover_row}, {rover_col})")
            break
        else:
            add_element(element, rover_row, rover_col)
        matrix[rover_row][rover_col] = "E"

    elif command == "right":
        matrix[rover_row][rover_col] = "-"
        if rover_col + 1 > 5:
            rover_col = 0
        else:
            rover_col += 1
        element = matrix[rover_row][rover_col]
        if element == "R":
            print(f"Rover got broken at ({rover_row}, {rover_col})")
            break
        else:
            add_element(element, rover_row, rover_col)
        matrix[rover_row][rover_col] = "E"

if len(materials_found["W"]) >= 1 and len(materials_found["M"]) >= 1 and len(materials_found["C"]) >= 1:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
