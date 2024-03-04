import os
import duckdb

base_dir = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(base_dir, "../database", "drug_duck.db")

# Connect to the existing database file
con = duckdb.connect(database=database_path)  # type: ignore

# Create an index in a database
con.execute(("CREATE INDEX idx_med ON medic (idx_column)"))  # type: ignore

# Commit the changes
con.commit()

con.close()

if __name__ == "__main__":
    print("Index created successfully!")
