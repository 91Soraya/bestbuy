class Product:
    def __init__(self, name, price, quantity):
        if len(name) > 1:
            self._name = name
        else:
            raise ValueError('No name entered.')
            self._name = input("Please enter the name of the product: ")


        if float(price) > 0:
            self._price = float(price)
        else:
            raise ValueError("Negative price.")
            self._price = float(input("Please enter the price: "))

        try:
            if quantity > 0:
                self._quantity = float(quantity)
            else:
                self._quantity = float(input("Please enter the quantity: "))
        except TypeError:
            self._quantity = float(input("Quantity entered is not a number. Please enter the quantity: "))

        self._is_active = True

    def get_quantity(self):
        return float(self._quantity)

    def set_quantity(self, quantity):
        if int(quantity) <= 0:
            self._is_active = False
        else:
            self._quantity = int(quantity)

    def is_active(self):
        return self._is_active

    def deactivate(self):
        self._is_active = False

    def show(self):
        return f"{self._name}, Price: {self._price}, Quantity: {self._quantity}"

    def buy(self, quantity):
        try:
            int(quantity)
        except ValueError:
            quantity = int(input("Please enter quantity: "))

        if quantity <= self._quantity:
            total_price = quantity * float(self._price)
            self._quantity -= quantity
        else:
            total_price = self._quantity * float(self._price)
            print(f"Only {self._quantity} available of {self._name}.")
            self._quantity = 0

        if self._quantity == 0:
            self.deactivate()

        return total_price

# bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
# mac = Product("MacBook Air M2", price=1450, quantity=100)

# print(bose.buy(50))
# print(mac.buy(100))
# print(mac.is_active())

# print(bose.show())
# print(mac.show())

# bose.set_quantity(1000)
# print(bose.show())
