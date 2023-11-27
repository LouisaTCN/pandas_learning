import matplotlib.pyplot as plt
import numpy as np

##STANDARD FORMAT##
##plt.scatter(number_of_placements, responses_received)
##plt.show()

# number_of_placements=list(range(1,11))
# responses_received = [14, 21, 34, 36, 45, 51, 54, 63, 78, 92] # Advertising in 1 place = 14, advertising in 2 places 21 etc
# plt.scatter(number_of_placements, responses_received)
# plt.title("Job Posting Junior Dev Role")
# plt.xlabel("Number of Places Advertised")
# plt.ylabel("Responses Received")
# plt.show()

##To Create line of best fit - need to implment an array (YOU HAVE TO HAVE NUMPY INSTALLED!)
number_of_placements=np.array(range(1,11))
responses_received = np.array([14, 21, 34, 36, 45, 51, 54, 63, 78, 92])
plt.scatter(number_of_placements, responses_received)
plt.title("Job Posting Junior Dev Role")
plt.xlabel("Number of Places Advertised")
plt.ylabel("Responses Received")
#plt.show()


m,c =np.polyfit(number_of_placements, responses_received, 1) #we can work out the scope of the line with polyfit()
# plt.show()
plt.plot(number_of_placements, m*number_of_placements+c) #plot method to plot the line. the second argument is the equation mx+c - PLOTS THE LINE
plt.show()
# A line of best fit is reregssesion. Regession is the process of estimating beween 2 variables & see if there is a relationship


