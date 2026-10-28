# Multi-Stage Examination Eligibility System

students = [
    ("Anu", 85, 30, True),
    ("Ravi", 65, 25, True),
    ("Sita", 80, 15, True),
    ("Kiran", 90, 32, False)
]

minimum_attendance = 75
minimum_marks = 20

for student in students:
    name, attendance, marks, assignment_status = student

    print("Student Name:", name)

    if (attendance >= minimum_attendance
            and marks >= minimum_marks
            and assignment_status == True):

        print("Eligible for Examination")

    else:
        print("Not Eligible for Examination")

        if attendance < minimum_attendance:
            print("Reason: Attendance is below 75%")

        if marks < minimum_marks:
            print("Reason: Internal marks are below 20")

        if assignment_status == False:
            print("Reason: Assignments are incomplete")
