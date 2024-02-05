from bs4 import BeautifulSoup
import requests
url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result,"html.parser")

tbody = doc.tbody
trs = tbody.contents

#print(list(trs[0].parent.name))
#print(list(trs[0].descendants))

prices = {}
for tr in trs[:10]:
    name, price = tr.contents[2:4]
    market = tr.contents[7:8]
    fixed_name = name.p.string
    fixed_price = price.a.string
    prices[fixed_price] = fixed_price
    #print(market)
print(fixed_name)
print(prices)