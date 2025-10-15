def generator1(num):
    n = 0
    while n < num:
        yield n
        n += 1
sum_n = sum(generator1(5))
print(sum_n)