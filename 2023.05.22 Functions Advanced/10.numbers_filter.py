def even_odd_filter(**kwargs):
    nums_dict = {}
    
    for key, value in kwargs.items():
        if key == "odd":
            nums_dict["odd"] = [int(el) for el in value if el % 2 != 0]
        elif key == "even":
            nums_dict["even"] = [int(el) for el in value if el % 2 == 0]

    result = dict(sorted(nums_dict.items(), key=lambda kv: (len(kv[1]), kv[0]), reverse=True))
    
    return result
