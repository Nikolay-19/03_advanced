def reverse_text(string1):
    for i in range(len(string1) - 1, -1, -1):
        yield string1[i]
