import os
from collections.abc import Callable

# Farm:

class Animal:

    def __init__(self, name: str, type: str = "Animal"):
        self.name: str = name
        self.type: str = type

    def __str__(self):
        return f"{self.type}(name={self.name})"
    
    def walk(self):
        print(f"{self.type} {self.name} is walking")
    
    def run(self):
        print(f"{self.type} {self.name} is running")

    def eat(self, food: str = "food"):
        print(f"{self.type} {self.name} is eating {food}")
    
    def sleep(self):
        print(f"{self.type} {self.name} is sleeping")


class Dog(Animal):

    def __init__(self, name: str, type: str = "Dog"):
        super().__init__(name, type)

    def bark(self):
        print("Wow")

    def chase(self, person: str = "neighbor"):
        print(f"{self.type} {self.name} is chasing {person}")

    def hunt(self, animal: Animal):
        print(f"{self.type} {self.name} is hunting {animal.name}")


class Fish(Animal):

    def __init__(self, name: str, type = "Fish"):
        super().__init__(name, type)

    def fry(self, time: str = "dinner"):
        print(f"{self.type} {self.name} is fried, ready for the {time}")


class GoldFish(Fish):

    def __init__(self, name: str, wishes: int, type: str = "GoldFish"):
        super().__init__(name, type)
        self.__wishes: int = wishes

    def wish(self, w: str):
        if self.__wishes > 0:
            self.__wishes -= 1
            print(f"{self.type} {self.name} received wish '{w}'")
        else:
            print(f"No wishes left for {self.type} {self.name}")



# Bank Application:

class Account:

    def __init__(self, account_number: int, name: str, balance: float):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account(account_number={self.account_number}, name='{self.name}', balance={self.balance})"

    def row(self):
        """Returns a comma-separated view of the acccount details, used for saving to file."""
        return f"{self.account_number}, {self.name}, {self.balance}"
    
    @classmethod
    def from_row(cls, text: str):
        """Takes string row and returns corresponding Account, or None."""
        commas = [i for i, c in enumerate(text) if c == ","] # position of separators
        if len(commas) < 2:
            return None
        account_number = text[:commas[0]].strip()
        name = text[commas[0]+1:commas[-1]].strip()
        if not name:
            name = "unknown"
        balance = text[commas[-1]+1:].strip()
        try:
            account_number = int(account_number)
            balance = float(balance)
        except:
            return None
        else:
            if account_number < 0 or balance != balance or balance == float('inf') or balance == -float('inf'):
                return None
        return cls(account_number, name, balance)

class Bank:

    def __init__(self, accounts: dict[int, Account] = None, filename: str = "accounts.txt"):
        self.accounts = accounts if accounts is not None else {}
        self.filename = filename
        if not os.path.exists(filename):
            with open(filename, "w"):
                pass
        else:
            self.load_from_file()

    def create_account(self, name: str, initial_deposit: float):
        """Creates an account."""
        account_number = self.generate_account_number()
        name = name if isinstance(name, str) and name else "unknown"
        balance = max(initial_deposit, 0.0) if isinstance(initial_deposit, float) else 0.0
        account = Account(account_number, name, balance)
        self.accounts[account_number] = account
        self.__add_to_file(account)

    def view_account(self, account_number: int = None):
        """Returns/displays the corresponding Account."""
        # I'm asked view_account(account_number) asking user-input. 
        # User-input becomes unnecessary if the account number is passed as an argument, though.
        # Thus, I let account_number default to None, and handle invalid argument with user-input.
        if self.is_valid(account_number): # takes the argument and returns the output
            return self.accounts[account_number] 
        else: # takes user-input and prints the output
            account_number = int(input("Enter the account number: ").strip()) # Raises ValueError if the input is not integer
            if self.is_valid(account_number):
                print(self.accounts[account_number].row())
            else:
                raise ValueError("The account number does not exist.") # Raising the error as asked

    def deposit(self, account_number: int = None, amount: float = None):
        """Deposits amount in the account."""
        if self.is_valid(account_number) and self.is_valid_amount(amount):
            self.accounts[account_number].balance += self.net_amount(amount)
        else:
            account_number, amount = self._input()
            self.accounts[account_number].balance += self.net_amount(amount)
        
    def withdraw(self, account_number: int = None, amount: float = None):
        """Withdraws amount from the account."""
        if self.afford(account_number, amount):
            self.accounts[account_number].balance -= self.debit(amount)
        else:
            account_number, amount = self._input(self.afford, "Not enough money!")
            self.accounts[account_number].balance -= self.debit(amount)

    def __add_to_file(self, account: Account):
        """Adds the account to the file."""
        with open(self.filename, "a") as file:
            file.write(account.row() + "\n")
    
    def save_to_file(self):
        """Saves the internal dictionary to the file."""
        with open(self.filename, "w") as file:
            file.write("\n".join(i.row() for i in self.accounts.values()))
    
    def load_from_file(self):
        """Loads the data from the file."""
        with open(self.filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                account = Account.from_row(line)
                if account is not None:
                    self.accounts[account.account_number] = account

    def _input(self, f: Callable[[int, float], bool] = lambda x, y: True, t = "Try again."):
        """Inputs the account number and amount."""
        while True:
            account_number = input("Enter the account number: ").strip()
            try:
                account_number = int(account_number)
            except:
                print("Account number must be an integer!")
                continue
            if self.is_valid(account_number):
                break
            else:
                print("Invalid account number.")
        while True:
            amount = input("Enter the amount: ").strip()
            try:
                amount = float(amount)
            except:
                print("Amount must be a number!")
                continue
            if self.is_valid_amount(amount):
                if not f(account_number, amount):
                    print(t)
                    continue
                break
            else:
                print("Invalid amount.")
        return (account_number, amount)

    def is_valid(self, account_number: int):
        """Checks if an account number is valid. That is, it should be a positive int, and it should exist in the dictionary."""
        return isinstance(account_number, int) and account_number >= 0 and account_number in self.accounts
    
    def is_valid_amount(self, amount: float):
        return isinstance(amount, float) and amount >= 0.0 and amount != float('inf') and amount == amount
    
    def afford(self, account_number: int, amount: float):
        return self.is_valid(account_number) and self.is_valid_amount(amount) and self.accounts[account_number].balance >= self.debit(amount)

    def generate_account_number(self):
        """Generate a unique account number."""
        if len(self.accounts) == 0:
            return 1
        else:
            return max(max(i for i in self.accounts) + 1, 1)

    def net_amount(self, deposit: float):
        """Takes the deposit and returns the net amount, taking the processing fee."""
        return deposit # assume our bank has no processing fee
    
    def debit(self, amount: float):
        """Returns the total amount leaving the account given the amount that should be withdrawn or transmissed. """
        return amount * 1.02 # assume 2% charge for withraw




