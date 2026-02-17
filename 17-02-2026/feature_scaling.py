import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler
data = {
    "Age": [22, 25, 30, 35, 40, 45],
    "Salary": [25000, 30000, 50000, 70000, 90000, 120000]
}

df = pd.DataFrame(data)
plt.figure()
plt.hist(df["Salary"], bins=5)
plt.title("Salary Before Scaling")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

standard_scaler = StandardScaler()
df["Salary_Standardized"] = standard_scaler.fit_transform(df[["Salary"]])

plt.figure()
plt.hist(df["Salary_Standardized"], bins=5)
plt.title("Salary After Standardization")
plt.xlabel("Standardized Salary")
plt.ylabel("Frequency")
plt.show()

minmax_scaler = MinMaxScaler()
df["Salary_Normalized"] = minmax_scaler.fit_transform(df[["Salary"]])

plt.figure()
plt.hist(df["Salary_Normalized"], bins=5)
plt.title("Salary After Normalization")
plt.xlabel("Normalized Salary")
plt.ylabel("Frequency")
plt.show()

print(df)