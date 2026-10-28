# Student Academic Risk Classification

students = [
    ("Anu", 75, 85, 80),
    ("Ravi", 35, 60, 30),
    ("Sita", 55, 70, 65),
    ("Kiran", 30, 80, 55),
    ("Meena", 65, 90, 35)
]

low_risk = 0
moderate_risk = 0
high_risk = 0

for student in students:
    name, marks, attendance, lab_score = student

    risk_factors = []

    if marks < 40:
        risk_factors.append("Low Marks")

    if attendance < 75:
        risk_factors.append("Low Attendance")

    if lab_score < 40:
        risk_factors.append("Low Laboratory Score")

    print("Student Name:", name)
    print("Marks:", marks)
    print("Attendance:", attendance, "%")
    print("Laboratory Score:", lab_score)

    if len(risk_factors) >= 2:
        print("Risk Factors:", ", ".join(risk_factors))
        print("Risk Category: High Risk")
        high_risk += 1

    elif len(risk_factors) == 1:
        print("Risk Factors:", ", ".join(risk_factors))
        print("Risk Category: Moderate Risk")
        moderate_risk += 1

    else:
        print("Risk Factors: None")
        print("Risk Category: Low Risk")
        low_risk += 1

print("Academic Risk Summary")
print("Low Risk Students:", low_risk)
print("Moderate Risk Students:", moderate_risk)
print("High Risk Students:", high_risk)
