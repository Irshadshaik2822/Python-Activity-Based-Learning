# Advanced String-Based Registration Record Analyzer

records = [
    "2025-CS-1001",
    "2025-EC-1002",
    "2025-CS-1001",
    "25-ME-1003",
    "2025-IT-10A4",
    "2024-EE-1005",
    "2025-it-1006"
]

processed_records = []

valid_count = 0
duplicate_count = 0
invalid_count = 0

for record in records:
    print("Registration Record:", record)

    parts = record.split("-")

    if len(parts) != 3:
        print("Status: Invalid Registration Record")
        invalid_count += 1
        continue

    year, branch, student_number = parts

    if (len(year) != 4 or not year.isdigit()
            or len(branch) != 2
            or not branch.isalpha()
            or not branch.isupper()
            or len(student_number) != 4
            or not student_number.isdigit()):

        print("Status: Invalid Registration Record")
        invalid_count += 1

    elif record in processed_records:
        print("Status: Duplicate Registration Record")
        duplicate_count += 1

    else:
        processed_records.append(record)
        valid_count += 1

        print("Status: Valid Registration Record")
        print("Admission Year:", year)
        print("Branch Code:", branch)
        print("Student Number:", student_number)

print("Registration Analysis Summary")
print("Valid Records:", valid_count)
print("Duplicate Records:", duplicate_count)
print("Invalid Records:", invalid_count)
