import os

import duckdb

import duckdb

# import pandas as pd

base_dir = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(base_dir, "../database", "drug_duck.db")

# Create the database file
con = duckdb.connect(database=database_path)  # type: ignore

# Create a table
con.execute(
    """
    CREATE TABLE medic (
        idx_column INTEGER,
        last_updated VARCHAR,
        medicine VARCHAR PRIMARY KEY,
        stock_medicine_box INTEGER,
        drug_dosage INTEGER,
        prescription_valid_until VARCHAR,
        drug_container INTEGER
    )
"""
)

# Fetch and display the results
result = con.execute("SELECT * FROM medic").fetch_df()  # type: ignore
print(result)

# Commit the changes
con.commit()

con.close()

if __name__ == "__main__":
    print("OK - Database created successfully!")
