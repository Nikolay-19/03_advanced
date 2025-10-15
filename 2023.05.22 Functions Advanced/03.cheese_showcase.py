def sorting_cheeses(**kwargs):
    cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ""
    for key, values in cheeses:
        result += key + '\n'
        val1 = sorted(values, reverse=True)
        result += '\n'.join(str(el) for el in val1) + '\n'

    return result
