"""
Description: 
Author: Curtis Ainslie
Date: 2024-10-05
Usage: bank_transaction.py
"""
from random import randint

menu_options = ('D', 'W', 'Q')

current_balance = (randint(-1000, 10000))
current_balance = float(current_balance)

menu_line_break: str = "****************************************"
menu_line_1: str = "PIXELL RIVER FINANCIAL"
menu_line_2: str = f"Your current balance is: ${current_balance}"
menu_line_3: str = "Deposit: D"
menu_line_4: str = "Withdraw: W"
menu_line_5: str = "Quit: Q"

atm_menu = (menu_line_break, menu_line_1, menu_line_2, menu_line_3, \
              menu_line_4, menu_line_5, menu_line_break)

for menu_lines in atm_menu:
    print("{:^40}".format(menu_lines))
