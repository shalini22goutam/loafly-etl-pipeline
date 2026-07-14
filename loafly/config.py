"""
Application configuration settings.

This module contains configurable constants used across the application,including input file locations, pricing settings, 
currency, and retry limits for saving data.
"""

SETTINGS = {
    "file_path" : "data/raw_orders.csv",
    "currency": "INR",
    "discount_percent": 10,    
    "max_save_retries": 3,
}
