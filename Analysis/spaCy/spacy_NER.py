# Basic Named Entity Recognition (NER) on raw text using SpaCy library

#spacy
import spacy
from spacy.attrs import ORTH, LIKE_URL, IS_OOV, NORM
import operator
from operator import itemgetter
from collections import OrderedDict

# read in data
with open("sb-content.txt","r") as f:
  data = f.read() # type 'string'

# tokenize input data
nlp = spacy.load("en")
d = data.decode('utf-8')
doc = nlp(d) #tokens


# extract named entities
ents = list(doc.ents)

# create list of unique entities and print list
unique = []
for e in ents:
  e = str(e)
  if e not in unique:
    unique.append(e)
for u in unique:
  print u

#count up entity frequencies and sort list in ascending order by value
# counts = {}
# for e in ents:
#   e = str(e)
#   if e in counts.keys():
#     counts[e] += 1
#   else:
#     counts[e] = 1
#
# d_sorted_by_value = OrderedDict(sorted(counts.items(), key=lambda x: x[1], reverse=True))
#
# for k, v in d_sorted_by_value.items():
#   print "%s: %s" % (k, v)
