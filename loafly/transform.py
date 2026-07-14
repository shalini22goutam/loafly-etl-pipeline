"""
Transform raw order data into validated Order objects.

This module provides helper functions to clean price values, apply discounts, construct Order objects from raw input data,
and calculate the final discounted order total.
"""

import logging

from loafly.models import Order
from loafly.config import SETTINGS

def clean_price(text):
    """
    Convert a price string into a floating-point value.

    Removes thousands separators before converting the value
    to a float.

    Args:
        text (str): Price represented as a string.

    Returns:
        float: Parsed price value.
    """
    return float(text.replace(",", ""))

def apply_discount(price, percent):
    """
    Apply a percentage discount to a price.

    Args:
        price (float): Original price.
        percent (float): Discount percentage.

    Returns:
        float: Discounted price.
    """
    return price - price * percent / 100
   

def build_order(raw_order):
    """
    Build an Order object from raw order data.

    Converts item prices to numeric values and skips items with invalid prices.

    Args:
        raw_order (dict): Raw order data.

    Returns:
        Order: Populated Order object.
    """
    logging.info("Building order %s for customer '%s'.", raw_order["order_id"],raw_order["customer"])

    order = Order(raw_order["order_id"], raw_order["customer"])
    for item_name, item_price in raw_order["items"]:
        try:
            cleaned_price = clean_price(item_price)
        except(TypeError, AttributeError,ValueError): 
            logging.warning("Order %s item '%s' has no price, skipping it", raw_order["order_id"], item_name)
            continue
        order.add_item(item_name, cleaned_price)

    return order

def transform_order(order, discount_percent):
    """
    Calculate the discounted total for an order.

    Args:
        order (Order): Order to transform.
        discount_percent (float): Discount percentage.

    Returns:
        float: Discounted order total.
    """
    total = order.total()
    discounted_price = apply_discount(total, discount_percent)
    logging.info("Order %s total: %s %.2f (after %d%% discount).",order.order_id, SETTINGS["currency"], discounted_price, discount_percent)
    return discounted_price