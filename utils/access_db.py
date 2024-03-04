import os

import pandas as pd

import duckdb

# from tabulate import tabulate # type: ignore

base_dir = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(base_dir, "../database", "drug_duck.db")

# Connect to the existing DuckDB database
con = duckdb.connect(database=database_path)  # type: ignore

# Retrieve the table data
query = "SELECT * FROM medic"
result = con.execute(query).fetchall()  # type: ignore

# Convert the result to a pandas DataFrame
df = pd.DataFrame(
    result,
    columns=[
        "idx_column",
        "last_updated",
        "medicine",
        "stock_medicine_box",
        "drug_dosage",
        "prescription_valid_until",
        "drug_container",
    ],
)

# Print the DataFrame in markdown format
markdown_table = df.to_markdown(index=False)
print(markdown_table)

con.close()
