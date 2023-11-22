import pandas as pd
import numpy as np

df = pd.read_excel("first_hour_sales.xlsx")
print(df)

#To change index, so that Transation ID becomes Index (now row index)
df = df.set_index("Transaction ID")
print(df)

#---------------------------------------------------------------------
#         GETTING RID OF DATA YOU DON'T NEED (from spreadsheet) 
#----------------------------------------------------------------------

#DROP (get rid of column - there are 2 ways);
df = df.drop("Till ID", axis=1)
df = df.drop(columns=["Staff ID"]) # This does the same thing, just another way
print(df)

#DROP to remove rows (we can target them via index)
df = df.drop([16, 17,18]) #Drops ID's 16, 17 & 18
print(df)

# ## If you drop rows it doen't reset the number. You can change it by doing this;
# df = df.reset_index(drop=True)
# df.index=df.index.rename("Sales ID")



#Remove Duplicates;
# e.g. error - both lines called row 29 and are duplicate data
#drop_duplicates() will automatically search for dup rows and leaves 1 in (row after the first instance is removed)

df = df.drop_duplicates()
print(df)

## *** KATIE FINDING OUT HOW TO REMOVE BASED ON VALUE ***
#df = df.drop(df[df["Currency"]=='Credit].index) - removed the whole 'credits' from the 'Currency' column

#----------------------------------------------------------------------------------
#        OUTLIERS - SKEWS THE DATA (e.g. 2yr old submitting data)
#          IF YOU KNOW IS A MISTAKE - DELETE IT!        

#         TRUE OUTLIERS are genuine data points - Should be left in! (e.g. huge salary)
#          Take Stats with TRUE OUTLIER, AND Stat without TRUE OUTLIER - Then choose best result (e.g. remove salary to give more accurate salary bands)

##--------------------------------------------------------------------------------------


print(df["Amount"].mean())
print(df["Amount"].mode())
print(df["Amount"].median())
#this shows the median is £3.10, so transaction 12 at £31 is wrong

##TO CHANGE A SINGLE CELL - Argument is [row, column]
df.at[12,"Amount"]= 3.10 #This changes the 'Amount of row 12 to £3.10
print(df)

#-------------------------------------------------------------------------
##                  COLUMN WIDE CLEANING
###  ----------------------------------------------------------------------
              
#TO CHANGE WHOLE TIME COLUMN TO HH:MM (it was 9.28 - floating point)
### APPLY() method allows us to perform a function on a value

# for every float: THIS IS WHAT WE NEED TO DO TO GET 9.28 INTO HH:MM FORMAT
#      #- turn it into a String
#      # - swap the. for a :
#     #- add a zero at the Start
#     #- add 0 at end if needs be
#     # to put in string cast!

def float_to_time(stamp):
    stamp = str(stamp) # turns into a string
    stamp = stamp.replace(".",":") # replaces . to :
    stamp = "0" +stamp #adds 0 at the start - only works at current data is only till 9.30 - wouldn't work for 10am
    if len(stamp) !=5: #NEEDS TO BE 5 AS HH:MM
        stamp = stamp +"0" #if wasn't 5, would make it 5
    return stamp #Returns the stamp value

def extract_time(stamp):
    stamp = stamp.time()
    return stamp

# THEN NEED TO UPDATE THE TIME COLUMN TO REFORMATTED VALUES - AS per above actions
df["Time"] = df["Time"].apply(float_to_time)
print(df)

# in expected format but still not yet the correct data type - Data is showing as object
# can then use Panda to convert to date time (coudln't do without above as not in correct format)
df["Time"] = pd.to_datetime(df["Time"])

#**DATE/Time makes it give a date which would be date you did it!
# SO ADDED LINES 81 - 83 & 95 TO REMOVE THE DATE FROM THE ABOVE WORKINGS
df["Time"] = df["Time"].apply(extract_time)
print(df)



# ACTIVTIES:
# Work out the Average price of an item
# - Sum of all items sold
# - Sum of total vaule
total_amount = df['Amount'].sum()
total_items = df['Items'].sum()
print("Total Value Amount £: {total_amount:.2f}") # .2f rounds it to 2 decimal places
print("Total Items Sold:",total_items)
average_price = (total_amount/total_items)
print(f"Average Price £: {average_price:.2f}")

#Work out the Average basket price
# - Sum of all items sold
# - Sum of total number of transactions
total_amount = df['Amount'].sum()
total_transactions = df.shape[0] # this counts the number of rows by getting shape - count doesn't work as Transaction ID is not a column
print(f"Total Value Amount £:{total_amount:.2f}") # .2f rounds it to 2 decimal places
print("Total Transactions Made:",total_transactions)
average_basket_price = (total_amount/total_transactions)
print(f"Average Basket Price £: {average_basket_price:.2f}")


# The max spend in one transaction
max_spend = df['Amount'].max()
print(f"Maximum Spend £: {max_spend:.2f}")# .2f rounds it to 2 decimal places


# The min spend in one transaction
min_spend = df['Amount'].min()
print(f"Minimum Spend £: {min_spend:.2f}")# .2f rounds it to 2 decimal places

# The most common spend amount
# - mode finds out the most common of something ('Amount' in this case)
most_common_spend = df["Amount"].mode().loc[0]#We add .loc[0] so it only gives back 1 series - mode will create 2 series by itself, so otherwise would show £ 0 2.85
print(f"The most common spend is £: {most_common_spend}")

# The most common payment type
# - mode finds out the most common of something ('Currency' in this case)
most_used_payment_type = df["Currency"].mode().loc[0] #We add .loc[0] so it only gives back 1 series - mode will create 2 series by itself, so otherwise would show £ 0  Debit
print(f"The most common payment type is: {most_used_payment_type}")
