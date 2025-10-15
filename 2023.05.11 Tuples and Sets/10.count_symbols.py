string1 = tuple(el for el in input())
count = {}

for char in string1:
    if char not in count:
        count[char] = 0
    count[char] += 1

for key, value in sorted(count.items()):
    print(f"{key}: {value} time/s")
