import functools
def operate(operator, *args):

    return functools.reduce(lambda a, b: eval(f"{a}{operator}{b}"), args)


print(operate("/", 1, 2, 3, 4))
