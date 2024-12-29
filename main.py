import os
from datetime import datetime
from colorama import Fore, Style, init
import matplotlib.pyplot as plt

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
        if category not in CATEGORIES:
            CATEGORIES.append(category)  # Add new category dynamically
        with open(EXPENSES_FILE, "a") as file:
            file.write(f"{category},{amount},{date}\n")
        print(Fore.GREEN + "Expense added successfully.")
    except Exception as e:
        print(Fore.RED + f"Error adding expense: {e}")

# View expenses by category
def view_expenses_by_category():
    try:
        # Ensure the categories dictionary is populated
        expenses = {}
        for category in CATEGORIES:
            expenses[category] = []
        
        with open(EXPENSES_FILE, "r") as file:
            next(file)  # Skip header
            for line in file:
                category, amount, date = line.strip().split(",")
                if category not in expenses:
                    expenses[category] = []
                expenses[category].append((float(amount), date))

        print(Fore.CYAN + "\nExpenses:")
        category_totals = {}
        for category in expenses:
            category_totals[category] = 0
            print(Fore.YELLOW + f"{category}:")
            if expenses[category]:
                for index, (amount, date) in enumerate(expenses[category], start=1):
                    print(Fore.WHITE + f"  {index}. Amount: {amount} - Date: {date}")
                    category_totals[category] += amount
            else:
                print(Fore.LIGHTBLACK_EX + "  No expenses recorded.")
        
        # Generate a pie chart
        generate_pie_chart(category_totals)

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
                    if category not in category_totals:
                        category_totals[category] = 0
                    category_totals[category] += float(amount)
        
        print(Fore.CYAN + f"Total expenses from {start_date.date()} to {end_date.date()}: {total:.2f}")
        print(Fore.CYAN + "By Category:")
        for category, amount in category_totals.items():
            print(Fore.YELLOW + f"{category}: {amount:.2f}")

        # Generate a pie chart
        generate_pie_chart(category_totals)
    except Exception as e:
        print(Fore.RED + f"Error calculating total expenses: {e}")

# Generate a pie chart of expenses
def generate_pie_chart(category_totals):
    labels = []
    sizes = []

    for category, amount in category_totals.items():
        if amount > 0:
            labels.append(category)
            sizes.append(amount)

    if sizes:
        plt.figure(figsize=(8, 6))
        plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140, colors=["#ff9999","#66b3ff","#99ff99","#ffcc99","#c2c2f0"])
        plt.title("Expense Distribution by Category")
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()
    else:
        print(Fore.LIGHTBLACK_EX + "No data available to generate a pie chart.")

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
