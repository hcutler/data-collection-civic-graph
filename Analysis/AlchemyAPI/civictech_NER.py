from alchemyapi import AlchemyAPI
import json
import requests
import pprint

alchemyapi = AlchemyAPI()

pp = pprint.PrettyPrinter(indent=4)

#list of files containing all content pulled from Civicist and TechPresident (not uploaded to GitHub)
# files = ['tp0_content.txt',
        # 'tp06_content.txt',
        # 'tp05_content.txt',
        # 'tp75_content.txt',
        # 'tp95_content.txt',
        # 'tp1_content.txt',
        # 'tp11_content.txt',
        # 'tp111_content.txt',
        # 'tp2_content.txt',
        # 'tp21_content.txt',
        # 'tp22_content.txt',
        # 'tp222_content.txt',
        # 'tp2222_content.txt',
        # 'tp3_content.txt',
        # 'tp33_content.txt',
        # 'tp333_content.txt',
        # 'all_content-CIVICIST.txt']

for f in files:
  with open(f, "r") as file:
    data = file.read()
    myText = data

    print "ANALYSIS FOR " + f + " \n"

    # extract keywords
    # kr_0 = alchemyapi.keywords('text', test_text)
    # print "KEYWORDS: \n"
    # pp.pprint(kr_0)

    # extract taxonomy
    # tr_0 = alchemyapi.taxonomy('text', myText)
    # pp.pprint(tr_0)

    # extract entities
    er_0 = alchemyapi.entities('text', myText)
    print "ENTITIES: \n"
    for i in range(0, 50):
      pp.pprint(er_0['entities'])
      print(er_0['entities'][i]['text'])
      print(er_0['entities'][i]['relevance'])
      print(er_0['entities'][i]['type'])
      print(er_0['entities'][i]['count'])
      print '\n'

    # extract categories
    # cr_0 = alchemyapi.category('text', myText)
    # pp.pprint(cr_0)


    # extract concepts
    # cr_0 = alchemyapi.concepts('text', myText)
    # pp.pprint(cr_0)

    # sentiment analysis
    # sr_0 = alchemyapi.sentiment('text', myText)
    # pp.pprint(sr_0)
