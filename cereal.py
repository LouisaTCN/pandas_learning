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
*! ##index_of_bran_flakes = df.index.get_loc("Bran Flakes")
*! ##print(index_of_bran_flakes)
print(df.values["Bran Flakes"])

print(df.loc[4:7, "Ranking 2020"]) # just gives info from rows 4 to 7 of Ranking 2020