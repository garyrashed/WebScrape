

##Getting a list of all cities in Bergen County
#
#target: https://www.cleargov.com/new-jersey/bergen
#

import bs4 as bs
import urllib.request
citiesPage = urllib.request.urlopen('https://www.cleargov.com/new-jersey/bergen').read()
cleanCitiesPage = bs.BeautifulSoup(citiesPage, 'lxml')


### Rats, it's a dynamic page. Time for selenium!!
#Downloaded Selenium and Chrome Driver. (See ChromeDriverTest)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/Users/Gary/Downloads/chromedriver_win32/chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://www.cleargov.com/new-jersey/bergen')
citiesWebElement = driver.find_elements_by_class_name('municipality-name')
citiesStrings = [x.text for x in citiesWebElement]
print(citiesStrings)
driver.close()
driver.quit()

### Write the cities somewhere or save them to a database?
### I made this a bit complicated to handle blank lines.
import csv
with open ('bergenCities.csv', 'w') as bergenCities:
    for cityCounter in range(0, len(citiesStrings)):
        if(cityCounter != (len(citiesStrings) - 1)):
            bergenCities.write('{item}\n'.format(item=citiesStrings[cityCounter]))
        else:
            bergenCities.write('{item}'.format(item=citiesStrings[cityCounter]))


### Now onto the listings page
### Pattern: https://www.loopnet.com/new-jersey/hackensack-commercial-real-estate/
### Pattern: https://www.loopnet.com/new-jersey/<city>-commercial-real-estate/
### Pattern: Note that you have to replace spaces in the city name with hyphens

###Create scrappy project
### To be done in command prompt
### scrapy startproject LoopNetCrawler

#create a starting urls file from the citys

with open ('bergenCities.csv', 'r') as targetCities:
    cities = list(map(lambda x: x.strip().replace(' ', '-').lower(), targetCities.readlines()))

citiesURL = list(map(lambda x: "http://www.loopnet.com/new-jersey/{0}-commercial-real-estate".format(x), cities))

print(citiesURL)
