import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("House_data_500.csv")

print("Columns in dataset:", df.columns)

plt.figure()
plt.scatter(df["SquareFootage"], df["Price"])
plt.xlabel("SquareFootage")
plt.ylabel("Price")
plt.title("House Size vs Price")
plt.show()

plt.figure()
sns.boxplot(x="City", y="Price", data=df)
plt.xlabel("City")
plt.ylabel("Price")
plt.title("Price Distribution by City")
plt.xticks(rotation=45)
plt.show()

print("Observation:")
print("As SquareFootage increases, Price tends to increase, showing a positive relationship.")
