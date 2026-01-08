from datetime import datetime

class User:
    def __init__(self, name, mobile, pin, balance):
        self.name = name
        self.mobile = mobile
        self.pin = pin
        self.balance = balance
        self.transactions = []
        self.daily_withdraw = 0
        self.daily_limit = 5000

    def check_balance(self):
        print("Current Balance:", self.balance)

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        else:
            self.balance += amount
            self.transactions.append(f"{datetime.now()} - Deposited {amount}")
            print("Deposit successful")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.balance:
            print("Insufficient balance")
        elif self.daily_withdraw + amount > self.daily_limit:
            print("Daily limit exceeded")
        else:
            self.balance -= amount
            self.daily_withdraw += amount
            self.transactions.append(f"{datetime.now()} - Withdrawn {amount}")
            print("Withdraw successful")

    def show_transactions(self):
        if len(self.transactions) == 0:
            print("No transactions found")
        else:
            for t in self.transactions:
                print(t)


#  USER DATA 


users = [
    User("Mahesh", 9922125846, 1234, 1000),
    User("Rohit", 9876543210, 4567, 2000) ]





#AUTHENTICATION FUNCTION -



def authenticate(users):
    attempts = 0

    while attempts < 3:
        try:
            mobile = int(input("Enter mobile number: "))
            pin = int(input("Enter pin: "))
        except ValueError:
            print("Please enter numbers only")
            continue

        for user in users:
             if user.mobile == mobile and user.pin == pin:
                   print("Login successful")
                   return user

        print("Wrong mobile number or pin")
        attempts += 1

    print("Login failed")
    return None


#  ATM MENU 



def atm_menu(user):
    while True:
        print("\nATM MENU")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Show Transactions")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user.check_balance()

        elif choice == "2":
            try:
                amount = int(input("Enter deposit amount: "))
                user.deposit(amount)
            except ValueError:
                print("Enter valid number")

        elif choice == "3":
            try:
                amount = int(input("Enter withdraw amount: "))
                user.withdraw(amount)
            except ValueError:
                print("Enter valid number")

        elif choice == "4":
            user.show_transactions()

        elif choice == "5":
            print("Thank you")
            break

        else:
            print("Invalid choice")
            
            

# MAIN PROGRAM



while True:
            print("\nWELCOME TO ATM")
            user = authenticate(users)

            if user:
                atm_menu(user)

            again = input("Login again yes or no: ")
            if again.lower() != "yes":
                    print("ATM closed")
                    break
