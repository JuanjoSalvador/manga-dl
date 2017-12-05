import sys
from urllib.parse import urlparse
from lib import submanga, tumangaonline, heavenmanga

VERSION = "0.1"

def main():
    uri    = sys.argv[1]
    dest   = sys.argv[2]
    site   = urlparse(uri).netloc.replace("www.", "")
    domain = site.split('.')[0]

    # Add here more sites!
    
    websites = {
        'submanga': submanga,
        'tumangaonline': tumangaonline,
        'heavenmanga': heavenmanga,
    }

    try:
        websites[domain].getChapter(uri, dest=dest)
    except AttributeError as ae:
        print(ae)
        print("Error: '{}' is not a valid URL!".format(uri))
    except KeyError:
        print("Ooops! Sorry, '{}' is not a valid URL or is not supported yet.".format(site))

if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            main()
        else:
            print("\nWelcome to manga-dl {}. Download manga from many websites!".format(VERSION))
            print("\nSUPPORTED WEBSITES\n\n - Submanga")
            print("\nUSAGE\n\n  manga-dl [URL]\n")
    except KeyboardInterrupt:
        print("\nCanceled. Goodbye!")