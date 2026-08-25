class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise InvalidDepositAmount(amount)
        
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        
        if amount > self.balance:
            raise InsufficientFundsError(amount, self.balance)

        
        self.balance -= amount

    def get_balance(self):
        return self.balance

class InsufficientFundsError(ValueError):
    def __init__(self, needed, available):
        self.needed = needed
        self.available = available

class InvalidDepositAmount(ValueError):
    def __init__(self, amount):
        self.amount = amount

def main():
    carl_j = BankAccount("Carl Jinayon", 500)

    while True:
        print("1. Deposit" \
        "\n2. Withdraw" \
        "\n3. View balance" \
        "\n4. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError as e:
            print(e)
        else:
            if choice not in [1, 2, 3, 4]:
                print("Please enter a number from 1-4.")
                continue
            if choice == 1:
                try:
                    amount = float(input("Enter deposit amount: "))
                    carl_j.deposit(amount)
                except InvalidDepositAmount as e:
                    print(f"Invalid amount: {e.amount}. Must be greater than zero.")
                except ValueError as e:
                    print("Please enter a valid input.")
                else:
                    print(f"Deposit amount '{amount}' successful.")
            elif choice == 2:
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    carl_j.withdraw(amount)
                except InsufficientFundsError as e:
                    print(f"Failed to withdraw {e.needed}.")
                    print(f"Balance: {e.available}")
                except ValueError as e:
                    print(e)
                else:
                    print(f"Withdrawal of amount '{amount}' successful.")
            elif choice == 3:
                print(f"Balance: {carl_j.get_balance()}")
            elif choice == 4:
                print("Program terminated.")
                return

if __name__ == "__main__":
    main()