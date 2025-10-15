from os import path

file_path = path.abspath(".") + "\\"
MARKS = ("-", ",", ".", "!", "?")
result = []

with open(file_path + "text.txt") as file1:
    content = [line for line in file1.readlines()]

for idx in range(len(content)):
    if idx % 2 == 0:
        result.append(content[idx][:-1].split())

for line in result:
    for word in range(len(line)):
        if not line[word].isalpha():
            for char in line[word]:
                if char in MARKS:
                    line[word] = line[word].replace(char, "@")

for sentence in result:
    for word in sentence[::-1]:
        print(word, end=" ")
    print()
