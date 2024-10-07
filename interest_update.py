"""
Description: 
Author: Curtis Ainslie
Date: 2024-10-05
Usage: interest_update.py

C-0001|1024.12
C-0002|49025.19
C-0003|5.29
C-0004|-599.33
C-0005|480.39
C-0006|2352.13
C-0007|54.93
C-0008|-509.39
C-0009|592.42
C-0010|9082.69
C-0011|392.33
C-0012|-90.33
C-0013|9932.33
C-0014|5902.5
C-0015|5902.55
C-0016|694.29
C-0017|49.33
C-0018|-55.33
C-0019|-0.33
C-0020|4.25
"""
import pprint

account_balances = {}

# with open("account_balances.txt", "r") as account_balances_file:
#     account_balances = DictReader(account_balances_file)
#     for row in account_balances:
#         print(row)

# account_balances_file.close()

# print(account_balances)

with open("account_balances.txt") as account_balances_file:
    for balance_line in account_balances_file:
        (key, value) = balance_line.strip().split('|')
        account_balances[key] = value

pprint.pp(account_balances)
