def age_assignment(*names, **dict1):
    result = []
    
    for name in names:
        for key, value in dict1.items():
            if name[0] == key:
                result.append(f"{name} is {value} years old.")

    return "\n".join(sorted(result))
