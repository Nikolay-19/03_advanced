def even_odd(*args):
    command = args[-1]
    nums = [int(el) for el in args[:-1]]

    if command == "even":
        return [int(el) for el in nums if el % 2 == 0]
    elif command == "odd":
        return [int(el) for el in nums if el % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
