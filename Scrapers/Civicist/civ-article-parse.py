import urllib2
import time
from bs4 import BeautifulSoup as bsoup
from bs4 import BeautifulSoup
import requests as rq
import re
import unicodedata

#read article urls from textfile
all_text = ""
with open("summer-break.txt", "r") as file:
  data = file.read()
  url_list = data.split('\n')
  
  for x in url_list:
    html_doc = urllib2.urlopen(x).read()
    soup = BeautifulSoup(html_doc, "lxml")

    #get title
    title = soup.find('h1', attrs={"class": "post-title"})
    title = str(title)
    t_start = title.find('">')
    t_end = title.find('</')
    #print title[t_start+2:t_end]

    #get excerpt
    # excerpt = soup.find('p', attrs={"class": "post-excerpt"})
    # excerpt = str(excerpt)
    # e_start = excerpt.find('">')
    # e_end = excerpt.find('</')
    #print excerpt[e_start+2:e_end]

    #get author
    author = soup.find('span', attrs={"class": "post-author"})
    author = str(author)
    a_start = author.find('/">')
    a_end = author.find('</a>')
    #print author[a_start+3:a_end]
    
    #get date
    date = soup.find('span', attrs={"class": "post-date"})
    date = str(date)
    d_start = date.find('">')
    d_end = date.find('</span>')
    full_date = date[d_start+2:d_end]
    #print full_date

    # get bulleted content
    content = soup.find('div', attrs={"class": "entry"})
    content = str(content)
    soup2 = BeautifulSoup(content, "lxml")
    # text = soup2.p.contents
    text = soup2.get_text()
    str_text = unicodedata.normalize('NFKD', text).encode('ascii','ignore')
    all_text += text
    # print all_text
    all_text = unicodedata.normalize('NFKD', all_text).encode('ascii','ignore')

with open("sb-content.txt", "w") as outfile:
  outfile.write(all_text)

