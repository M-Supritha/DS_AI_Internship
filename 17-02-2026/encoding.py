import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {
    "Transmission": ["Automatic", "Manual", "Automatic", "Manual"],
    "Color": ["Red", "Blue", "Green", "Red"]
}

df = pd.DataFrame(data)

le = LabelEncoder()
df["Transmission_Encoded"] = le.fit_transform(df["Transmission"])

df_encoded = pd.get_dummies(df, columns=["Color"], drop_first=True)

print(df_encoded)