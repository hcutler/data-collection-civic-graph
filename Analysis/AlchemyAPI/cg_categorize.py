from alchemyapi import AlchemyAPI
import json
import pprint

#Reads in file containing names of entities in Civic Graph and their associated descriptions
#Attempts to categorize entities in Civic Graph based on descriptions using AlchemyAPI's "category" function

alchemyapi = AlchemyAPI() # API Key: ff8f993db5ee0b907a3e41f19bbd57b8b4cbc24a


pp = pprint.PrettyPrinter(indent=4)

#Read in data
myText = ""
with open("cg_entities_and_descr.csv", "r") as file:
  data = file.read()
  myText = data.split()
  print type(myText)
  print myText


#categorize entities in Civic Graph based on their descriptions (data = 'text')
for i in range(0, len(lis)):
  categ_result = alchemyapi.category('text', entities[i]);
  pp.pprint(categ_result)
  i += 1

#Test API call
# categ_result = alchemyapi.category('text', "http://techpresident.com/news/25496/first-post-data-driven");
# pp.pprint(categ_result['category'])






