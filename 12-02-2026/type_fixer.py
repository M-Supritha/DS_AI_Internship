import pandas as pd
data = {
    "Price": ["$100", "$250.50", "$75", "$300"],
    "Date" : ["2024-01-01", "2024-01-05", "2024-01-10", "2024-01-15"]
}
df = pd.DataFrame(data)
print("Intial data types:\n", df.dtypes)
df["Price"] = df["Price"].str.replace("$", "", regex = False).astype(float)
df["Date"] = pd.to_datetime(df["Date"])
print("Data type after conversion:\n",df.dtypes)