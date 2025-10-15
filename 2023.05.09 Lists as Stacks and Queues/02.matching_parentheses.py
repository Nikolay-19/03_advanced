string1 = input()
stack1 = []

for idx in range(len(string1)):
    if string1[idx] == "(":
        stack1.append(idx)
    elif string1[idx] == ")":
        start_idx = stack1.pop()
        end_idx = idx + 1
        print(string1[start_idx:end_idx], sep="")
