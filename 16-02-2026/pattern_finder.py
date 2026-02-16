import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Price": [250000, 300000, 280000, 450000, 600000, 320000, 700000, 800000, 270000, 1200000],
    "SquareFootage": [700, 850, 800, 1200, 1600, 900, 1800, 2000, 780, 3000],
    "Bedrooms": [1, 2, 2, 3, 4, 2, 4, 5, 2, 6],
    "Bathrooms": [1, 2, 1, 2, 3, 2, 3, 4, 2, 5]
}

df = pd.DataFrame(data)
corr_matrix = df.corr()

plt.figure()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix Heatmap")
plt.show()
print("Highly correlated feature pairs (correlation > 0.8):")
for col in corr_matrix.columns:
    for row in corr_matrix.index:
        if col != row and corr_matrix.loc[row, col] > 0.8:
            print(f"{row} and {col}: {corr_matrix.loc[row, col]:.2f}")

plt.figure()
sns.boxplot(y=df["Price"])
plt.title("Boxplot of Housing Prices")
plt.ylabel("Price")
plt.show()