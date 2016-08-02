from __future__ import unicode_literals

with open("sample.txt","r") as f:
  data = f.read() # type 'string'

#nltk
import nltk

#spacy
import spacy
from spacy.attrs import ORTH, LIKE_URL, IS_OOV, NORM
from spacy.parts_of_speech import *
import operator
from operator import itemgetter
from collections import OrderedDict

nlp = spacy.load("en")
d = data.decode('utf-8')
doc = nlp(d, tag=True) #tokenized doc

# -------

# Sentence Tokenization:

# -------

#(1) spaCy sentence tokenization
sentences = [sent.string.strip() for sent in doc.sents]

i = 1
for s in sentences:
  print '(' + str(i) + '): ' + s + '\n'
  i += 1

# -------

# (2) nltk sentence tokenization (very slow - don't use)
# sentences = nltk.sent_tokenize(data)
# tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

# for s in tokenized_sentences:
#   print 'nts: ' + ' '.join(s) + '\n'

# -------

#What is this stuff doing????????

#convert proper nouns (PROPN) to uppercase and print associated text
#print u''.join(tok.string.upper() if tok.pos == PROPN else tok.string for tok in tokens)
#print u''.join(tok.string.upper() + '\n' if tok.pos == PROPN else '' for tok in doc)


#convert adverbs (ADV) to uppercase and print associated text
# print u''.join(tok.string.upper() if tok.pos == ADV else tok.string for tok in tokens)


# -------

# Basic Named Entity Recognition (NER) on raw text using SpaCy library

#count up entity frequencies and sort list in ascending order by value
# ents = list(doc.ents)

# counts = {}
# for e in ents:
#   e = str(e)
#   if e in counts.keys():
#     counts[e] += 1
#   else:
#     counts[e] = 1

# d_sorted_by_value = OrderedDict(sorted(counts.items(), key=lambda x: x[1], reverse=True))

# for k, v in d_sorted_by_value.items():
#   print "%s: %s" % (k, v)

# -------

#RANDOM STUFF vvvvvv

# for e in ents:
#   #print(e.label, e.label_, ' '.join(t.orth_ for t in e))
#   print type(' '.join(t.orth_ for t in e))


# counts = {}

# counts = doc.count_by(ents.orth_)
# print counts


# import code
# code.interact(local=locals())
