import urllib2
import time
from bs4 import BeautifulSoup as bsoup
from bs4 import BeautifulSoup
import requests as rq
import re
import unicodedata
import sys

#write article urls to textfile
all_text = ""
secretURLs = []
with open("tp-333.txt", "r") as file:
  data = file.read()
  url_list = data.split('\n')
  
  for x in url_list: #change range to e.g. [0:2] to test

    html_doc = urllib2.urlopen(x).read()
    soup = BeautifulSoup(html_doc, "lxml")

    #get title
    # title = soup.find('div', attrs={"class": "boxshadow  "})
    # title = str(title)
    # t_start = title.find('<h1>')
    # t_end = title.find('</h1>')
    # print title[t_start + 4 :t_end]

    #get author
    try:
        # author = soup.find('span', attrs={"id": "techauth"})
        # author_name = author.text + ' '
    
        # get article content
        content = soup.find('div', attrs={"id": "story-content"})
        text = content.text

        # str_text = unicodedata.normalize('NFKD', text).encode('ascii','ignore')
        # all_text += author_name
        # all_text += text
        # all_text = unicodedata.normalize('NFKD', all_text).encode('ascii','ignore')
        # print 'Success: ', x

    except:
        # print 'This article has no techauth tag'
        secretURLs.append(x)
        # author_name = ''
        text = ''
        pass

    # author = str(author)
    # a_start = author.find('">')
    # a_end = author.find('</a>')
    #print author[a_start+3:a_end]
    
    # # get article content
    # content = soup.find('div', attrs={"id": "story-content"})
    # text = content.text

    # content = str(content)
    # soup2 = BeautifulSoup(content, "lxml")
    # text = soup2.get_text()

    #str_text = unicodedata.normalize('NFKD', text).encode('ascii','ignore')
    # auth_name = unicodedata.normalize('NFKD', author_name).encode('ascii','ignore')
    txt = unicodedata.normalize('NFKD', text).encode('ascii','ignore')
    # print author_name
    print txt

    # all_text += author_name
    # all_text += text
    #all_text = unicodedata.normalize('NFKD', all_text).encode('ascii','ignore')
    #print 'Success: ', x
 
# with open("tp0_content.txt", "w") as outfile:
#   outfile.write(all_text)

# with open("tp0_secretURLs.txt", "w") as outfile:
#   outfile.write(secretURLs)    

#print secretURLs

