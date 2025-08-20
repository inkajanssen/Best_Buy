from products import Product

class Store:
    list_of_products = []


    def add_product(self, product):
        """
        adds a product to the list of products
        :param product:
        :return:
        """
        pass


    def remove_product(self, product):
        """
        Removes a product from store.
        :param product:
        :return:
        """
        pass


    def get_total_quantity(self)-> int:
        """
        Returns how many items are in the store in total.
        :return:
        """
        pass


    def get_all_products(self)-> list[Product]:
        """
        Returns all products in the store that are active.
        :return:
        """
        pass


    def order(self, shopping_list)-> float:
        """
        Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.
        :param shopping_list:
        :return:
        """
        pass