from bs4 import BeautifulSoup
from urllib import request
import requests
from tqdm import trange
import os

def getInfo(url):
    request = requests.get(url)
    content = BeautifulSoup(request.text, 'html.parser')

    manga = {}

    info = content.find('td', {'class': 'l'}).findAll('a')

    manga["title"]  = info[2].text
    manga["pages"]  = len(content.select('option'))
    manga["chapter"] = info[3].text
    manga["fansub"] = info[1].text

    return manga

def download(uri, page):
    try:
        request.urlretrieve(uri, "{}.jpg".format(page))
    except Exception as e:
        print("Error! {}".format(e))

def urlBuilder(uri, page):
    r = requests.get(uri)
    bs = BeautifulSoup(r.text, 'html.parser')
    page_uri = bs.findAll('img')[3].get('src')

    splited_uri = page_uri.split("/")
    
    return uri.replace(splited_uri[len(splited_uri) - 1], "{}.jpg".format(page))

def getChapter(url, **kwargs):

    info  = getInfo(url)    
    dest  = kwargs.get('dest', None)
    title = "{} {}".format(info["title"], info["chapter"])

    if dest is not None:
        dest = "{}/{}".format(dest, title)
    else:
        dest = title
        
    if not os.path.exists(dest):
        os.makedirs(dest)

    os.chdir(dest)

    for page in trange(info["pages"] + 1):
        download(urlBuilder(url, page), page)

    print("Download finished!")