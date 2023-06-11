from abc import ABC, abstractmethod
import products

# Single-Product Promotion
# Promotions are applied on a single product only, no mixing. For example, if the promotion “Second item at half price” is applied on the Product Mac, then for every two Mac items that I bought I get one for free.
# Single Promotion for each Product
# Products can have only one promotion at a given time.
# Bonus: support multiple promotions for a single item.

class Promotion(ABC):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass

class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        self.percent = percent
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        price_without_discount = quantity * product._price
        discount_price = price_without_discount * (self.percent/100)
        return price_without_discount - discount_price

class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity):
        no_promo_price = 0
        while quantity % 2 != 0:
            no_promo = quantity % 2
            no_promo_price = product._price * no_promo
            quantity -= no_promo

        if quantity % 2 == 0:
            product._price *= 0.75
            total_price = quantity * product._price
            total_price += no_promo_price
            return total_price


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity):
        no_promo_price = 0
        total_price = 0
        while quantity % 3 != 0:
            no_promo = quantity % 3
            no_promo_price = product._price * no_promo
            quantity -= no_promo

        if quantity % 3 == 0:
            no_discount_price = quantity * product._price
            free_amount = quantity / 3
            discount_price = free_amount * product._price
            total_price = no_discount_price - discount_price
            total_price += no_promo_price
        return total_price


