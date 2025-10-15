nums = tuple(float(el) for el in input().split())
count = {}

for num in nums:
    if num not in count:
        count[num] = 0
    count[num] += 1

for key, value in count.items():
    print(f"{key} - {value} times")
