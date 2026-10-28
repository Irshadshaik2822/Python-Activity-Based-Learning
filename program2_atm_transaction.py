# ATM Transaction Sequence Simulation

balance = 10000
withdrawal_limit = 5000
transactions = []

for i in range(5):
    print("Transaction", i + 1)
    transaction_type = input(
        "Enter deposit or withdrawal: "
    ).lower()
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount")
        transactions.append("Invalid amount")

    elif transaction_type == "deposit":
        balance += amount
        print("Deposit successful")
        transactions.append(
            ("Deposit", amount, balance)
        )

    elif transaction_type == "withdrawal":
        if amount > withdrawal_limit:
            print("Withdrawal limit exceeded")
            transactions.append(
                "Withdrawal limit exceeded"
            )
        elif amount > balance:
            print("Insufficient balance")
            transactions.append(
                "Insufficient balance"
            )
        else:
            balance -= amount
            print("Withdrawal successful")
            transactions.append(
                ("Withdrawal", amount, balance)
            )

    else:
        print("Invalid transaction type")
        transactions.append(
            "Invalid transaction type"
        )

print("Transaction Summary")
for transaction in transactions:
    print(transaction)

print("Final Account Balance: Rs.", balance)
