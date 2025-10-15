from collections import deque

words = ["rose", "tulip", "lotus", "daffodil"]
vowels = deque(char for char in input().split())      # FIFO
consonants = deque(char for char in input().split())  # LIFO

while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    if vowel in words[0]:
        words[0] = words[0].replace(vowel, "")
    if consonant in words[0]:
        words[0] = words[0].replace(consonant, "")
    if len(words[0]) == 0:
        print(f"Word found: rose")
        if vowels:
            print(f"Vowels left: {' '.join(vowels)}")
        if consonants:
            print(f"Consonants left: {' '.join(consonants)}")
        break

    if vowel in words[1]:
        words[1] = words[1].replace(vowel, "")
    if consonant in words[1]:
        words[1] = words[1].replace(consonant, "")
    if len(words[1]) == 0:
        print(f"Word found: tulip")
        if vowels:
            print(f"Vowels left: {' '.join(vowels)}")
        if consonants:
            print(f"Consonants left: {' '.join(consonants)}")
        break

    if vowel in words[2]:
        words[2] = words[2].replace(vowel, "")
    if consonant in words[2]:
        words[2] = words[2].replace(consonant, "")
    if len(words[2]) == 0:
        print(f"Word found: lotus")
        if vowels:
            print(f"Vowels left: {' '.join(vowels)}")
        if consonants:
            print(f"Consonants left: {' '.join(consonants)}")
        break

    if vowel in words[3]:
        words[3] = words[3].replace(vowel, "")
    if consonant in words[3]:
        words[3] = words[3].replace(consonant, "")
    if len(words[3]) == 0:
        print(f"Word found: daffodil")
        if vowels:
            print(f"Vowels left: {' '.join(vowels)}")
        if consonants:
            print(f"Consonants left: {' '.join(consonants)}")
        break

else:
    print("Cannot find any word!")
    if vowels:
        print(f"Vowels left: {' '.join(vowels)}")
    if consonants:
        print(f"Consonants left: {' '.join(consonants)}")
