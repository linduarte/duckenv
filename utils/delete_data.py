import os
import duckdb

base_dir = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(base_dir, "../database", "drug_duck.db")

# Connect to the existing database file
con = duckdb.connect(database=database_path)  # type: ignore

"""
-- remove the rows matching the condition "i=2" from the database
DELETE FROM tbl WHERE i=2;
-- delete all rows in the table "tbl"
DELETE FROM tbl;
"""

# Delete a row "i=1"
con.execute(("DELETE FROM medic WHERE idx_column=1;"))  # type: ignore

# Commit the changes
con.commit()

con.close()

if __name__ == "__main__":
    print("Deleted row successfully!")
