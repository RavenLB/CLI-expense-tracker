import csv
import os.path
from datetime import datetime
from tabulate import tabulate

EXPENSE_FILE = "expenses.csv"


def make_expense_file():
    """
    Creates the expense file if it does not exist, initializing it with column headers.
    """
    if not os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Description", "Amount", 'Date'])


def load_expenses():
    """
    Loads the expenses from the CSV file, skipping the header row.
    Returns a list of expenses.
    """
    make_expense_file()
    with open(EXPENSE_FILE, "r", newline="") as file:
        reader = csv.reader(file)
        return list(reader)[1:]


def save_expenses(expenses):
    """
    Saves the given list of expenses to the CSV file, overwriting the current contents.

    Args:
        expenses (list): List of expenses, each being a list containing ID, Description, and Amount.
    """
    with open(EXPENSE_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Description", "Amount"])
        writer.writerows(expenses)


def get_next_id():
    """
    Returns the next available ID for a new expense.
    If no expenses exist, it returns 1.
    """
    expenses = load_expenses()
    if not expenses:
        return 1
    return int(expenses[-1][0]) + 1


def add_expense(description, amount, date=None):
    """
    Adds a new expense to the CSV file.

    Args:
        description (str): The description of the expense.
        amount (float): The amount of the expense.
        date (str, optional): The date of the expense. If None, the current date is used.
    """
    make_expense_file()
    id = get_next_id()
    if not date:
        date = datetime.now().strftime('%Y-%m-%d')
    with open(EXPENSE_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([id, description, amount, date])
    print(f"Added expense: {id}: {description} for {amount} $ on {date}.")


def update_expense(id):
    """
    Updates the details of an existing expense.

    Args:
        id (int): The ID of the expense to update.
    """
    expenses = load_expenses()
    index = get_index(id)

    if index == -1:
        print("Expense ID not found!")
        return

    expense = expenses[index]
    print(f"Current details: {expense[1]}, Amount: {expense[2]}")


def list_expenses():
    """
    Lists all the expenses in a formatted table.
    If no expenses exist, prints a message indicating no expenses are recorded.
    """
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded.")
    else:
        headers = ["ID", "Description", "Amount", "Date"]
        # Use tabulate to format the expenses as a table
        print(tabulate(expenses, headers=headers, tablefmt="pretty"))


def get_index(id):
    """
    Retrieves the index of the expense with the given ID.

    Args:
        id (int): The ID of the expense.

    Returns:
        int: The index of the expense if found, otherwise -1.
    """
    expenses = load_expenses()
    for index, expense in enumerate(expenses):
        if expense[0] == str(id):
            return index
    return -1


def delete_expense(id):
    """
    Deletes the expense with the given ID from the CSV file.

    Args:
        id (int): The ID of the expense to delete.
    """
    expenses = load_expenses()
    index = get_index(id)
    if index == -1:
        print("Expense ID not found!")
        return
    removed = expenses.pop(index)
    save_expenses(expenses)
    print(f"Deleted expense: {removed[1]} ({removed[2]}$)")