def print_upper(num):
    for i in range(1, num + 1):
        print(" " * (num - i) + "* " * i)


def print_lower(num):
    for j in range(num - 1, 0, -1):
        print(" " * (num - j) + "* " * j)


def print_rhombus():
    n = int(input())
    print_upper(n)
    print_lower(n)


print_rhombus()
