# დავალება 1

class Profile:
    def __init__(self, password):
        self.__password = password

    def check_password(self, password):
        return self.__password == password

    def change_password(self, old_password, new_password):
        if self.__password == old_password:
            self.__password = new_password


# profile1 = Profile("11111")
# print(profile1.check_password("11110"))
# profile1.change_password("11111", "00000")
# print(profile1.check_password("00000"))


# დავალება 2

class Product:
    def __init__(self, price):
        self.__price = price

    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            print("ფასი არ უნდა იყოს უარყოფითი")

    def get_price(self):
        return self.__price


# product1 = Product(10)
# product1.set_price(-50)
# print(product1.get_price())

# დავალება 3

class CreditCardPayment:
    def pay(self, amount):
        print(f"{amount} ლარი გადახდილია საკრედიტო ბარატით")


class PayPalPayment:
    def pay(self, amount):
        print(f"{amount} ლარი გადახდილია paypal-ით")


class CryptoPayment:
    def pay(self, amount):
        print(f"{amount} ლარი გადახდილია კრიპტოთი")


# credit_card = CreditCardPayment()
# paypal = PayPalPayment()
# crypto = CryptoPayment()
#
# credit_card.pay(100)
# paypal.pay(200)
# crypto.pay(300)