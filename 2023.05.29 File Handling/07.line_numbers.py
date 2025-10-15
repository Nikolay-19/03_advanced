from os import path

file_path = path.abspath(".") + "\\"
result = []
MARKS = ("-", ",", ".", "!", "?", "'")
count = 0

with open(file_path + "text.txt") as file1:
    content = [line[:-1] for line in file1.readlines()]

with open(file_path + "output.txt", "w") as output1:
    pass

for line in content:
    alpha = 0
    mark = 0
    count += 1

    for char in line:
        if char.isalpha():
            alpha += 1
        elif char in MARKS:
            mark += 1

    with open(file_path + "output.txt", "a") as output1:
        output1.write(f"Line {count}: {line} ({alpha})({mark})\n")
