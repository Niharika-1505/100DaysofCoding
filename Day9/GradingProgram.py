student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

for key, value in student_scores.items():
    if 91 <= value <= 100:
        student_grades = "Outstanding"
    elif 81 <= value <= 90:
        student_grades = "Exceeds Expectations"
    elif 71 <= value <= 80:
        student_grades = "Acceptable"
    elif value <= 70:
        student_grades = "Fail"
    print(f"{key} score is {student_grades}")
