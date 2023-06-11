import promotions
class Product:
    def __init__(self, name, price, quantity):
        self.promotion = None
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
        return f"{self._name}, Price: {self._price}, Quantity: {self._quantity}."

    def set_promotion(self, promotion):
        self.promotion = promotion

    def buy(self, quantity):
        try:
            int(quantity)
        except ValueError:
            quantity = int(input("Please enter quantity: "))

        quantity_for_promotion = int(quantity)

        if quantity <= self._quantity:
            total_price = quantity * float(self._price)
            self._quantity -= quantity
        else:
            raise ValueError("Requested amount higher than quantity.")
            total_price = self._quantity * float(self._price)
            print(f"Purchased {self._quantity} of {self._name}, as only {self._quantity} are available.")
            self._quantity = 0

        if self._quantity == 0:
            self.deactivate()

        if self.promotion != None:
            total_price = self.promotion.apply_promotion(self, quantity)
            return total_price

        return total_price



class NonStockedProduct(Product):
    """
    Some products in the store are not physical,
    so we don’t need to keep track of their quantity.
    for example - a Microsoft Windows license. On these products,
    the quantity should be set to zero and always stay that way.
    """
    def __init__(self, name, price):
        quantity = 1
        super().__init__(name, price, quantity)
        self._quantity = 0

    def buy(self, quantity):
        if self.promotion != None:
            total_price = self.promotion.apply_promotion(self, quantity)
            return total_price
        return quantity * float(self._price)

    def set_quantity(self, quantity):
        pass

    def show(self):
        return f"{self._name}, Price: {self._price}"


class LimitedProduct(Product):
    """
    Some products can only be purchased X times in an order.
    For example - a shipping fee can only be added once.
    If an order is attempted with quantity larger than the maximum one,
    it should be refused with an exception.
    """
    def __init__(self, name, price, quantity, maximum):
        self._limit_per_order = maximum
        super().__init__(name, price, quantity)

    def buy(self, quantity):
        try:
            int(quantity)
        except ValueError:
            quantity = int(input("Please enter quantity: "))

        if quantity > self._limit_per_order:
            raise ValueError(f"Amount ordered not permitted.")

        if quantity <= self._quantity:
            total_price = quantity * float(self._price)
            self._quantity -= quantity
        else:
            raise ValueError("Requested amount higher than quantity.")
            total_price = self._quantity * float(self._price)
            print(f"Purchased {self._quantity} of {self._name}, as only {self._quantity} are available.")
            self._quantity = 0

        if self._quantity == 0:
            self.deactivate()

        if self.promotion != None:
            total_price = self.promotion.apply_promotion(self, quantity)
            return total_price

        return total_price
