#Script attempts to generate labels for training data associated with a given label

#spacy imports
import spacy
from spacy.attrs import ORTH, LIKE_URL, IS_OOV, NORM

#other imports
import operator
from operator import itemgetter
from collections import OrderedDict

# Label 1: 'Funding'

# read in training dataset
def label_funding():
  with open("funding_training.txt","r") as f:
    data = f.read() # type 'string'

  nlp = spacy.load("en")
  d = data.decode('utf-8')
  doc = nlp(d, tag=True) #tokens

  sentences = [sent.string.strip() for sent in doc.sents]
  # labels = [None] * len(sentences)
  labels = []

  for s in sentences:
    s = str(s)
    if 'money' in s or 'pay' in s or 'dollar' in s or 'currency' in s or 'give' in s or 'account' in s or 'exchange' in s or 'fund' in s:
      labels.append('Funding')
    else:
      labels.append('Not funding')

  print labels

# -----------------

# Label 2: 'Data'

# read in training dataset
def label_data():
  with open("data_training.txt","r") as f:
    data = f.read() # type 'string'

  nlp = spacy.load("en")
  d = data.decode('utf-8')
  doc = nlp(d, tag=True) #tokens

  sentences = [sent.string.strip() for sent in doc.sents]
  labels = []

  for s in sentences:
    s = str(s)
    if 'data' in s or 'provide access' in s or 'distribute' in s:
      labels.append('Data')
    else:
      labels.append('Not data')

  print labels

# # -----------------

# Label 3: 'Employment'

# read in training dataset
def label_employment():
  with open("employment_training.txt","r") as f:
    data = f.read() # type 'string'

  nlp = spacy.load("en")
  d = data.decode('utf-8')
  doc = nlp(d, tag=True) #tokens

  sentences = [sent.string.strip() for sent in doc.sents]
  labels = []

  for s in sentences:
    s = str(s)
    if 'job' in s or 'work' in s or 'employ' in s or 'delegate' in s or 'career' in s or 'delegation' in s or 'labor' in s or 'tenure' in s or 'opportunity' in s or 'experience' in s:
      labels.append('Employment')
    else:
      labels.append('Not employment')

  print labels

# # -----------------

# Label 4: 'Collaboration'

# read in training dataset
def label_collaboration():
  with open("collaboration_training.txt","r") as f:
    data = f.read() # type 'string'

  nlp = spacy.load("en")
  d = data.decode('utf-8')
  doc = nlp(d, tag=True) #tokens

  sentences = [sent.string.strip() for sent in doc.sents]
  labels = []

  for s in sentences:
    # s = str(s)
    if 'collaborate' in s or 'collaboration' in s or 'team' in s or 'together' in s or 'work together' in s or 'teamwork' in s or 'coproduce' in s or 'sponsor' in s or 'combine' in s or 'ally' in s or 'collude' in s or 'fraternize' in s or 'cofunction' in s or 'join' in s or 'partner' in s:
      labels.append('Collaboration')
    else:
      labels.append('Not collaboration')

  print labels

# # -----------------

# Label 5: 'Location'

# read in training dataset
def label_location():
  with open("location_training.txt","r") as f:
    data = f.read() # type 'string'

  nlp = spacy.load("en")
  d = data.decode('utf-8')
  doc = nlp(d, tag=True) #tokens

  sentences = [sent.string.strip() for sent in doc.sents]
  labels = []

  for s in sentences:
    # s = str(s)
    if 'location' in s or 'located' in s or 'within' in s or 'outside' in s or 'governed' in s or 'part' in s or 'city' in s or 'state' in s or 'country' in s or 'continent' in s or 'vicinity' in s or 'territory' in s:
      labels.append('Location')
    else:
      labels.append('Not location')

  print labels


def main():
  # label_funding()
  # label_data()
  label_employment()
  # label_collaboration()
  # label_location()


if __name__ == "__main__":
  main()

