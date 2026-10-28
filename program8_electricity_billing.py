# Smart Electricity Billing for Multiple Apartments

apartments = [
    ("A101", 120),
    ("A102", 250),
    ("A103", 80),
    ("A104", 310),
    ("A105", 180)
]

fixed_charge = 50
total_units = 0
total_bill = 0

for apartment in apartments:
    apartment_number, units = apartment

    if units < 0:
        print("Invalid electricity consumption")
        continue

    if units <= 100:
        charge = units * 3

    elif units <= 200:
        charge = (100 * 3) + ((units - 100) * 5)

    else:
        charge = (100 * 3) + (100 * 5) + ((units - 200) * 7)

    bill = charge + fixed_charge

    print("Apartment Number:", apartment_number)
    print("Units Consumed:", units)
    print("Electricity Bill: Rs.", bill)

    if units > 200:
        print("High Electricity Consumption")

    total_units += units
    total_bill += bill

print("Overall Billing Summary")
print("Total Units Consumed:", total_units)
print("Total Electricity Bill: Rs.", total_bill)
