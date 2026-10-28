# Food Waste Monitoring System

food_data = [
    ("Day 1", 100, 90),
    ("Day 2", 120, 100),
    ("Day 3", 80, 76),
    ("Day 4", 150, 120),
    ("Day 5", 100, 95)
]

wastage_limit = 10

total_prepared = 0
total_served = 0
total_leftover = 0

for day in food_data:
    day_name, prepared, served = day

    leftover = prepared - served
    wastage_percentage = (leftover / prepared) * 100

    print(day_name)
    print("Meals Prepared:", prepared)
    print("Meals Served:", served)
    print("Leftover Meals:", leftover)
    print("Wastage Percentage:", round(wastage_percentage, 2), "%")

    if wastage_percentage > wastage_limit:
        print("Excessive Food Wastage")
    else:
        print("Food Wastage Within Limit")

    total_prepared += prepared
    total_served += served
    total_leftover += leftover

print("Overall Food Waste Summary")
print("Total Meals Prepared:", total_prepared)
print("Total Meals Served:", total_served)
print("Total Leftover Meals:", total_leftover)

overall_wastage = (total_leftover / total_prepared) * 100
print("Overall Wastage Percentage:", round(overall_wastage, 2), "%")
