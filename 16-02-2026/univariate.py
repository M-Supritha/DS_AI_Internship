import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis
data = {
    "Price": [250000, 300000, 280000, 450000, 600000, 320000, 700000, 800000, 270000, 290000],
    "City": ["Mumbai", "Delhi", "Mumbai", "Bangalore", "Mumbai",
             "Delhi", "Bangalore", "Mumbai", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data)

plt.figure()
sns.histplot(df["Price"], kde=True)
plt.title("Distribution of Housing Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()
price_skewness = skew(df["Price"])
price_kurtosis = kurtosis(df["Price"])

print("Skewness of Price:", price_skewness)
print("Kurtosis of Price:", price_kurtosis)
plt.figure()
sns.countplot(x="City", data=df)
plt.title("Count of Houses by City")
plt.xlabel("City")
plt.ylabel("Count")
plt.show()