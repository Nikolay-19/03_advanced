def vowel_filter(function):
    def wrapper():
        return [el for el in function() if el.lower() in ["a", "e", "i", "o", "u", "y"]]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
