import matplotlib.pyplot as plt


advertising_locations =[
    "Twitter",
    "Facebook",
    "LinkedIn",
    "Indeed",
    "Instagram"
]

responses = [3,11,16,13,2]

plt.bar(advertising_locations, responses)
bars = plt.bar(advertising_locations, responses) # this is same as above line but so you can highlight a colour
bars[2].set_color('Red') # this adds the colour to bar 3 - index starting at 0 - so LinkedIn done colour change


plt.title("Return from Job Posting by Location")
plt.xlabel("Advert Location")
plt.ylabel("Applications Received")
plt.show()

##Hero Bar - we can highlight a bar if necessary so it stands out
## - by saving the plot to a variable we can weasily reference the index positon of thete bar & use .set_colour() method to change iter
## - bars = plt.bar(advertising_locations, responses)
## - bars[2].set_colour('Red')
