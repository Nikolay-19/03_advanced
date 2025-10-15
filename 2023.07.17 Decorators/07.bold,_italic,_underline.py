def make_bold(function):
    def decorator(*args):
        return f"<b>{function(*args)}</b>"
    return decorator


def make_italic(function):
    def decorator(*args):
        return f"<i>{function(*args)}</i>"
    return decorator


def make_underline(function):
    def decorator(*args):
        return f"<u>{function(*args)}</u>"
    return decorator


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(str(el) for el in args)}"


print(greet("Peter"))
print(greet_all("Peter", "George"))