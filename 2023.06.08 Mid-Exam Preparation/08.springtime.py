def start_spring(**kwargs):
    dict1 = {}
    result = ""
    for key, value in kwargs.items():
        if value not in dict1:
            dict1[value] = [key]
        else:
            dict1[value].append(key)

    dict1 = sorted(dict1.items(), key=lambda x: (-len(x[1]), x[0]))

    for kvp in dict1:
        type1 = kvp[0]
        list1 = sorted(kvp[1])
        result += f"{type1}:\n"
        for el in list1:
            result += f"-{el}\n"

    return result
