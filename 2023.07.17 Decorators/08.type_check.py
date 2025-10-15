def type_check(type1):
    def decorator(function):
        def wrapper(var):
            if not isinstance(var, type1):
                return "Bad Type"
            return function(var)
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2("Not A Number"))
