import pandas as pd
import numpy as np


df=pd.read_csv("cereal.csv")
print(df)


#Activities:
# - How many rows & columns?
print(df.shape)

# - What are the names of the columns?
print(df.columns)

# - Which cereals have more than 4g of protein?
cereals_more_than_4g_protein=df[df['protein'] >4]
#Created variable name 'cereals_more_than_4g_protein'.
#Told it to look at 'Protein' column
#Then to return values of protein that are higher than 4g
print(cereals_more_than_4g_protein)

# - Bring back all data relating to Bran Flakes
# To find out which row Bran Flakes is on
bran_flakes_data=df.loc[df["name"] == 'Bran Flakes']
#This is creating new data frame where it's pulling in the info relating to Bran Flakes
#== is telling it to only add in data frame if name is Bran Flakes 
print(bran_flakes_data)
