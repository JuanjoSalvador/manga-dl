from lib import submanga as sm
import sys

VERSION = "0.1"

if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            sm.getChapter(sys.argv[1])
        else:
            print("\nWelcome to manga-dl {}. Download manga from many websites!".format(VERSION))
            print("\nSUPPORTED WEBSITES\n\n - Submanga")
            print("\nUSAGE\n\nmanga-dl [URL]\n")
    except KeyboardInterrupt:
        print("\nCanceled. Goodbye!")