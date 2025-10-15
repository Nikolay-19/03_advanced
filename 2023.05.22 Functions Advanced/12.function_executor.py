def func_executor(*functions):
    result = []
    
    for func_name, func_data in functions:
        result.append(f"{func_name.__name__} - {func_name(*func_data)}")
    
    return "\n".join(result)
    