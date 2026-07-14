"""
Load processed orders to the target system.

This module is responsible for retrieving database credentials and saving processed orders to the Orders API. Failed API calls are
retried based on the configured retry limit before being marked as failed.
"""

import os
import logging
import time
from loafly.config import SETTINGS
from data.starter.gateway import save_to_orders_api


def get_db_password():
    """
    Retrieve the database password from the environment.

    Returns:
        str: Database password. If the environment variable is not set, a default password is returned.
    """
    return os.getenv("DB_PASSWORD", "demo-password")

def save_order(order, final_price):
    """
    Save an order to the Orders API with retry logic.

    Attempts to save the processed order to the target API. If the request fails due to a connection error, the operation is retried
    up to the configured maximum number of attempts.

    Args:
        order: Order object containing order details.
        final_price (float): Final order amount after pricing.

    Returns:
        None
    """
    password = get_db_password()
    retries = SETTINGS["max_save_retries"]
    for attempt in range(1, retries+1):
        try:
            order_id = order.order_id
            response = save_to_orders_api(order_id, final_price)
            logging.info("Saved order %s for %s", order.order_id, order.customer)
            return
        except(ConnectionError) as e:
            logging.warning("Save failed for order %s (attempt %s): %s, trying again", order.order_id, attempt, e)
        time.sleep(0.5)    
    logging.error("Gave up saving order %s", order.order_id) 
    