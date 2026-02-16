import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    "SquareFootage": [600, 800, 1000, 1200, 1500, 1800, 2000, 2300],
    "Price": [300000, 400000, 520000, 610000, 750000, 900000, 1050000, 1200000],
    "City": ["Mumbai", "Delhi", "Mumbai", "Bangalore",
             "Delhi", "Mumbai", "Bangalore", "Mumbai"]
}

df = pd.DataFrame(data)
plt.figure()
plt.scatter(df["SquareFootage"], df["Price"])
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.title("House Size vs Price")
plt.show()
plt.figure()
sns.boxplot(x="City", y="Price", data=df)
plt.xlabel("City")
plt.ylabel("Price")
plt.title("Price Distribution by City")
plt.show()
print("Observation:")
print("As SquareFootage increases, Price generally increases.")