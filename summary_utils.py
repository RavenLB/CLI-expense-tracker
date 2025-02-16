from expense_utils import load_expenses, list_expenses


def summary():
    expenses = load_expenses()
    amounts = [float(expense[2]) for expense in expenses]
    summary = sum(amounts)
    print (f"Your total expenses are {summary} $.")

def monthly_summary(month,year):
    expenses = list_expenses()
    total = 0.0
    print(f"Summary of expenses for {month}/{year}.")

    for expense in expenses:
        date = expenses[3]
        date_month, date_year = date.split("-")[1], date.split("-")[2]
        if date_month == str(month).zfill(2) and date_year == str(year):
            total += float(expense[2])

    print(f"Your spendings for {month}/{year} are {total} $.")

def daily_summary(day, month, year):
    expenses = list_expenses()
    total = 0.0
    print(f"Daily expenses for{day}/{month}/{year}")

    for expense in expenses:
        date = expenses[3]
        date_day, date_month, date_year = date.split("-")[0], date.split("-")[1], date.split("-")[2]
        if date_day == str(day).zfill(2) and date_month == str(month).zfill(2) and date_year == str(year):
            total += expenses[2]
    print(f"Your expenses on {day}/{month}/{year} were {total} $.")