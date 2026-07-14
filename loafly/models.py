"""
Order domain model.

This module defines the Order class, which represents a customer order containing one or more items. 
It provides methods to add items and calculate the total order value.
"""


class Order:
    """
    Represents a customer order.

    An order consists of an order ID, customer name, and a collection of purchased items. 
    Each item is stored as a tuple containing the item name and its price.
    """

    def __init__(self, order_id, customer):
        """
        Initialize a new Order instance.

        Args:
            order_id (str): Unique identifier for the order.
            customer (str): Name of the customer.
        """
        self.order_id = order_id
        self.customer = customer
        self.items = []

    def add_item(self, item_name, item_price):
        """
        Add an item to the order.

        Args:
            item_name (str): Name of the purchased item.
            item_price (float): Price of the item.
        """
        self.items.append((item_name, item_price))

    def total(self):
        """
        Calculate the total value of the order.

        Returns:
            float: Sum of the prices of all items in the order.
        """
        total_price = 0 
        for item_name, item_price  in self.items:
            total_price+=item_price
        return total_price

            



