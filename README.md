# Loafly ETL Pipeline

## Overview

This project is a production-style ETL pipeline developed for the **Codebasics Data Engineering Bootcamp**. It refactors a legacy order-processing script into a modular, maintainable Python application by following software engineering best practices.

The pipeline extracts customer orders from a CSV file, transforms and validates the data, applies configurable discounts, and loads the processed orders to a simulated Orders API with retry handling and logging.

---

## Technologies Used

- Python 3
- CSV
- Object-Oriented Programming (OOP)
- Logging
- Environment Variables
- Exception Handling
- Retry Logic

---

## Project Structure

```
loafly-etl-pipeline/
│
├── data/
│   ├── raw_orders.csv
│   └── starter/
│       ├── gateway.py
│       └── legacy_orders.py
│
├── loafly/
│   ├── __init__.py
│   ├── config.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── models.py
│
├── run_pipeline.py
├── requirements.txt
└── README.md
```

---

## Pipeline Workflow

```
Raw CSV
    │
    ▼
Extract
    │
    ▼
Transform
    │
    ├── Build Order Objects
    ├── Clean Price Values
    ├── Validate Records
    └── Apply Discount
    │
    ▼
Load
    │
    ├── Retry Failed API Calls
    ├── Read Environment Variables
    └── Save Orders
```

---

## Key Features

- Modular ETL architecture (Extract → Transform → Load)
- Object-oriented order model
- Configuration-driven pipeline
- Centralized logging
- Exception handling
- Automatic retry mechanism for API failures
- Environment variable support for sensitive configuration
- Well-documented code with Python docstrings

---

## Modules

### extract.py
- Reads raw CSV data
- Groups items belonging to the same order
- Returns structured order records

### transform.py
- Cleans price values
- Creates `Order` objects
- Applies configurable discounts
- Calculates final order totals

### models.py
- Defines the `Order` domain model
- Stores order details and purchased items
- Calculates total order value

### load.py
- Reads credentials from environment variables
- Saves processed orders to the target API
- Retries failed API requests
- Logs successful and failed operations

### config.py
Stores configurable application settings such as:
- Input file path
- Discount percentage
- Currency
- Maximum retry attempts

### run_pipeline.py
Main entry point that orchestrates the complete ETL workflow.

---

## Concepts Demonstrated

- ETL Pipeline Design
- Modular Python Development
- Object-Oriented Programming
- Configuration Management
- Logging
- Exception Handling
- Retry Strategy
- Environment Variables
- Code Refactoring
- Python Documentation (Docstrings)

---

## How to Run

1. Clone the repository.

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Set the database password (optional):

```bash
export DB_PASSWORD=your_password
```

4. Run the pipeline:

```bash
python run_pipeline.py
```

---

## Output

The pipeline:

- Extracts orders from the input CSV
- Cleans and validates order data
- Applies configured discounts
- Saves processed orders to the simulated Orders API
- Logs processing progress and retries failed API calls when necessary

---

## Author

**Shalini Goutam**
