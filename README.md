Expense Tracker

Project Description

The Expense Tracker is a Python-based console application designed to help users manage and categorize their personal expenses effectively. The program allows users to add expenses, view categorized summaries, and calculate total expenditures over a specified period. It uses file handling to persistently store expense data and utilizes colorama for enhanced console visuals.

Features

Add Expense: Record an expense by specifying the category, amount, and date.

View Expenses by Category: View a detailed breakdown of expenses organized by predefined categories.

Calculate Total Expenses: Calculate and display the total expenses within a specified date range, along with category-wise totals.

Predefined Categories: Includes categories such as Food, Travel, Entertainment, Utilities, and Others.

File Persistence: Stores expense data persistently in expenses.txt.

Enhanced Console Visuals: Uses the colorama library for color-coded output, improving readability.

How to Run the Project

Ensure you have Python installed on your system.

Clone or download the project files to your local machine.

Open a terminal or command prompt in the project directory.

Run the program using the command:

python expense_tracker.py

Follow the on-screen menu to interact with the Expense Tracker.

Installation Instructions

Install Python (if not already installed):

Download Python and follow the installation instructions for your operating system.

Install required dependencies:

Open a terminal and run the following command to install colorama:

pip install colorama

(Optional) Create an empty expenses.txt file in the same directory as the script if it doesn't already exist. The program will initialize it automatically if missing.

Usage

Add an Expense:

Choose option 1 from the menu.

Enter the category, amount, and date of the expense.

View Expenses by Category:

Choose option 2 to see a categorized summary of all recorded expenses.

Calculate Total Expenses:

Choose option 3 and specify the start and end dates to calculate total and category-wise expenses within that range.

Exit:

Choose option 4 to exit the program.

File Structure

expense_tracker.py: Main script containing the application logic.

expenses.txt: File used to store expense records in CSV format.