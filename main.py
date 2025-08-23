import sys

from products import Product
from store import Store


def initialize_store():
    """
    Setup initial stock of inventory
    """
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]

    best_buy = Store(product_list)
    return best_buy


def start():
    """
    Show the user the following menu
    :param: the store
    :return: print a menu
    """
    print("""
        ********** Store Menu **********
        Menu:
        1. List all products in store
        2. Show total amount in store
        3. Make an order
        4. Quit

        Enter choice (0-4): 
        """)


def pause():
    """
    Give the user a pause to read output and then print menu again
    :return:
    """
    input("Press Enter to continue...")


def list_all_products(store):
    """
    Lists all products in store
    :return:
    """
    for position, product in enumerate(store.list_of_products, 1):
        print(f"{position}. {product.show()}")


def show_total_amount(store):
    """
    Show total amount in store
    :return:
    """
    print(f"Total of {Store.get_total_quantity(store)} items in store")


def make_order(store):
    """
    Make an order from the store
    Get product and amount from user and order from store
    :return:
    """
    print(5 * '-')
    list_all_products(store)
    print(5 * '-')
    print("When you want to finish order, enter empty text.")

    shopping_list = []
    while True:
        product = input("Which product # do you want?")
        amount = input("What amount do you want?")

        if not product and not amount:
            try:
                total_price = Store.order(store, shopping_list)
            except Exception:
                print("Error while making order! Quantity larger than what exists")
                break
            print(f"Order made! Total payment:{total_price}")
            break

        try:
            product = int(product)
            amount = int(amount)

            order = store.list_of_products[product -1], amount # -1 cause we start enumerate at 1
            shopping_list.append(order)
            print("Product added to list!")

        except ValueError:
            print("Error adding product!")


def main():
    """
    Initialize the store
    Print the menu
    Get the desired function
    Reload or end menu
    :return:
    """
    # Dictionary to get functions
    menu_functions = {
        1: list_all_products,
        2: show_total_amount,
        3: make_order
    }

    try:
        store = initialize_store()
    except TypeError:
        print("A product was not created properly.")
        sys.exit(0)

    while True:
        start()

        try:
            option = int(input())

            if option == 4:
                print("Bye!")
                return False

            if option in menu_functions:
                menu_functions[option](store)
                pause()

            else:
                print("Wrong input")
                pause()

        except ValueError:
            print("The option should only be a number")
            pause()


if __name__ == '__main__':
    main()
