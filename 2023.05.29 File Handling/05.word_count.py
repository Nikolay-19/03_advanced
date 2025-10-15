result = {}
content2 = []

with open("words.txt") as words_file:
    words = [el for el in words_file.readline().split()]

with open("input.txt") as input_file:
    content = [line[:-2].lower() for line in input_file.readlines()]

for sentence in content:
    sentence = sentence.split()
    content2.append(sentence)

for word in words:
    if word not in result:
        result[word] = 0

for sentence in content2:
    for word in sentence:
        if not word.isalpha():
            for char in word:
                if not char.isalpha():
                    word = word.replace(char, "")
        if word in words:
            result[word] += 1

with open("output.txt", "w") as output_file:
    result_tuple = sorted(result.items(), key=lambda x: -x[1])
    for el in result_tuple:
        output_file.write(f"{el[0]} - {el[1]}\n")
