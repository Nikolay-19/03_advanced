def movie_organizer(*tuples):
    dict1 = {}
    result = ""
    for el in tuples:
        name = el[0]
        genre = el[1]
        if genre not in dict1:
            dict1[genre] = [name]
        else:
            dict1[genre].append(name)

    dict1 = sorted(dict1.items(), key=lambda x: (-len(x[1]), x[0]))
    for el in dict1:
        result += f"{el[0]} - {len(el[1])}\n"
        for i in sorted(el[1]):
            result += f"* {i}\n"

    return result
