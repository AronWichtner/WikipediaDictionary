import requests
from bs4 import BeautifulSoup
from googlesearch import search

userInput = input("Enter: ")
for i in search(userInput + "Wikipedia", tld='com', lang='en', num=1, start=0, stop=1, pause=2.0):
    URL = i

headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
request = requests.get(URL, headers)
content = request.content
soup = BeautifulSoup(content, "html.parser")
body = soup.find("body")

divcontent = body.find("div", {"class": "mw-body"})
divbodycontent = divcontent.find("div", {"id": "bodyContent"})
divbodycontenttext = divbodycontent.find("div", {"id": "mw-content-text"})
pfrombodycontenttext = divbodycontenttext.find_all("p")

for i in range(10):
    text = pfrombodycontenttext[i].text
    if len(text) > 20:
        finalText = text
        break
print(finalText)
