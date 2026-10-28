# Repeated Transaction Detection

transactions = [
    ("T101", 500),
    ("T102", 1000),
    ("T101", 500),
    ("T103", -200),
    ("T104", 750),
    ("T102", 1000)
]

processed_ids = []
repeated_count = 0
invalid_count = 0

for transaction in transactions:
    transaction_id, amount = transaction

    if amount <= 0:
        print(transaction_id, "- Invalid transaction")
        invalid_count += 1

    elif transaction_id in processed_ids:
        print(transaction_id, "- Repeated transaction")
        repeated_count += 1

    else:
        processed_ids.append(transaction_id)
        print(transaction_id, "- Valid transaction")

print("Transaction Summary")
print("Unique transactions:", len(processed_ids))
print("Repeated transactions:", repeated_count)
print("Invalid transactions:", invalid_count)
