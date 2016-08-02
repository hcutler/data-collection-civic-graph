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


# Print all entity names
print entity_names

# Print unique entity names
unique_en = set(entity_names)

print len(unique_en)
# Result: 9452

for en in unique_en:
  print en + ','

  # #write entities to text file
  # with open('unique_en_all.txt', 'wb') as f:
  #   writer = csv.writer(f)
  #   writer.writerows(en)


# Word token analysis
text = nltk.Text(tokens)

# text.concordance("keyword") searches text for all occurences of keyword.
# Can parse other sources for instances of people, organizations, names, etc.
text.concordance("money", lines=all)

# Examine the contexts that are shared by two or more words
text.common_contexts(["kw1", "kw2"])

# Example:
text.common_contexts(["Facebook", "Microsoft"])

# Result:
# ,_, (_) like_, between_and ,_announced ._also of_, and_have ._, for_,
# with_that with_itself ,_will at_, that_'s ._ceo through_'s for_.
# ''_also as_and


# Computing with Language: Simple Statistics

vocab = set(text)
print len(vocab)
# Result:
# 119591

fdist1 = nltk.FreqDist(text)
print(fdist1)
# Result:
# <FreqDist with 29267 samples and 451860 outcomes>

# Cumulative frequency plot for 50 most used words (Plot doesn't display!)
# fdist1.plot(50, cumulative=True)

print fdist1.most_common(100)
# Result:
# [(u',', 22952), (u'the', 19793), (u'.', 15499), (u'to', 11626), (u'of', 11130), (u'and', 10391), (u'a', 8217), (u'in', 6484), (u'that', 5363), (u'for', 5299), (u'is', 4477), (u'on', 3526), (u':', 2957), (u'with', 2506), (u'The', 2341), (u'are', 2157), (u'it', 2041), (u'as', 2010), (u'by', 1908), (u'be', 1809), (u'from', 1647), (u'at', 1633), (u'has', 1620), (u'have', 1586), (u')', 1573), (u'(', 1559), (u'their', 1533), (u'this', 1530), (u'more', 1525), (u'an', 1503), (u'we', 1458), (u'was', 1430), (u'about', 1366), (u'they', 1265), (u'or', 1265), (u'not', 1226), (u'people', 1184), (u'will', 1176), (u'its', 1161), (u'civic', 1139), (u'can', 1137), (u'I', 1133), (u'tech', 1086), (u'how', 1013), (u'reports', 987), (u'new', 979), (u'who', 977), (u'data', 931), (u'government', 925), (u'New', 886), (u'but', 885), (u'you', 881), (u'which', 877), (u'?', 866), (u'our', 822), (u'like', 814), (u'out', 797), (u'he', 781), (u'one', 767), (u'what', 739), (u'his', 734), (u'than', 729), (u'were', 728), (u'all', 718), (u'public', 711), (u'up', 654), (u'In', 648), (u'other', 645), (u'been', 628), (u'technology', 627), (u'would', 621), (u'This', 611), (u'York', 602), (u'also', 592), (u'debate', 587), (u'media', 577), (u'campaign', 568), (u'some', 562), (u'them', 557), (u'do', 552), (u'work', 552), (u'By', 549), (u'into', 535), (u'just', 533), (u'Civic', 532), (u'if', 531), (u'social', 529), (u'said', 504), (u'Facebook', 503), (u'there', 492), (u'political', 492), (u'had', 491), (u'We', 485), (u'open', 485), (u'when', 479), (u'Post', 475), (u'so', 470), (u'where', 463), (u'make', 456), (u'most', 444)]
# print len(sorted(w for w in set(text) if len(w) > 7 and fdist1[w] > 7))
# Result:
# 1828

# Collocations and Bigrams
# collocation is a sequence of words that occur together unusually often

#Example:
print text.collocations()

# Result:
# New York; civic tech; First Post; York Times; social media; Civic
# Hall; Jessica McKenzie; Bernie Sanders; 2015 First; White House;
# Personal Democracy; open data; San Francisco; Donald Trump; Democracy
# Forum; Hillary Clinton; United States; 2016 First; Silicon Valley;
# Washington Post

# Word Analysis
print sorted(w for w in set(text) if w.istitle())


# Pronoun Resolution: semantic role labeling (FIGRUE OUT HOW TO DO THIS!)

# Using a Tagger (Not working!)
tagged = nltk.pos_tag(text)
namedEnt = nltk.ne_chunk(tagged)
print namedEnt


# Funding analysis (Test)
tokens2 = []
with open("money.txt","r") as f:
  data2 = f.read().decode('utf8') # type 'string'
  tokens2 = nltk.word_tokenize(data2)

text2 = nltk.Text(tokens2)

print sorted(w for w in set(text2) if w.istitle() and len(w) > 3)
