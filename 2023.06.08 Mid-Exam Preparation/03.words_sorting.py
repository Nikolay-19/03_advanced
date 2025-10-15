def words_sorting(*words):
    dict1 = {}
    sum_values = 0
    result = []

    for word in words:
        value1 = 0
        for char in word:
            value1 += ord(char)

        sum_values += value1
        dict1[word] = value1

    if sum_values % 2 == 0:
        for key, value in sorted(dict1.items(), key=lambda x: x[0]):
            result.append(f"{key} - {value}")

    elif sum_values % 2 != 0:
        for key, value in sorted(dict1.items(), key=lambda x: x[1], reverse=True):
            result.append(f"{key} - {value}")

    return "\n".join(result)


print(words_sorting('escape', 'charm', 'mythology'))
print(words_sorting('escape', 'charm', 'eye'))
print(words_sorting('cacophony', 'accolade'))
