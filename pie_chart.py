import matplotlib.pyplot as plt

roles = [    
    "Front-end", 
    "Back-end",
    "Full-stack",
    "DevOps"
    ]

employees = [52,36,28,11]

##### - THIS GIVES BASIC PIE CHART -- #######
# plt.pie(employees, labels=roles) # label argument helps provide context & shows the names
# plt.title("Developer Roles")
# plt.show()


#### - THIS GIVES PIE WITH IT'S %'s - (doesn't add up to a full 100%, might be that.1 of decimal place is too small) -1f is to 1 decimal place, you can change to 2 decimal places if want e.g 2f#####
plt.pie(employees, labels=roles, autopct="%.1f%%") # Autopct gives %
# Explode 0.2 is the top bit of pie - the above is pushing that section out!!
plt.title("Developer Roles")
#


## - IF YOU WANT TO EXPLODE THE PIE  - #####
# plt.pie(employees, labels=roles, autopct="%.1f%%", explode =[0.2,0,0,0]) # # Explode 0.1 is the top bit of pie - the above is pushing that section out!!
# plt.show()


#### TO SAVE OUR PLOTS/CHARTS ######
plt.savefig("pie.png")
###** YOU MUST SAVE BEFORE YOU PRINT IT. ONCE YOU PRINT IT THEN GETS RID OF PIE ONCE YOU'VE SEEN IT!!
plt.show()

