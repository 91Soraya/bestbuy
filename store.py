import products


class Store:

    def __init__(self, list_of_products):
        self._all_products = list_of_products

    def add_product(self, product):
        self._all_products.append(product)

    def remove_product(self, product):
        if product in self._all_products:
            product_index = self._all_products.index(product)
            del self._all_products[product_index]
            print(f"Product removed.")

    def get_total_quantity(self):
        total_quantity = 0
        for product_in_store in self._all_products:
            total_quantity += product_in_store._quantity
        return int(total_quantity)

    def get_all_products(self):
        list_of_all_active_products = []
        for product in self._all_products:
            if product._is_active:
                list_of_all_active_products.append(product._name)
        return list_of_all_active_products

    def order(self, shopping_list):
        total_price = 0
        for item in shopping_list:
            item_name = item[0]
            quantity = item[1]
            for product in self._all_products:
                if product._name == item_name:
                    total_price += product.buy(quantity)
        return float(total_price)


product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
                ]

store = Store(product_list)
products = store.get_all_products()
print(store.get_total_quantity())
print(store.order([(products[0], 1), (products[1], 2)]))
print(store.get_total_quantity())
