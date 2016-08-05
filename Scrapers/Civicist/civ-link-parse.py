import urllib2
import time
from bs4 import BeautifulSoup as bsoup
from bs4 import BeautifulSoup
from yaml import load, Loader
import requests as rq
import re

#get contents of Civicist archives
base_url = "http://civichall.org/civicist-archives/"

r = rq.get(base_url)
soup = bsoup(r.text, "lxml")

page_count_links = soup.find_all("a",href=re.compile(r".*javascript:goToPage.*"))
try: # Make sure there are more than one page, otherwise, set to 1.
    num_pages = int(page_count_links[-1].get_text())
except IndexError:
    num_pages = 48 #48 pages

url_list = ["{}page/{}".format(base_url, str(page)) for page in range(1, num_pages + 1)]

url_list.remove('http://civichall.org/civicist-archives/page/1')


url_list.insert(0, "http://civichall.org/civicist-archives")

article_links = []

for url in url_list:
  html_doc = urllib2.urlopen(url).read()
  soup = BeautifulSoup(html_doc, "lxml")
  contents = soup.findAll('h2', attrs={"class": "post-title"})
  for link in contents:
    #x = re.search("(?P<url>https?://[^\s]+)", str(link).group("url"))
    link = str(link)
    start = link.find("http") #index of this
    end = link.find('/">')
           
    # print link[start:end]
    article_links.append(link[start:end])

#write article urls to textfile
with open("article-links-extra.txt", "w") as outfile:
  for x in article_links:
    outfile.write(x +'\n')


# print article_links

