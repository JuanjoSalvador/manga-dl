from bs4 import BeautifulSoup
import requests
from urllib import request

def getNumberOfPages(url):
    request = requests.get(url)
    content = BeautifulSoup(request.text, 'html.parser')

    pages = content.select('option')

    return len(pages)

def getPage(url, page):
    r = requests.get(url)
    bs = BeautifulSoup(r.text, 'html.parser')

    pages = bs.findAll('img')

    try:
        request.urlretrieve(pages[3].get('src'), "{}.jpg".format(page))
    except Exception as e:
        print("Error! {}".format(e))

def getChapter(url):
    for page in range(1, getNumberOfPages(url) + 1):
        if page == 1:
            getPage("{}".format(url), "1")
        else:
            getPage("{}/{}".format(url, page), page)

    
    
    
