"""
01_encapsulation_demo.py

This file introduces encapsulation in Python.
It demonstrates public, protected, and private attributes.

Main teaching goals:
1. Show the naming conventions:
   - public attribute: name
   - protected attribute: _name
   - private attribute: __name
2. Explain that Python does not enforce access modifiers like Java,
   but conventions and name mangling still matter.
3. Show why getters and setters can be useful.
"""


class BankAccount:
    """
    A simple BankAccount class for demonstrating encapsulation.
    """

    def __init__(self, owner, balance, pin_code):
        """
        Create a new bank account.
        in: owner name, starting balance, pin code
        out: BankAccount object
        """
        self.owner = owner                 # public
        self._balance = balance            # protected by convention
        self.__pin_code = pin_code         # private by name mangling

    def deposit(self, amount):
        """
        Add money to the account.
        in: positive number
        out: none
        """
        if amount > 0:
            self._balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount, pin_code):
        """
        Withdraw money only if pin code is correct and balance is enough.
        in: amount and pin code
        out: none
        """
        if pin_code != self.__pin_code:
            print("Incorrect pin code.")
            return

        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount > self._balance:
            print("Not enough balance.")
            return

        self._balance -= amount
        print(f"{amount} was withdrawn successfully.")

    def get_balance(self, pin_code):
        """
        Return the balance only if pin code is correct.
        in: pin code
        out: balance or None
        """
        if pin_code == self.__pin_code:
            return self._balance

        print("Incorrect pin code.")
        return None

    def set_pin_code(self, old_pin, new_pin):
        """
        Change the pin code if the old one is correct and the new one is valid.
        in: old pin, new pin
        out: none
        """
        if old_pin != self.__pin_code:
            print("Incorrect current pin code.")
            return

        if len(str(new_pin)) != 4:
            print("New pin code must be exactly 4 digits.")
            return

        self.__pin_code = new_pin
        print("Pin code updated successfully.")

    def show_account_info(self):
        """
        Print general account information.
        in: none
        out: none
        """
        print(f"Owner: {self.owner}")
        print(f"Protected balance attribute: {self._balance}")
        print("Private pin code attribute cannot be accessed directly in a normal way.")


def main():
    """
    Run examples for the lesson.
    in: none
    out: none
    """
    account = BankAccount("Michael", 1000, 1234)

    print("=== PUBLIC ATTRIBUTE ===")
    print(account.owner)
    account.owner = "David"
    print(account.owner)

    print("\n=== PROTECTED ATTRIBUTE ===")
    print(account._balance)
    print("We CAN access it, but we SHOULD treat it as internal.")

    print("\n=== PRIVATE ATTRIBUTE ===")
    print("Trying account.__pin_code directly would fail.")
    print("Python changes its internal name using name mangling.")

    print("\n=== METHODS ===")
    account.show_account_info()

    print("\n=== DEPOSIT ===")
    account.deposit(300)
    print(account.get_balance(1234))

    print("\n=== WITHDRAW WITH WRONG PIN ===")
    account.withdraw(100, 1111)

    print("\n=== WITHDRAW WITH CORRECT PIN ===")
    account.withdraw(100, 1234)
    print(account.get_balance(1234))

    print("\n=== CHANGE PIN ===")
    account.set_pin_code(1234, 5678)
    print(account.get_balance(5678))

    print("\n=== NAME MANGLING DEMO ===")
    print("This works, but should not be used in real design:")
    print(account._BankAccount__pin_code)


if __name__ == "__main__":
    main()