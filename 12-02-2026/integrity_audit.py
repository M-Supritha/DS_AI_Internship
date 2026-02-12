import pandas as pd
df = pd.read_csv("customer_orders.csv")
print("shape before cleaning:",df.shape)
print("\nMissing values report:",df.isna().sum())
numeric_cols = df.select_dtypes(include="number").columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
df = df.drop_duplicates()
print("Shape after cleaning:", df.shape)