total_marks_of_students = input("Please enter marks followed by space : ").split()
for marks in range(0, len(total_marks_of_students)):
    total_marks_of_students[marks] = int(total_marks_of_students[marks])
highest_marks = 0
for marks in total_marks_of_students:
    if marks > highest_marks:
        highest_marks = marks
print(highest_marks)