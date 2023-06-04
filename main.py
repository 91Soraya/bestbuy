import products
import store


def menu_options():
    """
    Returns a string of the menu options for the store.
    """
    menu_text = f"1. List all products in store \n" \
                f"2. Show total amount in store\n" \
                f"3. Make an order\n" \
                f"4. Quit"
    return menu_text


def get_user_selection():
    """
    Requests user to make a menu selection and returns the selection as an int.
    """
    while True:
        try:
            user_selection = int(input("Please choose a number: "))
            if 0 < user_selection <= 4:
                return user_selection
            else:
                print("Number not in menu. Please choose a number between 1 and 4")
        except ValueError:
            print("Not a valid option.")


def create_shopping_list():
    """
    Requests product name and quantity from the user, and adds to the shopping list.
    :return: Shopping list of tuple with product name and quantity.
    """
    shopping_list = []
    add_other_product = True
    while add_other_product:
        product_name_input = input("Please enter product name: ")
        product_quantity = int(input("Please enter quantity: "))
        shopping_list_item = (product_name_input, product_quantity)
        shopping_list.append(shopping_list_item)
        user_input_add_other_product = input("Do you want to add another product to the shopping list? yes or no: ")
        if user_input_add_other_product == "yes":
            add_other_product = True
        else:
            return shopping_list


def start(store_object):
    """
    Takes a store object, gets user selection as menu_selection,
    performs the selected option on the store_object.
    """
    products = store_object._all_products
    while True:
        print(menu_options())
        menu_selection = get_user_selection()
        if menu_selection == 1:
            for product in products:
                print(product.show())
        if menu_selection == 2:
            print(store_object.get_total_quantity())
        if menu_selection == 3:
            complete_shopping_list = create_shopping_list()
            print(complete_shopping_list)
            store_object.order(complete_shopping_list)
        if menu_selection == 4:
            quit()


def main():
    """
    Setup initial stock of inventory, creates the store object
    and runs the menu options and selection on the store object.
    """
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == '__main__':
    main()
