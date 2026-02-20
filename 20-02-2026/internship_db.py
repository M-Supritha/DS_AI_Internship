import sqlite3
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    track TEXT NOT NULL,
    stipend INTEGER
)
""")
intern_data = [
    (1, "Aisha", "Data Science", 15000),
    (2, "Rahul", "Web Dev", 12000),
    (3, "Sneha", "Cyber Security", 14000),
    (4, "Karan", "Data Science", 16000),
    (5, "Meera", "Web Dev", 13000)
]
cursor.executemany("INSERT OR REPLACE INTO interns VALUES (?, ?, ?, ?)", intern_data)
cursor.execute("SELECT name, track FROM interns")

results = cursor.fetchall()
print("Intern Name and Track:")
for row in results:
    print(row)
conn.commit()
conn.close()