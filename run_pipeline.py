"""
Main entry point for the Loafly order processing pipeline.

This script orchestrates the end-to-end ETL workflow by extracting raw order data, transforming it into validated Order objects,
calculating discounted prices, and loading the processed orders into the target Orders API.
"""

import logging
from loafly.config import SETTINGS
from loafly.extract import extract
from loafly.transform import build_order, transform_order
from loafly.load import save_order

logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(levelname)s  %(message)s")

def main():
    """
    Execute the complete order processing workflow.

    Reads raw orders from the configured input file, transforms each order by cleaning prices and applying discounts, and
    saves the processed orders to the Orders API.
    """
    try:
        logging.info("Starting today's order run")
        raw_orders = extract(SETTINGS['file_path'])
        for raw_order in raw_orders:
            order = build_order(raw_order)
            discounted_price = transform_order(order, SETTINGS["discount_percent"])
            save_order(order, discounted_price)
        logging.info("Order processing completed successfully.")
    except Exception as e:
        logging.exception("Order processing failed. The error is %s", e)



if __name__ == "__main__":
    main()