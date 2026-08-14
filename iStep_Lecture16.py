# ამოცანა 1

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says: Woof!")

    def info(self):
        print(f"Name: {self.name} & Age: {self.age}")


# dog1 = Dog("Bombora", 3)
# dog1.bark()
# dog1.info()


# ამოცანა 2

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def is_square(self):
        return self.width == self.height


# Rectangle1 = Rectangle(5, 3)
# print(Rectangle1.area())
# print(Rectangle1.perimeter())
# print(Rectangle1.is_square())


# ამოცანა 3

class BankAccount:
    bank_name = "Step Bank"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds!")

    def show_balance(self):
        print(f"Bank name: {self.bank_name}; Owner name: {self.owner}; Balance: {self.balance}")


# bank_account1 = BankAccount("Albert", 5000)
#
# bank_account1.deposit(500)
# print(bank_account1.balance)
#
# bank_account1.withdraw(9000)
# print(bank_account1.balance)
#
# bank_account1.show_balance()
