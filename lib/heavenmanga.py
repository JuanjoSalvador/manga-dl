import os
import requests
from bs4 import BeautifulSoup
from urllib import request

def download(uri, page):
    r     = requests.get(uri)
    soup  = BeautifulSoup(r.text, 'html.parser')
    uri   = soup.find('img', {'id': 'p'}).get('src')

    try:
        request.urlretrieve(uri, "{}.jpg".format(page + 1))
    except Exception as e:
        print("Error! {}".format(e))

def getChapter(uri, **kwargs):
    r     = requests.get(uri)
    soup  = BeautifulSoup(r.text, 'html.parser')
    uri   = soup.find('img', {'id': 'p'}).get('src')
    pages = soup.findAll('option')
    title = soup.find('title').text.split(' - ')[0]

    dest  = kwargs.get('dest', title)

    if dest is not None:
        dest = "{}/{}".format(dest, title)

    if not os.path.exists(dest):
        os.makedirs(dest)

    os.chdir(dest)

    for index, page in enumerate(pages):
        download(page.get('value'), index)



 
