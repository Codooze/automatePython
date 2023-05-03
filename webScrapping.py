#path syntax
#* //tagName[1]
#* //tagName[@attributeName='value']
#* //tagName[contains(@attributeName='value')]
#* //tagName[starts-with(@attributeName='value')]
#* //tagName[ends-with(@attributeName='value')]
#* //tagName[@attributeName='value' and @attributeName='value']
#* //tagName[@attributeName='value' or @attributeName='value']
#* //tagName[@attributeName='value' or @attributeName='value' and @attributeName='value']


#?Special characters

#* /: select the children from the node se on the left of this character
#* //: specifies that the matching node set should be located at any level within the document
#* .: select the current node
#* ..: select the parent of the current node
#* @: select attributes
#* *: select all elements in the document
#* []: select nodes based on a condition
#* ./*: select all child nodes of the current node
#* .//*: select all descendant nodes of the current node

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os
import sys

application_path = os.path.dirname(sys.executable) # to get the path of the python interpreter

now = datetime.now().strftime("%d-%m-%Y %H-%M-%S") # to get the current date and time

webside = "https://www.thesun.co.uk/sport/football"
path = r"C:\Users\jeyso\chromedriver_win32\chromedriver.exe"


# headless- mode

options = Options()
options.headless = True

service = Service(executable_path= path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(webside)

#? Automate The News - Finding Elements

containers = driver.find_elements("xpath", "//div[@class='teaser__copy-container']")

#// driver.find_elements("xpath", "//div[@class='teaser__copy-container']//h3")
#? //div[@class="teaser__copy-container" ]
#? //div[@class="teaser__copy-container" ]//h3
import pandas as pd

titles = []
subtitles = []
links = []
for container in containers:
   title = container.find_element("xpath", ".//h3").text
   subtitle = container.find_element("xpath", ".//p").text
   link = container.find_element("xpath", ".//a").get_attribute("href")
   titles.append(title)
   subtitles.append(subtitle) 
   links.append(link)

file_name = os.path.join(application_path, f"headline-{now}.csv")
pd.DataFrame({"title": titles, "subtitle": subtitles, "link": links}).to_csv(file_name, index=False)


driver.quit() # close the browser
#?  Automate The News - Preparing Script to Be Run Everyday
# pyistaller --onefile filename.py