def genrange(start, end):
    return (el for el in range(start, end + 1))


print(list(genrange(1, 10)))
