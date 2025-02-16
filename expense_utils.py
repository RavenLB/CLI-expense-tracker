import csv
import os.path
from datetime import datetime
from tabulate import tabulate

EXPENSE_FILE = "expenses.csv"

def make_expense_file():
    if not os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, "w", newline="")as file:
            writer=csv.writer(file)
            writer.writerow(["ID", "Description", "Amount", 'Date'])

def load_expenses():
    make_expense_file()
    with open(EXPENSE_FILE, "r", newline="")as file:
        reader=csv.reader(file)
        return list(reader)[1:]

def save_expenses(expenses):
    with open(EXPENSE_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID","Description", "Amount"])
        writer.writerows(expenses)

def get_next_id():
    expenses = load_expenses()
    if not expenses:
        return 1
    return int(expenses[-1][0]) + 1

def add_expense(description,amount,date=None):
    make_expense_file()
    id=get_next_id()
    if not date:
        date=datetime.now().strftime('%Y-%m-%d')
    with open(EXPENSE_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([id, description, amount, date])
    print (f"Added expense: {id}: {description} for {amount} $ on {date}.")

def update_expense(id):
    expenses = load_expenses()
    index = get_index(id)

    if index == -1:
        print("Expense ID not found!")
        return

    expense = expenses[index]
    print(f"Current details: {expense[1]}, Amount: {expense[2]}")


def list_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded.")
    else:
        headers = ["ID", "Description", "Amount", "Date"]
        # Use tabulate to format the expenses as a table
        print(tabulate(expenses, headers=headers, tablefmt="pretty"))

def get_index(id):
    expenses = load_expenses()
    for index, expense in enumerate(expenses):
        if expense[0] == str(id):
            return index
    return -1

def delete_expense(id):
    expenses = load_expenses()
    index = get_index(id)
    if index == -1:
        print("Expense ID not found!")
        return
    removed = expenses.pop(index)
    save_expenses(expenses)
    print(f"Deleted expense: {removed[1]} ({removed[2]}$)")
