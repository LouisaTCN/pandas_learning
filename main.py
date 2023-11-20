from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

html_text=requests.get("https://www.scrapethissite.com/pages/simple/").text #text was added after from DIR
print(html_text)
#.get makes is web scraper.
#however, BeautifulSoup refines it!

print(dir(html_text))
#Makes a property of the directory of HTML text - shows you the property info. eg. Text
#You can then change

print(html_text)
#Makes a property of the directory of HTML text - shows you the property info. eg. Text
#You can then change to just show text:
#by adding Text to line 5.
# this then returns just the text info

souped_html = BeautifulSoup(html_text, "lxml")
#soupled html is now the new category from Beautiful Soup* (can then use find and find all)

# in Country files all the countries are under 'h3' - found by using INSPECT on W.Site.
countries = souped_html.find_all('h3')
print(countries)

for country in countries:
    print(country.text.strip())
#this just returns the countries names
# adding.strip takes away the big blank spaces between countries


#Create DataFrame from the scraped list
df=pd.DataFrame([country.text.strip() for country in countries]) # list comprehension, creating a new list from an old list
print(df)


#To add in further info e.g. Captipal, Population & Area - check inspect to see what is on website classed as
#can include class to filter

country_capitals = (souped_html.find_all('span', class_="country-capital"))
#span keeps in line rather than seperate lines
for capital in country_capitals:
    print(capital.text.strip())

country_populations = (souped_html.find_all('span', class_="country-population"))
#span keeps in line rather than seperate lines
for population in country_populations:
    print(population.text.strip())

country_areas = (souped_html.find_all('span', class_="country-area"))
#span keeps in line rather than seperate lines
for areas in country_areas:
    print(areas.text.strip())

#To make data frame from exisiting series
#Key is column name and Value is the series
# Below is creating a dictionary
countries_series= pd.Series([country.text.strip() for country in countries])
capitals_series = pd.Series([capitals.text.strip() for capitals in country_capitals])
populations_series = pd.Series([population.text.strip() for population in country_populations])
areas_series = pd.Series([area.text.strip() for area in country_areas])
print(areas_series)

df = pd.DataFrame({
    "Countries" : countries_series,
    "Capitals" : capitals_series,
    "Populations" : populations_series,
    "Areas" : areas_series
})
print(df)

#DataFrame created and now to save to Excel;
#** In terminal enter: pip install openpyxl
df.to_excel("output.xlsx")

