from bs4 import BeautifulSoup
from urllib import request
import requests
import os

def _getInfo(url):
    request = requests.get(url)
    content = BeautifulSoup(request.text, 'html.parser')

    manga = {}

    info = content.find('td', {'class': 'l'}).findAll('a')

    manga["title"]  = info[2].text
    manga["pages"]  = len(content.select('option'))
    manga["chapter"] = info[3].text
    manga["fansub"] = info[1].text

    return manga

def _download(url, page):
    r = requests.get(url)
    bs = BeautifulSoup(r.text, 'html.parser')

    pages = bs.findAll('img')

    try:
        request.urlretrieve(pages[3].get('src'), "{}.jpg".format(page))
    except Exception as e:
        print("Error! {}".format(e))

def getChapter(url, **kwargs):

    info = _getInfo(url)
    
    dest = kwargs.get('dest', None)

    if dest is None:
        dest = ("{}, chapter {}".format(info["title"], info["chapter"]))

    if not os.path.exists(dest):
        os.makedirs(dest)
    else:
        print("Destination directory doesn't exist!")
        exit()

    os.chdir(dest)

    for page in range(1, info["pages"] + 1):
        print("Downloading '{} - {}'. Page {} of {}".format(info["title"], info["chapter"], page, info["pages"]))
        if page == 1:
            _download("{}".format(url), "1")
        else:
            _download("{}/{}".format(url, page), page)