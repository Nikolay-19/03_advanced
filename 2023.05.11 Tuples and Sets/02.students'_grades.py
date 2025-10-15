students_qt = int(input())
students = {}

for _ in range(students_qt):
    command = input().split()
    student = command[0]
    grade = float(command[1])

    if student not in students:
        students[student] = [grade]
    else:
        students[student].append(grade)

for student in students:
    grades = students[student]
    average = sum(grades) / len(grades)
    print(f"{student} -> ", end="")
    for grade in grades:
        print(f"{grade:.2f}", end=" ")
    print(f"(avg: {average:.2f})")
