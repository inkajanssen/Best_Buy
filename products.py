class Product:

    def __init__(self, name, price, quantity):
        """
        Initiator (constructor) method.
        Creates the instance variables (active is set to True).
        If something is invalid (empty name / negative price or quantity),
        raises an exception.
        :param name:
        :param price:
        :param quantity:
        """
        self.active = None
        if not type(name) == str or name == "":
            raise TypeError("Invalid name")

        if type(price) != float and type(price) != int:
            raise TypeError("Price must be a number")

        if not type(quantity) == int:
            raise TypeError("Quantity must be an int")

        self.name = name
        self.price = price
        self.quantity = quantity
        Product.activate(self)


    def get_quantity(self) -> int:
        """
        Getter function for quantity.
        Returns the quantity (int).
        :return:
        """
        return self.quantity


    def set_quantity(self, quantity):
        """
        Setter function for quantity. If quantity reaches 0, deactivates the product.
        Set activate to true if the quantity is over 0.
        :return:
        """
        self.quantity = quantity

        if not Product.is_active(self):
            Product.activate(self)

        if quantity == 0:
            Product.deactivate(self)


    def is_active(self)-> bool:
        """
        Getter function for active.
        Returns True if the product is active, otherwise False.
        :return:
        """
        return self.active


    def activate(self):
        """
        Activates the product.
        :return:
        """
        self.active = True


    def deactivate(self):
        """
        Deactivates the product.
        :return:
        """
        self.active = False


    def show(self):
        """
        Prints a string that represents the product
        :return:
        """
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def buy(self, quantity)-> float:
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        In case of a problem (when? think about it), raises an Exception.
        :param quantity:
        :return:
        """
        if not self.is_active():
            raise Exception("There is no such product")

        if quantity > self.quantity:
            raise Exception(f"There are only {self.quantity} {self.name} left")

        price = quantity * self.price
        new_quantity = self.quantity - quantity
        Product.set_quantity(self, new_quantity)
        return price