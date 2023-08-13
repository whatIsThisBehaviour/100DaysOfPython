students_score = {
    "Alex": 81,
    "Cinderella": 95,
    "Yu": 62,
    "Angela": 75,
    "John Prunell": 98,
    "Sophia": 54,
    "Judo": 87,
    "Sara": 67,
    "Clara": 85,
}

students_grades = {}
for student in students_score:
    score = students_score[student]
    if score > 90:
        students_grades[student] = "Outstanding"
    elif score > 80:
        students_grades[student] = "Exceeds Expectations"
    elif score > 70:
        students_grades[student] = "Acceptable"
    else:
        students_grades[student] = "Fail"

print(students_grades)


