import requests
from lxml import html
import random
# This section saves a template wikipedia url that will be modified by the user to a specific year
url = "https://en.wikipedia.org/wiki/"
year = input("Pick a year from 1 to the present, and I'll tell you something that happened that year: ")
# Because of the way wikipedia structures their url's certain dates have AD_ before the year, and this
# line accounts for that
if int(year) <= 150 or int(year) == 1000 or int(year) == 500:
    year = "AD_"+year
# the following line combines the template url with the year the user has input
url = f'{url}{year}'
page = requests.get(url)
tree = html.fromstring(page.content)
# using xpath, this grabs only the section of the page that contains dates and events
dates_section = tree.xpath('//span[@id="Events"]/following::ul[1]//li')
if len(dates_section)>0:
    # This segment basically just clean up the string to eliminate the "[1]"s and other artifacts that wikipedia
    # uses to link to sources.
    random_date = dates_section[random.randint(0,len(dates_section)-1)].text_content()
    last_period_index = random_date.rfind('.')
    if last_period_index>0:
        random_date = random_date[:last_period_index+1]
    print(random_date)
# some years did not have anything notable in the events section and I check for that by printing the following
# statement when the "date_section" list does not have any elements.
else: print("I was unable to find anything notable that happened that year.")


