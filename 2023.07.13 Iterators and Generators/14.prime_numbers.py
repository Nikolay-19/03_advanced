def get_primes(nums):
    for num in nums:
        count1 = 0
        for b in range(1, num + 1):
            if num % b == 0:
                count1 += 1
        if count1 == 2:
            yield num
        count1 = 0
