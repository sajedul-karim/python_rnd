students = [
    ("Grade 1", "Alice"),
    ("Grade 2", "Bob"),
    ("Grade 1", "Charlie"),
    ("Grade 3", "David"),
    ("Grade 2", "Eve"),
]

students_by_grade = {
    grade: [
        student_name
        for grade_, student_name in students
        if grade_ == grade
    ]
    for grade in {grade_ for grade_, _ in students}
}

print(students_by_grade)
