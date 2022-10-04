def find_average_marks(marks):
    sum_of_marks=sum(marks)
    total_subjects=len(marks)
    average_marks=sum_of_marks/total_subjects
    return average_marks
def total_grade(average_marks):
    if average_marks>=80:
        grade='A'
    elif average_marks>=60:
        grade='B'
    elif average_marks>=50:
        grade='C'
    else:
        grade='C'
    return grade
marks=[95,85,75,80,65]
average_marks=find_average_marks(marks)
print(average_marks)
grade=total_grade(average_marks)
print("your grade is",grade)