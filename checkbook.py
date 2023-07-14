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


def add_credit():
    amount = float(input("Enter the amount to deposit: "))
    with open(working_file, "r") as file:
        data = json.load(file)
        balance = float(data[0]["balance"])
        balance += amount
        data[0]["balance"] = balance
        with open(working_file, "w") as file:
            json.dump(data, file, indent=4)
        print("Credit successfully recorded.")

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
