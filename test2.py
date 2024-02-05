
from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

#tag = doc.find(["option"])d
#tag = doc.find_all(class_="btn-item")
#tags = doc.find_all(string=re.compile("\$.*"), limit = 1)
tags = doc.find_all("input", type="string")
# tag['color'] = 'blue'
for tag in tags:
    tag['placeholder'] = " I changed it "
   # print(tag.strip()) # strip() is used to clear all other element

with open("changed.html", "w") as file:
    file.write(str(doc))

