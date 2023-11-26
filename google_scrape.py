import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
# google search web scraping


search_engine = "https://google.com/search?q="
# this is what the program will seach up using google
query = 'When will the aggies play football again'

search = search_engine + query # the search url

options = webdriver.ChromeOptions()
options.add_argument('--headless')
# making browser headless


driver = webdriver.Chrome(options=options)
# creating my browsing object
links_list = []
pages = []
titles = []
def search_links(search):

   driver.get(search) # loads webpage in headless browser

   ini_height = driver.execute_script("return document.body.scrollHeight")
   # Scrolls to bottom of page since google adds more when you scroll down
   while True:
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
      time.sleep(1)

      new_height = driver.execute_script("return document.body.scrollHeight")

      if new_height == ini_height:
         break
      ini_height = new_height


   page = driver.page_source
   # retrieving my webpage and getting the html contents

   # google page 
   web_results = BeautifulSoup(page, "html.parser")


   
  
   # attempting to find the links of all the google recommeneded pages
   for result in web_results.find_all("div", class_="MjjYud"):
      try:
         melink = result.find('a', href=True)
         mepage = result.find('span', class_='VuuXrf')
         metitle = result.find('h3', class_='LC20lb MBeuO DKV0Md')
         if metitle == None:
            metitle = result.find('div', class_='n0jPhd ynAwRc tNxQIb nDgy9d')  
         if mepage == None:
            mepage = result.find('div', class_='MgUUmf NUnG9d')
         link = melink['href']
         if(str(link).startswith('/search?')):
            continue
         
         links_list.append(link)
         pages.append(mepage.text)
         titles.append(metitle.text)
         
         
      except TypeError:
         print("Must not have a link")
      except AttributeError:
         print("does not have a title with same class")
      
for i in range(0, len(links_list)):
   page_dict = {'page title': titles[i], 'link': links_list[i], 'page': pages[i]}





# ignore for now

#search_page = requests.get(search)
#search_page = ''
# manages and limits requests rates.
#while search_page == '':
  #  try:
   #     search_page = requests.get(search)
   #     break
   # except:
   #     print("Connection refused by the server..")
   #     print("Let me sleep for 5 seconds")
    #    print("ZZzzzz...")
    #    time.sleep(5)
    #    print("Was a nice sleep, now let me continue...")
    #    continue