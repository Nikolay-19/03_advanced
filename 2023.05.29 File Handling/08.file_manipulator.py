from os import path, remove

file_path = path.abspath(".") + "\\"

while True:
    command = input().split("-")
    if command[0] == "End":
        break

    elif command[0] == "Create":
        file_name = command[1]
        with open(file_path + file_name, "w") as file1:
            pass

    elif command[0] == "Add":
        file_name = command[1]
        content = command[2]

        try:
            with open(file_path + file_name, "a") as file1:
                file1.write(f"{content}\n")

        except FileNotFoundError:
            with open(file_path + file_name, "w") as file1:
                file1.write(f"{content}\n")

    elif command[0] == "Replace":
        file_name = command[1]
        old_string = command[2]
        new_string = command[3]

        try:
            with open(file_path + file_name) as file1:
                content = file1.read()
                content = content.replace(old_string, new_string)

            with open(file_path + file_name, "w") as file1:
                file1.write(content)

        except FileNotFoundError:
            print("An error occurred")

    elif command[0] == "Delete":
        file_name = command[1]

        try:
            remove(file_path + file_name)
        except FileNotFoundError:
            print("An error occurred")
