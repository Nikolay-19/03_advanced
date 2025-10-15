def naughty_or_nice_list(sc_list, *args, **kwargs):
    nice = []
    result = []
    naughty = []
    not_found = []

    def unique_num(list1, unq_num):
        count = 0
        for el in list1:
            num = el[0]
            if num == unq_num:
                name = el[1]
                count += 1
        if count == 1:
            list1.remove((unq_num, name))
            return name

    def unique_name(list1, unq_name):
        count = 0
        for el in list1:
            name = el[1]
            if name == unq_name:
                count += 1
        if count == 1:
            for el in list1.copy():
                if el[1] == unq_name:
                    list1.remove(el)
            return True

    for arg in args:
        command = arg.split("-")
        if command[1] == "Naughty":
            naughty.append(unique_num(sc_list, int(command[0])))
        elif command[1] == "Nice":
            nice.append(unique_num(sc_list, int(command[0])))

    for name, behaved in kwargs.items():
        if behaved == "Nice":
            if unique_name(sc_list, name):
                nice.append(name)
        elif behaved == "Naughty":
            if unique_name(sc_list, name):
                naughty.append(name)

    for el in sc_list.copy():
        not_found.append(el[1])
        sc_list.remove(el)

    while None in nice:
        nice.remove(None)
    while None in naughty:
        naughty.remove(None)
    while None in not_found:
        not_found.remove(None)

    if nice:
        result.append(f"Nice: {', '.join(nice)}")
    if naughty:
        result.append(f"Naughty: {', '.join(naughty)}")
    if not_found:
        result.append(f"Not found: {', '.join(not_found)}")

    return "\n".join(result)


print(naughty_or_nice_list([(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy"), ], "3-Nice", "1-Naughty", Amy="Nice",
                           Katy="Naughty", ))
print(naughty_or_nice_list([(7, "Peter"), (1, "Lilly"), (2, "Peter"), (12, "Peter"), (3, "Simon"), ], "3-Nice",
                           "5-Naughty", "2-Nice", "1-Nice", ))
print(naughty_or_nice_list([(6, "John"), (4, "Karen"), (2, "Tim"), (1, "Merry"), (6, "Frank"), ], "6-Nice", "5-Naughty",
                           "4-Nice", "3-Naughty", "2-Nice", "1-Naughty", Frank="Nice", Merry="Nice", John="Naughty", ))
