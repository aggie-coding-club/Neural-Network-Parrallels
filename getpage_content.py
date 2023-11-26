from bs4 import BeautifulSoup

import requests

from google_scrape import links_list, pages, titles

#url = "https://www.theadvertiser.com/story/sports/college/lsu/2023/11/25/lsu-football-texas-am-live-score-updates-highlights-tiger-stadium/71614503007/"


def get_page_text(url):

    page = requests.get(url)
    content =[]

    soup = BeautifulSoup(page.content, "lxml")

    for text in soup.find_all("p")[:10]:
        stuff = text.text
        content.append(stuff)
    
    return content

print(links_list[8:12])     


#me = soup.find("div", id= "contentHolder")
txt = 0
try:
    for link in links_list[5:20]:
        link_content = get_page_text(link)

        with open('pagecontents/page{}content'.format(txt), 'w') as file:
            for i in range(0, len(link_content)):
                file.write(link_content[i])

        txt+=1
except:
    pass


