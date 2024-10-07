"""
Description: This script will calculate the interest rate of each balance and copy it into a new file
Author: Curtis Ainslie
Date: 2024-10-05
Usage: interest_update.py
"""
import pprint
import csv

accounts_and_balances = {}

with open("account_balances.txt") as account_balances_file:
    for balance_line in account_balances_file:
        (account_number, account_balance) = balance_line.strip().split('|')
        accounts_and_balances[account_number] = account_balance
account_balance = float(account_balance)

pprint.pp(accounts_and_balances)



for account_key, account_value in accounts_and_balances.items():
    account_value = float(account_value)
    
    if account_value >= 5000:
        interest_rate = 0.05
    elif account_value >= 1000:
        interest_rate = 0.025
    elif account_value < 0:
        interest_rate = 0.1
    elif account_value < 1000:
        interest_rate = 0.01

    new_account_value = account_value + ((account_value * interest_rate) / 12)

    accounts_and_balances[account_key] = new_account_value

pprint.pp(accounts_and_balances)

updated_accounts_and_balances = "updated_balance_CA.csv"

file_names = ["Account", "Balance"]

with open("updated_balance_CA.csv", 'w', newline='') as updated_file:
    writer = csv.DictWriter(updated_file, fieldnames=file_names)

    writer.writeheader()

    for account_key, account_value in accounts_and_balances.items():
        writer.writerow({"Account": account_key, "Balance": account_value})

with open("updated_balance_CA.csv", 'r') as updated_file:
    reader = csv.DictReader(updated_file)
    for accounts_and_balances_row in reader:
        print(accounts_and_balances_row["Account"], \
              accounts_and_balances_row["Balance"])
