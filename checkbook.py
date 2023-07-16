import json
import os 

# Load data from the JSON file and initialize variables
def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Function to view the current balance
def view_balance(data):
    total_balance = sum(float(item['balance'].replace(',', '').replace('$', '')) for item in data)
    return total_balance

# Function to add a debit (withdrawal)
def add_debit(data, account_number, amount):
    for item in data:
        if item['account_number'] == account_number:
            balance = float(item['balance'].replace(',', '').replace('$', ''))
            if amount <= balance:
                item['balance'] = "${:,.2f}".format(balance - amount)
                print(f"Withdrawal of ${amount:.2f} from account {account_number} successful.")
                return True
            else:
                print("Insufficient funds.")
                return False
    print(f"Account {account_number} not found.")
    return False

# Function to add a credit (deposit)
def add_credit(data, account_number, amount):
    for item in data:
        if item['account_number'] == account_number:
            balance = float(item['balance'].replace(',', '').replace('$', ''))
            item['balance'] = "${:,.2f}".format(balance + amount)
            print(f"Deposit of ${amount:.2f} to account {account_number} successful.")
            return True
    print(f"Account {account_number} not found.")
    return False

def main():
    file_path = "data.json"
    data = load_data(file_path)

    while True:
        print("\nWelcome to the Command Line Checkbook Application!")
        print("1. View Current Balance")
        print("2. Add a Debit (Withdrawal)")
        print("3. Add a Credit (Deposit)")
        print("4. Exit")

        choice = input("Please enter the number of the action you want to take: ")

        if choice == "1":
            balance = view_balance(data)
            print(f"Your current balance is ${balance:.2f}")

        elif choice == "2":
            account_number = input("Enter the account number: ")
            amount = float(input("Enter the amount to withdraw: "))
            add_debit(data, account_number, amount)

        elif choice == "3":
            account_number = input("Enter the account number: ")
            amount = float(input("Enter the amount to deposit: "))
            add_credit(data, account_number, amount)

        elif choice == "4":
            save_data(file_path, data)
            print("Thank you for using the Checkbook Application. Goodbye!")
            break

        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
