import os
import duckdb

base_dir = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(base_dir, "../database", "drug_duck.db")

# Connect to the existing database file
con = duckdb.connect(database = database_path) # type: ignore

cur = con.cursor()
cur.execute("PRAGMA table_info('medic')")
rows = cur.fetchall() # type: ignore
for row in rows: # type: ignore
    print(row) # type: ignore