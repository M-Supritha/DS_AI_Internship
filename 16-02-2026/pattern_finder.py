import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("pattern_finder.csv")
corr_matrix = df.corr()

print("Correlation Matrix:")
print(corr_matrix)

plt.figure()
plt.imshow(corr_matrix, cmap="coolwarm")
plt.colorbar()
plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=45)
plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)
plt.title("Correlation Heatmap")
plt.show()

print("\nHighly Correlated Feature Pairs (Correlation > 0.8):")

for i in range(len(corr_matrix.columns)):
    for j in range(i):
        if abs(corr_matrix.iloc[i, j]) > 0.8:
            print(corr_matrix.columns[i], "and", corr_matrix.columns[j],
                  "->", corr_matrix.iloc[i, j])

plt.figure()
plt.boxplot(df["Price"])
plt.title("Boxplot of Price (Outlier Detection)")
plt.ylabel("Price")
plt.show()
