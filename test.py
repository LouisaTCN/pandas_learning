import matplotlib.pyplot as plt



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
