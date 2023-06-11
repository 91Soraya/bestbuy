--ORIGINAL PROJECT INSTRUCTIONS--

Best Buy

The exercise is to create an engine for powering a tech equipment store like “Best Buy” 💻. 
Using the program you can list products and make an order.

Overview

In the first steps you’ll create the basic classes - Product and Store. Then, you will implement a user interface. 

Step 1 - Product Class

The Product class represents a specific type of product available in the store (For example, MacBook Air M2). It encapsulates information about the product, including its name and price.
Additionally, the Product class includes an attribute to keep track of the total quantity of items of that product currently available in the store. When someone will purchase it, the amount will be modified accordingly.

Class Specification

Instance variables:

Name (str)
Price (float)
Quantity (int)
Active (bool)
Methods

__init__(self, name, price, quantity)
Initiator (constructor) method.
Creates the instance variables (active is set to True).

If something is invalid (empty name / negative price or quantity), raises an exception.

get_quantity(self) -> float
Getter function for quantity.
Returns the quantity (float).
set_quantity(self, quantity)
Setter function for quantity. If quantity reaches 0, deactivates the product.
is_active(self) -> bool
Getter function for active.
Returns True if the product is active, otherwise False.
activate(self)
Activates the product.
deactivate(self)
Deactivates the product.
show(self) -> str
Returns a string that represents the product, for example:
"MacBook Air M2, Price: 1450, Quantity: 100"
buy(self, quantity) -> float
Buys a given quantity of the product.
Returns the total price (float) of the purchase.
Updates the quantity of the product.
In case of a problem (when? think about it), raises an Exception.

Task
In the file products.py, create the new class Product according to the specification above.
When you’re done, you can check that everything works using this code (put it in your main function):


bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()

Step 2 - Store Class
Now we have a bunch of instances of Product, but we might need something to connect them all together. 
Let’s create a class called Store that will hold all of these products, and will allow the user to make a purchase of multiple products at once.

Specification

The Store class will contain one variable - a list of products that exist in the store. It will expose the following methods:

add_product(self, product)
remove_product(self, product)
Removes a product from store.
get_total_quantity(self) -> int
Returns how many items are in the store in total.
get_all_products(self) -> List[Product]
Returns all products in the store that are active.
order(self, shopping_list) -> float
Gets a list of tuples, where each tuple has 2 items:
Product (Product class) and quantity (int).
Buys the products and returns the total price of the order.

Task

In the file store.py, create the new class Store according to the specification above.
When you’re done, you can check that everything works using this code (put it in your main function):

product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
               ]

store = Store(product_list)
products = store.get_all_products()
print(store.get_total_quantity())
print(store.order([(products[0], 1), (products[1], 2)]))

Step 3 - User Interface

Now that we have both of the classes for managing the store, let’s create a user interface! 🖥️
in the file main.py, Create a default inventory using this code:

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)

hen, create a function called start that will get the store object as a parameter, and will show the user the following menu:
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit

