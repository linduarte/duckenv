import os
import sqlite3

import duckdb

base_dir = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(base_dir, "../database", "drug_duck.db")

# Connect to the DuckDB database
con_duckdb = duckdb.connect(database=database_path)  # type: ignore

# Query the table from DuckDB
df = con_duckdb.execute("SELECT * FROM medic").fetch_df()  # type: ignore

# Close the DuckDB connection
con_duckdb.close()

# Define the path for the exported SQLite database file
export_file_path = (
    "C:/Users/clldu/OneDrive/vsc_envir/duck_ground/.venv/exported_database.db"
)

# Create a connection to the SQLite database
con_sqlite = sqlite3.connect(export_file_path)

# Write the DataFrame to SQLite
df.to_sql("medic", con_sqlite, if_exists="replace", index=False)

# Close the SQLite connection
con_sqlite.close()

if __name__ == "__main__":
    print("Database exported successfully!")
