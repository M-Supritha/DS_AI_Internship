import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

heights = np.random.normal(loc=170, scale=10, size=1000)

incomes = np.random.exponential(scale=50000, size=1000)

scores = np.random.beta(a=5, b=1, size=1000) * 100

df = pd.DataFrame({
    "Heights": heights,
    "Incomes": incomes,
    "Scores": scores
})

def analyze_distribution(data, title):
    
    mean_value = np.mean(data)
    median_value = np.median(data)
    
    plt.figure()
    sns.histplot(data, kde=True)
    
    plt.axvline(mean_value, linestyle='--', label=f"Mean: {round(mean_value,2)}")
    plt.axvline(median_value, linestyle='-', label=f"Median: {round(median_value,2)}")
    
    plt.title(title)
    plt.legend()
    plt.show()
    
    print(f"{title}")
    print(f"Mean   = {mean_value:.2f}")
    print(f"Median = {median_value:.2f}")
    
    if mean_value > median_value:
        print("Right-Skewed Distribution\n")
    elif mean_value < median_value:
        print("Left-Skewed Distribution\n")
    else:
        print(" Approximately Normal Distribution\n")

analyze_distribution(df["Heights"], "Human Heights (Normal)")
analyze_distribution(df["Incomes"], "Household Incomes (Right-Skewed)")
analyze_distribution(df["Scores"], "Easy Exam Scores (Left-Skewed)")
