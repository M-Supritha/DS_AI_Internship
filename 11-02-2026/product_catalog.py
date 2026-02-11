import pandas as pd
products = pd.Series([700, 150, 300], index= ['Laptop', 'Mouse', 'Keyboard'])
laptop_price = products['Laptop']
first_two_products = products.iloc[:2]
print("Full Products series:\n",products)
print("\nPrice Of laptop:",laptop_price)
print("\nFirst two products:\n",first_two_products)