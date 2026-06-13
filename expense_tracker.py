income = 0
expense = 0

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amt = int(input("Enter income amount: "))
        income += amt
        print("Income added successfully!")

    elif choice == "2":
        amt = int(input("Enter expense amount: "))
        expense += amt
        print("Expense added successfully!")

    elif choice == "3":
        balance = income - expense
        print("\n----- SUMMARY -----")
        print("Total Income:", income)
        print("Total Expense:", expense)
        print("Balance:", balance)

    elif choice == "4":
        print("Exiting... Thank you bro!")
        break

    else:
        print("Invalid choice! Try again.")
