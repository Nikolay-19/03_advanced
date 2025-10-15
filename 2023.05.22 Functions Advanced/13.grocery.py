def grocery_store(**products):
    dict1 = dict(sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    result = []
    
    for key, value in dict1.items():
        result.append(f"{key}: {value}")
    
    return "\n".join(result)
