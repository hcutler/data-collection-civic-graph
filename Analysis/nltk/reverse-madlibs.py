import nltk
import csv
import sys
import itertools

#from pylab import *
# import matplotlib.pyplot as plt

#from nltk.book import *
# from __future__ import division

# nltk.download('maxent_ne_chunker')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('punkt')
# nltk.download('words')

tokens = []
sentences = []

with open("sample.txt","r") as f:
  data = f.read().decode('utf8') # type 'string'
  #tokens = nltk.word_tokenize(data)
  sentences = nltk.sent_tokenize(data)

# NER
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)
def extract_entity_names(t):
    entity_names = []


    if hasattr(t, 'label') and t.label:
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))

    return entity_names

ent_tuples = []
ent_list_by_sentence = []
entity_names = []
for tree in chunked_sentences:

    # Print results per sentence
    ent_list_by_sentence.append(extract_entity_names(tree))

for s in ent_list_by_sentence:
  #print s
  ent_tuples.append(tuple(itertools.combinations(s, 2)))
print '\n'
print 'Welcome to Civic Tech "Reverse-MadLibs"! \n'
print 'Your responses can help us better understand the relations between'
print 'individuals, companies, and organizations in civic tech.\n'
for t in ent_tuples:
  # response = raw_input("Please enter the relationship between")
  for pair in t:
    strpair = str(pair)
    response = raw_input("Please enter the relationship between " + strpair + ': \n')

    with open("relations.txt", 'a') as f:
      f.write(strpair + '\n' + response + '\n')

  # for ent in s:

  #   response = raw_input("Please enter the relationship between")
  #   print ent
  #   raw_input('Press enter to continue)

    #entity_names.extend(extract_entity_names(tree))

