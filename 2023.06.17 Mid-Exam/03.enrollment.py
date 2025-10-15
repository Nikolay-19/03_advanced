def gather_credits(number, *course_tuples):
    needed_credits = number
    dict1 = {}
    credits_total = 0

    for course in course_tuples:
        name = course[0]
        credit = int(course[1])

        if name not in dict1 and needed_credits > 0:
            needed_credits -= credit
            credits_total += credit
            dict1[name] = credit

    dict1 = sorted(dict1)

    if needed_credits > 0:
        return f"You need to enroll in more courses! You have to gather {needed_credits} credits more."
    else:
        return f"Enrollment finished! Maximum credits: {credits_total}.\nCourses: {', '.join(el for el in dict1)}"
