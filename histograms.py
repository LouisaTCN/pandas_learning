import matplotlib.pyplot as plt

dev_ages=[
        45, 23, 57, 27, 37, 39, 61, 48, 23, 27, 
        59, 60, 28, 41, 25, 39, 22, 46, 48, 52, 
        38, 41, 52, 30, 46, 62, 25, 34, 52, 35, 
        48, 43, 21, 40, 22, 22, 57, 25, 21, 30, 
        55, 50, 54, 30, 43, 40, 53, 46, 36, 61, 
        35, 39, 40, 31, 29, 65, 28, 57, 39, 36, 
        20, 49, 42, 29, 62, 52, 29, 57, 39, 32
        ]

#By default histogram gives you 10 bars
plt.hist(dev_ages, edgecolor="black")
plt.show()

## Doesn't look nice as grouping by 4.5's - to find out how to change find out lenght of data and range of data so we can amend;
print(len(dev_ages)) # gives lengh of data
#To work out the range;
dev_ages.sort()
print(dev_ages[0]) # print lowest value
print(dev_ages[-0])# print last value

#We can specify the bin sizes ourselves so looks nicer - accress teh same range we've reduced it stepping by 5's with total of 9 bins
plt.hist(dev_ages, edgecolor="black", bins=[20,25,30,35,40,45,50,55,60])
# plt.show()

