from bs4 import  BeautifulSoup
import requests
import re

search_term = input("What product do you want to search for ?")

url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="list_tool_pagination_text").strong

print(page_text)
pages = str(page_text).split("/")[-2].split(">")[-1][:-1]