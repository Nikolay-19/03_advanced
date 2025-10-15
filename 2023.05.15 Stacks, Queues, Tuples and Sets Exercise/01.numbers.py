set1 = set(int(el) for el in input().split())
set2 = set(int(el) for el in input().split())
commands_qt = int(input())

for _ in range(commands_qt):
    command = input().split()
    nums = [int(el) for el in command[2:]]

    if command[0] == "Add" and command[1] == "First":
        for num in nums:
            set1.add(num)
    elif command[0] == "Add" and command[1] == "Second":
        for num in nums:
            set2.add(num)

    elif command[0] == "Remove" and command[1] == "First":
        for num in nums:
            if num in set1:
                set1.remove(num)
    elif command[0] == "Remove" and command[1] == "Second":
        for num in nums:
            if num in set2:
                set2.remove(num)

    else:
        print(set1.issubset(set2) or set2.issubset(set1))

print(*sorted(set1), sep=", ")
print(*sorted(set2), sep=", ")
