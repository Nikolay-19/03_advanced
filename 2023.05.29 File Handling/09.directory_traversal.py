from os import walk, path

files = []
file_dict = {}
file_path = path.abspath(".") + "\\"
base_depth = file_path.rstrip(path.sep).count(path.sep)

for root, dirs, file in walk("."):
    cur_depth = root.count(path.sep)

    if base_depth <= cur_depth + 1:
        del dirs[:]
    files.append(file)

for el in files:
    for file in el:
        extension = path.splitext(file)[1]

        if extension not in file_dict:
            file_dict[extension] = [file]
        else:
            file_dict[extension].append(file)

with open(file_path + "report.txt", "w") as report:
    for key, value in sorted(file_dict.items()):
        report.write(f"{key}\n")

        for el in value:
            report.write(f"- - - {el}\n")
