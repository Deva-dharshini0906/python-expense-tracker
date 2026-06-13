import json

# Load existing data
try:
    with open("data.json", "r") as file:
        data = json.load(file)
        income = data["income"]
        expense = data["expense"]
except:
    income = 0
    expense = 0


# Save function
def save_data():
    data = {
        "income": income,
        "expense": expense
    }
    with open("data.json", "w") as file:
        json.dump(data, file)


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
        save_data()
        print("Income added successfully!")

    elif choice == "2":
        amt = int(input("Enter expense amount: "))
        expense += amt
        save_data()
        print("Expense added successfully!")

    elif choice == "3":
        print("\n----- SUMMARY -----")
        print("Total Income:", income)
        print("Total Expense:", expense)
        print("Balance:", income - expense)

    elif choice == "4":
        print("Exiting... Bye bro!")
        break

    else:
        print("Invalid choice! Try again.")
