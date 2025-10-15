string1 = input().split("|")
sub_list = []

for el in string1[::-1]:
    sub_list.extend(el.split())
print(*sub_list)
