# Create a class BankAccount with an attribute balance. Implement a static
# method validate_amount(amount) to check if an amount is positive and raise an
# exception otherwise. Create two methods in this class, one to withdraw money
# and another one to deposit money into the account. The withdraw method will
# not allow withdrawing more money than available: it will raise an exception
# and not change the balance. The two instance methods should use the static
# method to validate that the amount is positive.
class InvalidAmount(Exception):
    pass


class BalanceExceeded(Exception):
    pass


class BankAccount:
    def __init__(self):
        self.balance = 0

    @staticmethod
    def validate_amount(amount):
        if amount <= 0:
            raise InvalidAmount("Amount should be greater than 0.")

    def withdraw(self, amount):
        self.validate_amount(amount)
        if amount > self.balance:
            raise BalanceExceeded("Insufficient funds.")
        self.balance -= amount

    def deposit(self, amount):
        self.validate_amount(amount)
        self.balance += amount


# Create a class Temperature with an instance attribute celsius. Add a static
# method celsius_to_fahrenheit(celsius) to convert Celsius to Fahrenheit and a
# class method from_fahrenheit(cls, fahrenheit) to create an instance from a
# Fahrenheit value. Use the two methods.

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return int(celsius * 9/5 + 32)

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return int((fahrenheit - 32) * 5 / 9)

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        celsius = cls.fahrenheit_to_celsius(fahrenheit)
        return cls(celsius)


if __name__ == "__main__":
    bank_acc = BankAccount()

    bank_acc.deposit(100)
    print("Balance after depositing 100:", bank_acc.balance)

    bank_acc.withdraw(60)
    print("Balance after withdrawing 60:", bank_acc.balance)

    try:
        bank_acc.deposit(-20)
    except Exception as ex:
        print(ex)

    try:
        bank_acc.withdraw(70)
    except Exception as ex:
        print(ex)

    print("Balance after failed transactions:", bank_acc.balance)

    temp = Temperature(31)

    temp1 = Temperature.from_fahrenheit(68)
    print("68 Fahrenheit in Celsius:", temp1.celsius)

    fahrenheit_temp = Temperature.celsius_to_fahrenheit(temp.celsius)
    print("31 Celsius in Fahrenheit:", fahrenheit_temp)
