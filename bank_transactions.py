"""
Description: 
Author: Curtis Ainslie
Date: 2024-10-05
Usage: bank_transaction.py
"""
from random import randint

menu_options = ['D', 'W', 'Q']

current_balance = (randint(-1000, 10000))
current_balance = float(current_balance)

# Each line for the menu
menu_line_break = "****************************************"
menu_bank_name = "PIXELL RIVER FINANCIAL"
menu_deposit = "Deposit: D"
menu_withdraw = "Withdraw: W"
menu_quit = "Quit: Q"
invalid_line = "INVALID SELECTION"
insufficient_funds = "INSUFFICIENT FUNDS"
user_selection = ""

# Different menu pop ups
atm_selection_menu = [menu_line_break, menu_bank_name,
                    (f"Your current balance is: ${current_balance}"),
                    menu_deposit, menu_withdraw, menu_quit, 
                    menu_line_break]

invalid_selection = [menu_line_break, invalid_line, menu_line_break]

insufficient_funds_menu = [menu_line_break, insufficient_funds, 
                            menu_line_break]

# Prints out the menu
for menu_lines in atm_selection_menu:
    print("{:^40}".format(menu_lines))

user_selection = input("Enter your selection: ").upper()

# Selection options

# Deposit option
if user_selection == menu_options[0]:
    user_deposit = input("Enter amount of transaction: ")
    user_deposit = float(user_deposit)

    current_balance = current_balance + user_deposit
    
    view_current_balance = [menu_line_break, \
                        (f"Your current balance is: ${current_balance}"), \
                        menu_line_break]

    for view_current_balance_lines in view_current_balance:
        print("{:^40}".format(view_current_balance_lines))

# Withdraw option
elif user_selection == menu_options[1]:
    user_withdraw = input("Enter amount of transaction: ")
    user_withdraw = float(user_withdraw)

    current_balance = current_balance - user_withdraw

    if current_balance < 0:
        current_balance = current_balance + user_withdraw

        for insufficient_funds_lines in insufficient_funds_menu:
            print("{:^40}".format(insufficient_funds_lines))

    else:
        view_current_balance = [menu_line_break, \
                            (f"Your current balance is: ${current_balance}"), \
                            menu_line_break]

        for view_current_balance_lines in view_current_balance:
            print("{:^40}".format(view_current_balance_lines))

# Quit option
elif user_selection == menu_options[2]:
    view_current_balance = [menu_line_break, \
                            (f"Your current balance is: ${current_balance}"), \
                            menu_line_break]
    
    for view_current_balance_lines in view_current_balance:
        print("{:^40}".format(view_current_balance_lines))

# Invalid option
else:
    for invalid_selection_lines in invalid_selection:
        print("{:^40}".format(invalid_selection_lines))
