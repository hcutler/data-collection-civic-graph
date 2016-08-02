import json
import pprint

pp = pprint.PrettyPrinter(indent=4)

graph = []
blog = []
both = []

with open("cg_entities.csv", "r") as file1:
  graph = file1.read().split('\n')

with open("blog_entities.csv", "r") as file2:  
  blog = file2.read().split('\n')

with open("both.csv", "r") as file3:
  both = file3.read().split('\n')

blog_set = set(blog)
both_set = set(both)

bNOTg = list(blog_set - both_set)

# print "\n# of entities extracted from blog content that are not in Civic Graph: \n", len(bNOTg), "\n"

# print "Entities extracted from blog content not in Civic Graph:"

# for x in bNOTg:
#   print x

with open("blog_not_graph.csv", "w") as f:
  for x in bNOTg:
    f.write(x + '\n')
