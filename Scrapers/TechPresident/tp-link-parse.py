import urllib2
import time
from bs4 import BeautifulSoup as bsoup
from bs4 import BeautifulSoup
from yaml import load, Loader
import requests as rq
import re


#get contents of Tech President's archives
base_url = "http://techpresident.com/blog"

r = rq.get(base_url)
soup = bsoup(r.text, "lxml")

page_count_links = soup.find_all("a",href=re.compile(r".*javascript:goToPage.*"))
try: # Make sure there are more than one page, otherwise, set to 1.
    num_pages = int(page_count_links[-1].get_text())
except IndexError:
    num_pages = 357 #1411 pages #1071 / 3 = 357

url_list = ["{}?page={}".format(base_url, str(page + 1054)) for page in range(1, num_pages + 1)]
#340 + 357 = 697
#697 + 357 = 1054


article_links = []
# loop through p. 341 ~ 1411 and grab partial article links
for url in url_list:
  html_doc = urllib2.urlopen(url).read()
  soup = BeautifulSoup(html_doc, "lxml")
  contents = soup.findAll('div', attrs={"class": " technewsfeat-wrapper boxshadow"})
  
  #grab inner html with partial links
  for c in contents: #10 article links per page
    piece = c.find('h4')
    piece = str(piece)

    #grab partial links
    start = piece.find("/") #index of this
    end = piece.find('">')
    #inner = piece[start:end]

    #construct full links
    full_link = "http://techpresident.com" + piece[start:end]
    
    article_links.append(full_link)

# print article_links

#write article urls to textfile
with open("techpres_links.txt", "w") as outfile:
  for x in article_links:
    outfile.write(x + '\n')
