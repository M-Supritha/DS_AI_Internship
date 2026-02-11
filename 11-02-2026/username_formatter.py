import pandas as pd
usernames = pd.Series(['Alice','boB', 'Charlie_Data' , 'daisy'])
cleaned_usernames = usernames.str.strip()
cleaned_usernames = cleaned_usernames.str.lower()
contains_a = cleaned_usernames.str.contains('a')
print("Cleaned Usernames:\n", cleaned_usernames)
print("contains letter:\n", contains_a)