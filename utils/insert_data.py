import os
import duckdb

base_dir = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(base_dir, "../database", "drug_duck.db")

# Connect to the existing database file
con = duckdb.connect(database = database_path) # type: ignore

# Insert data into the medic table row by row
rows = [
    (1, '30/05/2023', 'Losartana', 30, 2, '10/06/2023', 2),
(2, '30/05/2023', 'AAS', 30, 1,'10/06/2023',1),
(3, '30/05/2023', 'Anlodipino',30, 1, '10/06/2023', 1),
(4, '30/05/2023', 'Hidroclorotiazida', 30, 1, '10/06/2023', 1),
(5, '30/05/2023', 'Atorvastatina', 30, 1, '10/06/2023',1)
]

for row in rows:
    con.execute("""
        INSERT INTO medic (idx_column, last_updated, medicine, stock_medicine_box, drug_dosage, prescription_valid_until, drug_container)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, row)

# Commit the changes
con.commit()

con.close()

if __name__ == "__main__":
    print("Data inserted successfully!")
