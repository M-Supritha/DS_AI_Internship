import numpy as np
import pandas as pd

np.random.seed(42)

data = np.random.normal(loc=50, scale=10, size=1000)

data = np.append(data, [120, -20])

df = pd.DataFrame({"Values": data})

mean = df["Values"].mean()
std_dev = df["Values"].std()

print(f"Mean (μ) = {mean:.2f}")
print(f"Standard Deviation (σ) = {std_dev:.2f}")

df["z_score"] = (df["Values"] - mean) / std_dev

outliers = df[np.abs(df["z_score"]) > 3]

print("\nOutliers (|Z| > 3):")
print(outliers)
print(f"\nTotal Outliers Found: {len(outliers)}")
