from functools import wraps


def logged(function):
    @wraps(function)
    def wrapper(*args):
        return f"you called {function.__name__}({', '.join(str(el) for el in args)})\n" \
               f"it returned {function(*args)}"

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


@logged
def sum_func(a, b):
    return a + b


print(func(4, 4, 4))
print(sum_func(1, 4))
