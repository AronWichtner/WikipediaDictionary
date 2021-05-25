import requests
from bs4 import BeautifulSoup
from googlesearch import search


def webscrape(userinput):
    url = googleInput(userinput)
    soup = createSoup(url)
    text = findText(soup)
    return text


def googleInput(userinput):
    for i in search(userinput + "Wikipedia", tld='com', lang='en', num=1, start=0, stop=1, pause=2.0):
        url = i
        return url


def createSoup(url):
    headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
    request = requests.get(url, headers)
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    return soup


def findText(soup):
    allp = soup.find(id="mw-content-text").find_all("p")
    finaltext = controlparagraphs(allp)
    return finaltext


def controlparagraphs(allp):
    finaltext = "We could not find a proper definition. Please check your entry."
    for i in range(10):
        text = allp[i].text
        if len(text) > 20:
            finaltext = text
            break
        else:
            continue
    return finaltext
