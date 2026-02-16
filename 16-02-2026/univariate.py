
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis


df = pd.read_csv("House_price.csv")

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
sns.countplot(x="Location", data=df)
plt.title("Count of Houses by City")
plt.xlabel("Location")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

