import requests
import threading
import queue
def Main():
    PROTOCOL = "http://"
    LANGUAGE = "en"
    BASE_URL = "wikipedia.org"
    
    firstUrl = input("Enter starting Url: ")
    goalUrl = input("Enter finishing Url: ")
    try:
        r = requests.get(firstUrl)
    except:
        print("Error: That URL could not be reached")
        exit()

    q = queue.Queue
    q.put(firstUrl)
    while q.empty == False and found == False:
        nextUrl = q.get()
        urlChildren = getChildUrls(url)
        for url in urlChildren:
            if checkUrl(url) == True then:
                found = True
            else:
                q.put(url)


def checkUrl():




def getChildUrls(url):
    childUrls = []
    r = requests.get(url)
    content = r.text.split('"')
    for url in content:
        if (url[0:6] == "/wiki/" and ":" not in url and url not in childUrls:
            childUrls.append(url)

    return childUrls


if __name__ == "__main__":
    Main()

