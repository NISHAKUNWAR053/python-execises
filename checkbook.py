import os
import json

def get_data_file_path():
    return "checkbook_data.json"

def load_data():
    data_file_path = get_data_file_path()
    if os.path.exists(data_file_path):
        with open(data_file_path, "r") as file:
            data = json.load(file)
    else:
        data = {
            "name": "Nisha",
            "balance": 50000.0,
            "debit": 0.0,
            "credit": 0.0
        }
    return data

def save_data(data):
    data_file_path = get_data_file_path()
    with open(data_file_path, "w") as file:
        json.dump(data, file)

def print_options():
    print("Input your choices 1 through 4")
    print("1) view current balance")
    print("2) record a debit (withdraw)")
    print("3) record a credit (deposit)")
    print("4) exit")
    print()

def withdraw(debit):
    data["debit"] = debit
    data["balance"] -= debit
    return data["balance"]

def deposit(credit):
    data["credit"] = credit
    data["balance"] += credit
    return data["balance"]

def balance():
    return data["balance"]

data = load_data()

print(" ~~~ Welcome to your terminal checkbook! ~~~", data["name"])
while True:
    print_options()
    inp = int(input("Your Choice is: "))

    if inp == 1:
        print("Your balance is:", balance())
    elif inp == 2:
        dbt_amt = float(input("Amount to withdraw: "))
        print("Your balance is:", withdraw(dbt_amt))
    elif inp == 3:
        crdt_amt = float(input("Amount to deposit: "))
        print("Your balance is:", deposit(crdt_amt))
    elif inp == 4:
        print("Thanks, have a great day!")
        save_data(data)  # Save data before exiting
        break
    else:
        print("Please enter a valid input (1, 2, 3, or 4).")
