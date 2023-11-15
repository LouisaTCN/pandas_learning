import pandas as pd
import numpy as np

languages = pd.Series(['Python', 'JavaScript', 'HTML', 'SQL'])
print(languages)

ranking = pd.Series([3, 1, 2, 4])
print(ranking)

#DF is data frame

# df = pd.DataFrame([("Anne", 30), ("Bill", 27), ("Charlie", 55)])
# print(df)
# # The above creates a data frame. The list had 3 Tuples within in. It creates a column table

# df=pd.DataFrame([("Anne", 30), ("Bill", 27), ("Charlie", 55)], columns = ["Name", "Age"])
# print(df)
# # overwritten line 10 with this so that it adds in column names



#To make data frame from exisiting series
#Key is column name and Value is the series
# Below is creating a dictionary
df = pd.DataFrame({
    "Languages" : languages,
    "Ranking" : ranking

})
print(df)

# df = pd.concat([languages, ranking], axis = 1) 
# df.columns=["Languages", "Ranking"]
# print(df)
# # NOTE: axis = 1 puts them next to each other, axis=0 would stack on top of each other
# # NOTE: .columns makes it give header names
# ## Would use .concat if bringing/linking many data series. The other way is easier



#-----------------------------------------------------------------------
#                 AMENDING A DATA SERIES/STRUCTURE
#-----------------------------------------------------------------------

#-----------------------------------------------------------
# ~AMENDING A DATA LINE, AND ADDING TO IT~


df.loc[4] = ['PHP', 11]
print(df)
# this adds new information into to my list. Adding PHP, and telling it which postion (4)

# #ANOTHER way is to use .concat
# new_data=pd.DataFrame({"Languages": ["PHP"], "Ranking":[11]})
# df=pd.concat([df, new_data], ignore_index=True)
# print(df)
# # this adds 2 frames together. However, keeps the labels, so PHP would be index postion 0
# # so added ignore index, and this then creates a new ranking combining both, so PHP would be index position 5

#Activity 1
df.loc[6] = ['Jarva', 7]
df.loc[7] = ['TypeScript', 5]
print(df)
# df.loc[6] is the location number on the list e.g. Jarva added in to row 6 and ranking number is Jarva = 7

# To expand with columns! Could you concatenation
#We can assign data a new column in list
df["Ranking 2022"]=[4,1,2,3,10,6,5]
print(df)

#Activity 2
#'JavaScript', 'HTML', 'SQL', Jarva & Type Script
   
df["Ranking 2020"]=[4,1,2,3,10,6,5]
df["Ranking 2019"]=[4,1,2,3,10,6,5]
print(df)
# this has added column 2020 and 2019 with it's given ranking values

#--------------------------------------------------------------------
  #ADDING NEW COLUMN IN A SPECIFIC PLACE
#--------------------------------------------------------------------- 
# Missed adding 2021 so need to add in for a specific place

df.insert(3, "Ranking 2021", [3, 1,2,4,11,5,7])
print (df)
# Puts the new column in place 3

#print(df.columns)- This would print the header titles (doesn't give header numbers e.g. 1,2)

df.loc[3.5] = ["Louisa Added Row", 1,2,3,4,5] # This would add a new row in between 3&4

df = df.sort_index() #- This would sort rows by their index position
print(df)

#---------------------------------------------------------------------
     # ACCESSING A DATA STRUCTURE #
#----------------------------------------------------------------------

#To see how big the data is (size of data)
print(df.shape) # this will give number of rows, and number of columns

print(df.columns) #This would print the header titles (doesn't give header numbers e.g. 1,2)

print(df["Ranking 2022"]) # Just return info from that column
print(df[["Ranking 2022", "Ranking 2021"]]) #Double brackets as printing 2 columns info


print(df.loc[4]) # This would print info from row 4 (index position 4)

print(df.loc[:, "Ranking 2020"])
print(df.loc[4, "Ranking 2020"]) # just gives info from row 4 of Ranking 2020
print(df.loc[4:7, "Ranking 2020"]) # just gives info from rows 4 to 7 of Ranking 2020

#Activity 3
print(df.loc[0:3,"Languages":"Ranking 2020":2])
# Start at row 0 to 3 of Languages. Then go to Ranking 2020 column and goes by 2 steps (so misses 2021)
#THIS IS DONE BY: 'row' Start, Stop, Step & 'column' Start, Stop, Step is the above


print(df.columns.get_loc("Ranking 2022")) 
#This shows you the column number e.g. Ranking 2022 is the 2nd column


#-------------------------------------------------------------------
            #Selecting Data Bases on a Condition#

##print(df[df<4]) # this wouldn't work as String and Interger
# So, to only look at intergers:
print(df[df.select_dtypes(include="int") >4])
# > is a comparison operator!

#NaN means NOT a Number
#When we do a comparison, the cells are evaluated to True or False (False is not a number!)
#True allows us to see the matching results, False would show as False = NaN for this

