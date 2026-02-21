import sqlite3
import pandas as pd
conn = sqlite3.connect("internship.db")
filter_query = """
SELECT *
FROM interns
WHERE track = 'Data Science'
AND stipend > 5000
"""
df_filter = pd.read_sql_query(filter_query, conn)
print("Filtered Data (Data Science & stipend > 5000):")
print(df_filter)
avg_query = """
SELECT track,
       AVG(stipend) AS average_stipend
FROM interns
GROUP BY track
"""
df_avg = pd.read_sql_query(avg_query, conn)
print("\nAverage Stipend Per Track:")
print(df_avg)
count_query = """
SELECT track,
       COUNT(*) AS total_interns
FROM interns
GROUP BY track
"""
df_count = pd.read_sql_query(count_query, conn)
print("\nNumber of Interns Per Track:")
print(df_count)
conn.close()