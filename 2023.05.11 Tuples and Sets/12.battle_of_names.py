names_qt = int(input())
even = set()
odd = set()

for i in range(1, names_qt + 1):
    name = input()
    name_sum = 0

    for char in name:
        name_sum += ord(char)
    name_sum //= i

    if name_sum % 2 == 0:
        even.add(name_sum)
    else:
        odd.add(name_sum)

even_sum = sum(even)
odd_sum = sum(odd)

if even_sum == odd_sum:
    print(even.union(odd))
elif odd_sum > even_sum:
    print(", ".join(str(el) for el in odd.difference(even)))
elif even_sum > odd_sum:
    print(", ".join(str(el) for el in even.symmetric_difference(odd)))
