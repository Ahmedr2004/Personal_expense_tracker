# Expense Tracker

## Project Description
The Expense Tracker is a Python-based application designed to help users manage and analyze their personal expenses. It supports adding expenses, viewing them categorized by type, calculating total expenses for a specific time frame, and visualizing expense distribution using a pie chart.

## Features
- **Dynamic Categories:** Add expenses under predefined categories or create new ones dynamically.
- **View Expenses:** View expenses by category with serial numbers and dates.
- **Calculate Totals:** Calculate total expenses within a specified date range.
- **Data Visualization:** View a pie chart representation of expense distribution by category.
- **Persistent Storage:** Uses file handling (`expenses.txt`) to store data persistently.
- **Console Colors:** Enhanced visuals using the `colorama` library.

## File Structure
```
expense-tracker/
├── expense_tracker.py     # Main script for the Expense Tracker
├── expenses.txt           # File to store expenses (created automatically)
├── README.md              # Documentation
```

## How to Run the Project
1. Clone or download the repository:
   ```bash
   git clone https://github.com/yourusername/expense-tracker.git
   cd expense-tracker
   ```
2. Ensure you have Python installed (>= 3.6).
3. Install the required libraries:
   ```bash
   pip install colorama matplotlib
   ```
4. Run the script:
   ```bash
   python expense_tracker.py
   ```

## Instruction for Use
1. Upon running the script, a menu will appear:
   - **1. Add Expense:** Add an expense by entering category, amount, and date. If the category does not exist, it will be added dynamically.
   - **2. View Expenses by Category:** View all expenses categorized and listed with serial numbers. Displays a pie chart of the expense distribution.
   - **3. Calculate Total Expenses:** Enter a date range to calculate the total expenses and view category-wise totals. Also displays a pie chart for the specified range.
   - **4. Exit:** Exit the program.

## Installation
1. Download or clone the repository as mentioned above.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   If `requirements.txt` does not exist, use:
   ```bash
   pip install colorama matplotlib
   ```

## Additional Notes
- The `expenses.txt` file is created automatically if it doesn't exist.
- Categories with no recorded expenses are still shown in reports.
- Pie charts are generated only when expense data is available.

## Requirements
- Python 3.6+
- Libraries:
  - `colorama`
  - `matplotlib`

