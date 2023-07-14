# Command Line Checkbook Application
# You will create a command line checkbook application that allows users to track their finances with a command line interface.
# Build a .py file that will be run from the command line.

# When run, the application should welcome the user, and prompt them for an action to take:

# view current balance
# add a debit (withdrawal)
# add a credit (deposit)
# exit
# The application should notify the user if the input is invalid and prompt for another choice.

#The application should persist between times that it is run.

#Example, if you run the application, add some credits, exit the application and run it again, you should still see the balance that you previously created. In order to do this, your application will need to store its data in a text file. Consider creating a file where each line in the file represents a single transaction.
#Utilize functions to call the balance, debit, credit, and exit
# [THIS IS NOT COMPLETE YET STILL NEED TO WORK ON JUST POSTED TO SHOW MY TRIED WORK]

import json
import os

working_file = "checkbook.json"
balance = 0

def welcome():
    print("Welcome to the Checkbook Application!")

def menu_display():
    print("Menu:")
    print("1. View current balance")
    print("2. Add a Debit (Withdrawal)")
    print("3. Add a Credit (Deposit)")
    print("4. Exit")



def view_balance():
    with open(working_file, "r") as file:
        data = json.load(file)
        balance = data[0]["balance"]
        print(f"Current balance: {balance}")

def add_debit():
    amount = float(input("Enter the amount to withdraw: "))
    with open(working_file, "r") as file:
        data = json.load(file)
        balance = float(data[0]["balance"])
        if amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            data[0]["balance"] = balance
            with open(working_file, "w") as file:
                json.dump(data, file, indent=4)
            print("Debit successfully recorded.")



def exit_program():
    print("Thank you for using the Checkbook Application!")


while True:
    welcome()
    menu_display()

    your_choice = input("Enter your choice (1-4): ")
    if your_choice == '1':
        view_balance()
    elif your_choice == '2':
        add_debit()
    elif your_choice == '3':
        add_credit()
    elif your_choice == '4':
        exit_program()
    else:
        print("Invalid input. Please try again.")
