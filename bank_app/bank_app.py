class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            print(f"Current balance: ${self.balance}")
            return self.balance
        self.balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.balance}")
        return self.balance

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied: ${interest:.2f}. New balance: ${self.balance:.2f}")

class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0, overdraft_limit=100):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Overdraft limit exceeded.")
            return self.balance
        self.balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.balance}")
        return self.balance


def main():
    print("Welcome to ANH Bank!")
    name = input("Enter your name: ")

    account_type = input("Select account type (savings/checking): ").strip().lower()

    if account_type == "savings":
        account = SavingsAccount(name, balance=100)
    elif account_type == "checking":
        account = CheckingAccount(name, balance=100)
    else:
        print("Invalid account type.")
        return

    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        if isinstance(account, SavingsAccount):
            print("4. Apply Interest")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount: "))
            account.withdraw(amount)
        elif choice == "3":
            print(f"Current balance: ${account.get_balance()}")
        elif choice == "4" and isinstance(account, SavingsAccount):
            account.apply_interest()
        elif choice == "0":
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()