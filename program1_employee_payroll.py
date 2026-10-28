# Employee Payroll and Deduction Analysis

employee_name = input("Enter employee name: ")

basic_pay = float(input("Enter basic pay: "))
allowances = float(input("Enter allowances: "))
overtime_pay = float(input("Enter overtime pay: "))
incentives = float(input("Enter incentives: "))

gross_salary = (
    basic_pay + allowances + overtime_pay + incentives
)

if gross_salary >= 50000:
    deduction_rate = 0.10
else:
    deduction_rate = 0.05

deduction = gross_salary * deduction_rate
net_salary = gross_salary - deduction

print("Employee Name :", employee_name)
print("Basic Pay     : Rs.", basic_pay)
print("Allowances    : Rs.", allowances)
print("Overtime Pay  : Rs.", overtime_pay)
print("Incentives    : Rs.", incentives)
print("Gross Salary  : Rs.", gross_salary)
print("Deduction     : Rs.", deduction)
print("Net Salary    : Rs.", net_salary)
