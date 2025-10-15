def concatenate(*args, **kwargs):
    temp_string = "".join([el for el in args])
    replace_dict = kwargs

    for key, value in replace_dict.items():
        if key in temp_string:
            temp_string = temp_string.replace(key, value)
    
    return  temp_string
