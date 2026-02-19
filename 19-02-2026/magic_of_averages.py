import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(42)
population = np.random.exponential(scale=50000, size=100000)
sample_means = []

for i in range(1000):
    sample = np.random.choice(population, size=30)
    sample_mean = np.mean(sample)
    sample_means.append(sample_mean)
df_means = pd.DataFrame({"Sample Means": sample_means})

plt.figure()
sns.histplot(df_means["Sample Means"], kde=True)
plt.title("Distribution of Sample Means (n=30, 1000 samples)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()
print("Original Population Mean:", np.mean(population))
print("Mean of Sample Means:", np.mean(sample_means))
