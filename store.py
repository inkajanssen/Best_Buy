from products import Product

class Store:
    """
    Store will hold all products and will allow the user to make a purchase
    of multiple products at once.
    """

    def __init__(self, list_of_products):
        """
        Initiator (constructor) method.
        Creates the instance variables for a list of products.
        :param list_of_products:
        """
        self.list_of_products = list_of_products


    def add_product(self, product):
        """
        adds a product to the list of products
        :param product:
        :return:
        """
        self.list_of_products.append(product)


    def remove_product(self, product):
        """
        Removes a product from store.
        :param product:
        :return:
        """
        self.list_of_products.remove(product)


    def get_total_quantity(self)-> int:
        """
        Returns how many items are in the store in total.
        :return:
        """
        total_quantity = 0
        for product in self.list_of_products:
            total_quantity += Product.get_quantity(product)
        return total_quantity


    def get_all_products(self)-> list[Product]:
        """
        Returns all products in the store that are active.
        :return:
        """
        active_products = []
        for product in self.list_of_products:
            if Product.is_active(product):
                active_products.append(product)
        return active_products


    def order(self, shopping_list)-> float:
        """
        Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.
        :param shopping_list:
        :return: total price
        """
        total_price = 0

        for purchase in shopping_list:
            product, quantity = purchase
            price = Product.buy(product, quantity)
            total_price += price

        return total_price

product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250)
                 ]

best_buy = Store(product_list)