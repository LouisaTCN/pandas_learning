import matplotlib.pyplot as plt

years = [2018, 2019, 2020, 2021, 2022, 2023]
python_position = [7,4,4,3,4,3]
javascript_position = [1,1,1,1,1,1]
SQL_position = [4,3,3,4,3,4]
Typescript_posiiton = [12,10,9,7,5,5]


plt.plot(years, python_position) # On plot object, plot years and pythons position - X  
plt.title("Most-Wanted Language Ranking")
plt.xlabel("Year")
plt.ylabel("Postion")
plt.ylim(bottom=12, top=0)
plt.plot(years, javascript_position) # added Javascript position back up on row 5 - this just makes it add to graph
plt.plot(years, SQL_position)
plt.plot(years, Typescript_posiiton)


# plt.legend([ #Creates a legend
#     "Python",
#     "JavaScript",
#     "SQL",
#     "Typescript"
# ])
# #plt.show() 

# ANOTHER way to add a legend is - BETTER AS YOU CAN CHANGE LINE COLOUR:
# plt.plot(years,python_position,label = "Python")
# plt.plot(years, javascript_position,label = "Javascript")
# plt.plot(years, SQL_position,label = "SQL")
# plt.plot(years, Typescript_posiiton,label = "Typescript")
#plt.legend() #This tells it to add the legend as per above

#** To Change line styles;
#- this is defined with the linestyle argument
plt.plot(years,python_position,label = "Python") # defaults to a solid line
plt.plot(years, javascript_position,label = "Javascript", linestyle ="dashed")
plt.plot(years, SQL_position,label = "SQL", linestyle ="dotted")
plt.plot(years, Typescript_posiiton,label = "Typescript", linestyle ="dashdot")
plt.legend() #This tells it to add the legend as per above
plt.show()

# ------########## -  THIS IS SAME AS ABOVE BUT JUST WITH COMMENTS FOR INFO ---  #######
# python_position = [7,4,4,3,4,3]
# javascript_position = [1,1,1,1,1,1]


# plt.plot(years, python_position) # On plot object, plot years and pythons position - X Axis is alway 1st
# # plt.show() # Telling it to show it to us - Basically printing the graph by 'Show'. ALWAYS LAST THING!

# # This gives back a LINE GRAPH
# #- NO TITLE
# # - NO LABELS ON AXIS
# # LINE DECSCENDS WHEN SHOUDL ACEND

# # THE title() method allows up to assign a title to a plot
# plt.title("Most-Wanted Language Ranking")

# # THE xlabel() & ylabel() methods allow us to label axes
# plt.xlabel("Year")
# plt.ylabel("Postion")

# # Change descending axis line e.g. 1 is good & 10 is bad - 
# # The ylim() method allows us to set the limits for the y-axis by giving it 2 limits. Top limit & bottom limit
# plt.ylim(bottom=10, top=0)

# #To add 2nd data set e.g add JavaScript to popularity against Python
# # .plot()  allows you to update it;
# plt.plot(years, javascript_position) # added Javascript position back up on row 5 - this just makes it add to graph

# To create a legend
#plt.legend() is a method which allow su to create a key for our data
# plt.legend([
#     ~Python",
#     "JavaScript",
#     "SQL",
#     "Typescript"
# ])

#ANOTHER way to add a legend is:
#plt.plot(years,pthyon_position,label = "Python")
#plt.plot(years, javascript_position,lable = "Javascript")
# ## ---------------------END OF COMMENTS FOR ABOVE -------------------------####



##Challenge 1 - SCREENTIME
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
youtube_hours = [2,1,3,6,3]
twitter_hours = [1,1,0,0,2]
whatsapp_hours = [3,1,0,2,1]
raid_shadow_legends_hours = [0,4,2,3,3]
tiktok_hours = [3,0,1,0,2]

plt.plot(days,youtube_hours,label = "YouTube", marker ='*', color='red') # defaults to a solid line
plt.plot(days, twitter_hours,label = "Twitter", linestyle ="dashed", marker='o', color='green')
plt.plot(days, whatsapp_hours,label = "WhatsApp", linestyle ="dotted", marker='s', color='black')
plt.plot(days, raid_shadow_legends_hours,label = "Raid:Shadow Legends", linestyle ="dashdot", marker='D', color='pink')
plt.plot(days, tiktok_hours,label = "TikTok", linestyle ="dashdot", marker='^', color='blue')
##  marker styles such as 'o' (circle), 's' (square), '^' (triangle), 'D' (diamond), '*' (star) ##
plt.legend() #This tells it to add the legend as per above
plt.title("Screen-Time")
plt.xlabel("Days")
plt.ylabel("Hours")
plt.ylim(bottom=0, top=7)

plt.show()