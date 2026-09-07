# Improve the BankAccount from the previous exercise:
#
# Make the argument balance of the __init__ an optional argument with default
# value 0
# Override the dunder method __str__ so that we can print bank objects more
# easily. Make it tell us the bank name and balance. Make __repr__ do the same
# thing.
# Make balance an _ attribute to suggest it is protected. Make balance a
# property in order to return it. Update deposit and withdraw to use _balance
# Create a class Employee with three instance attributes:
#
# name
# bank_account (it should be a BankAccount object; pass an already created
# BankAccount instance at Employee initialisation)
# salary (default 0)
# Write a method raise_salary that receives a parameter percent that should be
# one of the following values: 5, 10, 20. Raise a ValueError if another value is
# received by this method. The raise_salary method should raise the salary with
# 5%, 10% or 20%.
#
# Create a method receive_salary that will deposit in the employee's bank
# account an amount equal to its salary.
#
# Use a property for salary management. Salary should be set only on
# initialisation; you shouldn't be able to set the salary from outside the
# class.
#
# Make bank_account protected by one _ and add a property net_worth that returns
# the balance from the employee bank_account. (should be called w/o paranthesis)
#
# Add a method spend that substracts a given amount from the employee's
# bank_account
#
# Create an Employee instance and call raise_salary, receive_salary and spend on
# it. Print its net_worth afterwards.

class InsufficientFundsException(Exception):
    pass


class BankAccount:
    def __init__(self, bank_name, balance=0):
        self.bank_name = bank_name
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientFundsException('insufficient funds')
        self._balance -= amount

    def __str__(self):
        return f"Bank: {self.bank_name} | Balance: {self._balance}"

    def __repr__(self):
        return self.__str__()
        # return str(self)


class Employee:
    ACCEPTED_RAISE_VALUES = (5, 10, 20)

    def __init__(self, name: str, bank_account: BankAccount, salary: int = 0):
        self.name = name
        self._bank_account = bank_account
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    def raise_salary(self, percent: int):
        """method accepts one of these values (5, 10, 20) as percent"""
        if percent not in self.ACCEPTED_RAISE_VALUES:
            raise ValueError(f'Invalid raise value: {percent}%')
        self._salary += (percent / 100) * self._salary

    def receive_salary(self):
        self._bank_account.deposit(self._salary)

    @property
    def net_worth(self):
        return self._bank_account.balance

    def spend(self, amount):
        self._bank_account.withdraw(amount)


if __name__ == "__main__":
    bank_acc = BankAccount('ING', 1000)  # create BankAccount instance
    full_name = "Ion Georgescu"  # create str instance

    employee = Employee(full_name, bank_acc, 200)
    print("Before receiving salary", employee.net_worth)

    employee.raise_salary(10)
    employee.receive_salary()
    print("After raise and receiving salary", employee.net_worth)
    employee.spend(100)
    print("After spending 100", employee.net_worth)
