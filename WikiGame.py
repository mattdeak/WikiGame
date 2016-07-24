import requests
import threading
import queue
import WikiTree

#Constants
PROTOCOL = "http://"
LANGUAGE = "en"
BASE_URL = "wikipedia.org"
   


def Main():
    

    firstUrl = input("Enter starting Url: ")
    goalUrl = input("Enter finishing Url: ")
    try:
        r = requests.get(firstUrl)
    except:
        print("Error: That URL could not be reached")
        exit()

    root = WikiTree.WikiNode(firstUrl)
    tree = WikiTree.WikiTree(root)


    while q.empty == False and found == False:
        for url in urlChildren:
           
           if checkUrl(url) == True then:
                found = True
            else:


def createProperURL(url):
    return PROTOCOL + LANGUAGE + "." = BASE_URL + url


if __name__ == "__main__":
     Main()

