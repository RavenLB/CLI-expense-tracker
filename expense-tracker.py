#!/usr/bin/env python3

import argparse
from expense_utils import (
    add_expense,
    list_expenses,
    delete_expense,
    update_expense
)
from summary_utils import summary, monthly_summary, daily_summary


def main():
    parser = argparse.ArgumentParser(description="Expense Tracker")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description", required=True, help="Description of the expense")
    add_parser.add_argument("--amount", type=float, required=True, help="Amount of the expense")
    add_parser.add_argument("--date", help="Date of the expense (YYYY-MM-DD)")

    summary_parser = subparsers.add_parser("summary", help="Show total expenses")
    summary_subparsers = summary_parser.add_subparsers(dest="type")

    subparsers.add_parser("list", help="List all expenses")

    delete_parser = subparsers.add_parser("delete", help="Delete an expense by ID")
    delete_parser.add_argument("--id", type=int, help="ID of the expense to delete")

    update_parser = subparsers.add_parser("update", help="Update an existing expense")
    update_parser.add_argument("--id", type=int, help="ID of the expense to update")
    update_parser.add_argument("--description", help="Updated description of the expense")
    update_parser.add_argument("--amount", type=float, help="Updated amount of the expense")
    update_parser.add_argument("--date", nargs="?", help="Updated date of the expense (YYYY-MM-DD)")

    monthly_parser = summary_subparsers.add_parser("monthly", help="Show monthly summary")
    monthly_parser.add_argument("--month", type=int, help="Month to summarize (1-12)")
    monthly_parser.add_argument("year", type=int, help="Year to summarize")

    daily_parser = summary_subparsers.add_parser("daily", help="Show daily summary")
    daily_parser.add_argument("--day", type=int, help="Day to summarize")
    daily_parser.add_argument("month", type=int, help="Month to summarize (1-12)")
    daily_parser.add_argument("year", type=int, help="Year to summarize")

    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.description, args.amount, args.date)
    elif args.command == "list":
        list_expenses()
    elif args.command == "delete":
        delete_expense(args.id)
    elif args.command == "update":
        update_expense(args.id, args.description, args.amount, args.date)
    elif args.command == "summary":
        if args.type == "monthly":
            monthly_summary(args.month, args.year)
        elif args.type == "daily":
            daily_summary(args.day, args.month, args.year)
        else:
            # If no type or invalid type, show general summary
            summary()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
