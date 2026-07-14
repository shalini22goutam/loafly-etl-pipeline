"""
Extract order data from a CSV file and group items by order.

The function reads a flat CSV file where each row represents an item within an order. It groups items by order ID and returns a list of
nested order dictionaries.
"""

import csv
import logging

def extract(file_path):
    """
    Read orders from a CSV file and group items by order.

    Each row in the source file represents a single item belonging to an order. Items with the same order ID are grouped together 
    into a single order record.

    Args:
        file_path (str): Path to the input CSV file.

    Returns:
        list: A list of dictionaries, where each dictionary contains the order ID, customer name, and associated order items.
    """

    orders = {}
    orders_list = []

    logging.info("Starting order extraction from '%s'.", file_path)

    try:
        with open(file_path, newline="", encoding="utf-8") as f:
            logging.info("Reading order records from CSV file.")
            for row in csv.DictReader(f):
                order_id = row["order_id"]
                customer = row["customer"]
                if order_id not in orders:
                    orders[order_id] = {"order_id":order_id, "customer": customer, "items": []}
                orders[order_id]["items"].append((row["item_name"], row["item_price"]))

        orders_list = list(orders.values())

        logging.info("Successfully extracted %d orders.", len(orders_list))
    
        return orders_list
            
    except Exception as e:
        logging.exception("Failed to extract orders from '%s'. The exception is %s", file_path, e)






