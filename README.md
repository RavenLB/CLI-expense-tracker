# Expense Tracker CLI

## Description
The Expense Tracker CLI is a Python-based command-line tool designed to help users track and manage their expenses. It allows users to add, view, update, delete, and summarize expenses. The tool stores expenses in a CSV file and provides functionality to view total expenses, monthly summaries, and daily summaries.

This project aims to simplify expense tracking and make it easy to monitor spending over time.

It is inspired by the [Expense Tracker](https://roadmap.sh/projects/expense-tracker) project featured in the [Backend Roadmap](https://roadmap.sh/backend) from [roadmap.sh](https://roadmap.sh/).

## Features
- **Add Expenses**: Easily add new expenses with details such as description, amount, and date.
- **Update Expenses**: Modify the details of an existing expense.
- **Delete Expenses**: Delete an expense based on its ID.
- **View Expenses**: Display a list of all recorded expenses.
- **Generate Reports**: Create summary reports of expenses, including total, monthly, and daily summaries.

## Prerequisites
- Python 3.x
- `tabulate` library (used for pretty table formatting)

## Installation
1. **Clone the Repository**:
   ```sh
   git clone https://
   cd expense-tracker-cli
   
2. **Create and Activate a Virtual Environment**:
    ```sh
    python -m venv venv
    
    # On Windows:
    .\venv\Scripts\activate
    
    # On macOS and Linux:
    source venv/bin/activate

3. **Install Dependencies**:
    ```sh
   pip install -r requirements.txt
   
## Usage
1. **Run the application**:
   ```sh
    python expense-tracker.py -h # Show help
   
2. **Example usage**:
    ```sh
   python expense-tracker-cli.py add --description "Lunch" --amount 20 # Add an expense
    python expense-tracker-cli.py add --description "Dinner" --amount 10 # Add another expense
    python expense-tracker-cli.py update --id 1 --description "Updated Lunch" --amount 25 # Update an existing expense
    python expense-tracker-cli.py list # List all expenses
    python expense-tracker-cli.py summary # Show summary of total expenses
    python expense-tracker-cli.py summary --month 8 --year 2025 # Show summary of expenses for specific month
    python expense-tracker-cli.py summary --day 15 --month 2 --year 2025 # Show summary of expenses for specific day
    python expense-tracker-cli.py delete --id 1 # Delete an expense by ID
  
   