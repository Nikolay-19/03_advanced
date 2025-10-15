file1 = open("numbers.txt")
content = sum([int(el) for el in file1.readlines()])
print(content)
