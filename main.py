import os
from datetime import datetime

# File to store expenses
EXPENSES_FILE = "expenses.txt"

# Predefined categories
CATEGORIES = ["Food", "Travel", "Entertainment", "Utilities", "Others"]

# Ensure the file exists
def initialize_file():
    if not os.path.exists(EXPENSES_FILE) or os.path.getsize(EXPENSES_FILE) == 0:
        with open(EXPENSES_FILE, "w") as file:
            file.write("Category,Amount,Date\n")

# Add an expense
def add_expense(category, amount, date):
    try:
        with open(EXPENSES_FILE, "a") as file:
            file.write(f"{category},{amount},{date}\n")
        print("Expense added successfully.")
    except Exception as e:
        print(f"Error adding expense: {e}")

# View expenses by category
def view_expenses_by_category():
    try:
        # Ensure the categories dictionary is populated
        expenses = {category: [] for category in CATEGORIES}
        with open(EXPENSES_FILE, "r") as file:
            next(file)  # Skip header
            for line in file:
                category, amount, date = line.strip().split(",")
                if category in expenses:
                    expenses[category].append((float(amount), date))

        print("\nExpenses:")
        for category in CATEGORIES:
            print(f"{category}:")
            if expenses[category]:
                for index, (amount, date) in enumerate(expenses[category], start=1):
                    print(f"  {index}. Amount: {amount} - Date: {date}")
            else:
                print("  No expenses recorded.")
    except Exception as e:
        print(f"Error viewing expenses: {e}")

# Calculate total expenses over a period
def calculate_total_expenses(start_date, end_date):
    try:
        total = 0
        category_totals = {category: 0 for category in CATEGORIES}
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

        with open(EXPENSES_FILE, "r") as file:
            next(file)  # Skip header
            for line in file:
                category, amount, date = line.strip().split(",")
                expense_date = datetime.strptime(date, "%Y-%m-%d")
                if start_date <= expense_date <= end_date:
                    total += float(amount)
                    if category in category_totals:
                        category_totals[category] += float(amount)
        
        print(f"Total expenses from {start_date.date()} to {end_date.date()}: {total:.2f}")
        print("By Category:")
        for category, amount in category_totals.items():
            print(f"{category}: {amount:.2f}")
    except Exception as e:
        print(f"Error calculating total expenses: {e}")

# Menu for user interaction
def menu():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses by Category")
        print("3. Calculate Total Expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter category: ")
            if category not in CATEGORIES:
                print("Invalid category. Please choose from the predefined categories.")
                continue
            amount = input("Enter amount: ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_expense(category, amount, date)
        elif choice == "2":
            view_expenses_by_category()
        elif choice == "3":
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            calculate_total_expenses(start_date, end_date)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    initialize_file()
    menu()
