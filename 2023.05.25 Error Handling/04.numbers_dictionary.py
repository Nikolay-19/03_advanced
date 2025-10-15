nums = {}

while True:
    command = input().lower()
    if command == "end":
        break

    elif command != "search" and command != "remove" and not isinstance(command, int) and not isinstance(command, float):
        num_str = command
        try:
            num_int = int(input())
            nums[num_str] = num_int
        except ValueError:
            print("The variable number must be an integer")

    elif command == "search":
        num_str = input().lower()
        if num_str == "remove":
            continue
        try:
            print(nums[num_str])
        except KeyError:
            print("Number does not exist in dictionary")

    elif command == "remove":
        num_str = input().lower()
        if num_str == "end":
            break
        try:
            nums.pop(num_str)
        except KeyError:
            print("Number does not exist in dictionary")

print(nums)
