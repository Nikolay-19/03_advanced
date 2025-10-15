command_qt = int(input())

stack1 = []

for _ in range(command_qt):
    command = input().split()
    if int(command[0]) == 1:
        stack1.append(int(command[1]))

    elif int(command[0]) == 2 and stack1:
        stack1.pop()

    elif int(command[0]) == 3 and stack1:
        print(max(stack1))

    elif int(command[0]) == 4 and stack1:
        print(min(stack1))

print(*stack1[::-1], sep=", ")
