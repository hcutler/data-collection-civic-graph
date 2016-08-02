import urllib
import time
import wikipedia #https://wikipedia.readthedocs.org/en/latest/code.html
from bs4 import BeautifulSoup

while True:
  topic = raw_input("\nPlease enter a topic: \n") #prompt user to enter topic

  print("\nFetching the Wikipedia page contents for '" + topic + "'... \n")
  url = urllib.urlopen("http://en.wikipedia.org/wiki/" + topic) #fetch page for topic

  title = wikipedia.page(topic) #store contents
  summary = title.summary #get summary
  categ = title.categories #get attributes
  links = title.links #get related links
  # sections = title.sections #get sections (not working)
  # suggestions = title.suggest #get suggested pages (not working)
  content = title.content #get page content

  def print_all_contents(t):
    print_summary(title)
    print_categories(title)
    print_links(title)
    # print_sections(title)
    # print_all_contents(title)

  def print_summary(t):
    print("\nSummary: \n") + summary + '\n'
    # print '\n' + str(section) + '\n' + summary + '\n'

  def print_categories(t):
    print "\nCategories associated with '" + topic + "':"
    for c in categ:
      print c
    print '\n'

  def print_links(t):
    print "\nPage links associated with '" + topic + "':"
    if len(links) == 0:
      print "\nNo links associated with '" + topic + "' \n"
    else:
      for l in links:
        print l
    print '\n'

  # this function is defined in the python-wikipedia API but is not working
  # def print_sections(t):
  #   print "\nSections associated with '" + topic + "':"

  #   if len(sections) == 0:
  #     print "No sections on '" + topic + "''s page\n"
  #   else:
  #     for s in sections:
  #       print s
  #     print '\n'

  def print_content(t):
    print "\nPage content of'" + topic + "''s wiki page: \n"
    print content

  def main():
    print_all_contents(title)


  if __name__ == "__main__":
      main()
