import pandas as pd
import numpy as np
from collections import Counter
import ast

df = pd.read_excel("friday_data.xlsx")


df = df.set_index("Transaction ID", drop=True)
df = df.reset_index(drop=True)
df.index = df.index.rename("Transaction ID")

df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df = df.drop(columns=["Till ID"])

# df = df.drop([18])
df = df.dropna()

df.to_excel("output_friday.xlsx")
print(df)

# BEST SELLING ITEM:
# Convert string representations of lists to actual lists
df['Basket'] = df['Basket'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else [])
# Explode the 'Basket' column to transform lists into separate rows
exploded_df = df.explode('Basket')
# Find the most common/least common item
most_common_item = exploded_df['Basket'].mode().iloc[0]
least_common_item = exploded_df['Basket'].value_counts().idxmin()
print("Best selling item:", most_common_item)
print("Worst selling item:", least_common_item)



# Work out total income
# - Sum of all items sold
total_amount = df['Cost'].sum()
print(f"Total Daily Takings £{total_amount:.2f}") # .2f rounds it to 2 decimal places

# The highest spend 
max_spend = df['Cost'].max()
print(f"Highest Daily Spend £{max_spend:.2f}")# .2f rounds it to 2 decimal places

# The MVP staff member
# Identifies the daily MVP staff member based on the number of transactions
daily_mvp = df['Staff'].value_counts().idxmax()
print(f"The daily MVP staff member is: {daily_mvp}")

#Work out the Average basket price
# - Sum of all items sold
# - Sum of total number of transactions
total_cost = df['Cost'].sum()
total_transactions = df.shape[0] # this counts the number of rows by getting shape - count doesn't work as Transaction ID is not a column
average_basket_price = (total_cost/total_transactions)
print(f"Average Days Basket Price £{average_basket_price:.2f}")

