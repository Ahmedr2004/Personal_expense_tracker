import os
from datetime import datetime
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

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
        print(Fore.GREEN + "Expense added successfully.\n(Expense recorded in expenses.txt)")
    except Exception as e:
        print(Fore.RED + f"Error adding expense: {e}")

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

        print(Fore.CYAN + "\nExpenses:")
        for category in CATEGORIES:
            print(Fore.YELLOW + f"{category}:")
            if expenses[category]:
                for index, (amount, date) in enumerate(expenses[category], start=1):
                    print(Fore.WHITE + f"  {index}. Amount: {amount} - Date: {date}")
            else:
                print(Fore.LIGHTBLACK_EX + "  No expenses recorded.")
    except Exception as e:
        print(Fore.RED + f"Error viewing expenses: {e}")

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
        
        print(Fore.CYAN + f"Total expenses from {start_date.date()} to {end_date.date()}: {total:.2f}")
        print(Fore.CYAN + "By Category:")
        for category, amount in category_totals.items():
            print(Fore.YELLOW + f"{category}: {amount:.2f}")
    except Exception as e:
        print(Fore.RED + f"Error calculating total expenses: {e}")

# Menu for user interaction
def menu():
    while True:
        print(Fore.CYAN + "\nExpense Tracker")
        print(Fore.GREEN + "1. Add Expense")
        print(Fore.GREEN + "2. View Expenses by Category")
        print(Fore.GREEN + "3. Calculate Total Expenses")
        print(Fore.RED + "4. Exit")

        choice = input(Fore.CYAN + "Enter your choice: ")

        if choice == "1":
            category = input(Fore.CYAN + "Enter category: ")
            if category not in CATEGORIES:
                print(Fore.RED + "Invalid category. Please choose from the predefined categories.")
                continue
            amount = input(Fore.CYAN + "Enter amount: ")
            date = input(Fore.CYAN + "Enter date (YYYY-MM-DD): ")
            add_expense(category, amount, date)
        elif choice == "2":
            view_expenses_by_category()
        elif choice == "3":
            start_date = input(Fore.CYAN + "Enter start date (YYYY-MM-DD): ")
            end_date = input(Fore.CYAN + "Enter end date (YYYY-MM-DD): ")
            calculate_total_expenses(start_date, end_date)
        elif choice == "4":
            print(Fore.YELLOW + "Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")

if __name__ == "__main__":
    initialize_file()
    menu()
