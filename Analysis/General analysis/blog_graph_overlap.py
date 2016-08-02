import json
import pprint


pp = pprint.PrettyPrinter(indent=4)

graph = []
blog = []

b_not_g = []
g_not_b = []
both = []

myText = ""
with open("cg_entities.csv", "r") as file1:  
  lis_1=[line for line in file1]        # create a list of lists

  for i in lis_1:
    graph.append(i)


with open("blog_entities.csv", "r") as file2:
  lis_2 =  [line for line in file2]

  for j in lis_2:
    blog.append(j)

# for g in graph:
#   for b in blog:
both = set(graph).intersection(blog)
print both

