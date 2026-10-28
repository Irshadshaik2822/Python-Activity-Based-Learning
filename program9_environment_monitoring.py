# Environmental Monitoring Data Analyzer

environment_data = [
    ("Zone A", 32, 85, 7.2),
    ("Zone B", 42, 130, 6.0),
    ("Zone C", 38, 95, 7.5),
    ("Zone D", 41, 110, 8.8),
    ("Zone E", 29, 70, 6.8)
]

total_temperature = 0
total_aqi = 0
attention_count = 0

for zone in environment_data:
    name, temperature, aqi, ph = zone

    alerts = []

    if temperature > 40:
        alerts.append("High Temperature")

    if aqi > 100:
        alerts.append("Poor Air Quality")

    if ph < 6.5 or ph > 8.5:
        alerts.append("Abnormal Water pH")

    print("Monitoring Zone:", name)
    print("Temperature:", temperature, "C")
    print("Air Quality Index:", aqi)
    print("Water pH:", ph)

    if len(alerts) > 0:
        print("Alerts:", ", ".join(alerts))
        attention_count += 1
    else:
        print("Alerts: None")

    total_temperature += temperature
    total_aqi += aqi

average_temperature = total_temperature / len(environment_data)
average_aqi = total_aqi / len(environment_data)

print("Environmental Monitoring Summary")
print("Average Temperature:", round(average_temperature, 2), "C")
print("Average AQI:", round(average_aqi, 2))
print("Zones Requiring Attention:", attention_count)
