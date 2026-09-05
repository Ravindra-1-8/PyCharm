# Without Encapsulation.

class Bank:
    def __init__(self):
        self.balance = 1000

    def show_balance(self):
        print(self.balance)

    def deposit(self,amount):
        self.balance += amount

b = Bank()
b.balance = 0
# When we changed "balance" properties from outside it has changed when we don't used encapsulation.
b.show_balance()

b.deposit(900)
b.show_balance()

# With Encapsulation: Protecting a data inside a class.
# It allows access to data only through class methods, not directly.
# It helps keeping data safe, controlled and secure.

class Reserve:
    def __init__(self):  # Encapsulation is used & it is safe and secure.
        self.__remaining = 1000

    def show_remaining(self):
        print(self.__remaining)

    def deposit(self,amount):
        self.__remaining += amount

    def withdraw(self,amount):
        self.__remaining -= amount

a = Reserve()
a.__remaining = 0
a.show_remaining()

a.deposit(5)
a.show_remaining()

a.withdraw(500)
a.show_remaining()