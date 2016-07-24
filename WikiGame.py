import requests
import threading
import queue
from WikiHTMLParser import WikiParser

class WikiNode:
    def __init__(self,title,url,childUrls=[],parent=None):
        self.url = url
        self.title = title
        self.parent = parent
        self.childUrls = childUrls
        self.children = []
        self.layer = self._getLayer()

    def printBranch(self):
        if self.parent is None:
            print(self.title,'')
        else:
            self.parent.printBranch()
            print(" ---> " + self.title,'')

    def _getLayer(self):
        if self.parent is None:
            return 1;
        else:
            return 1 + self.parent._getLayer()

    def addChild(self,childNode):
        self.children.append(childNode)

    def __eq__(self,otherNode):
        if self.url == otherNode.url or self.title == otherNode.title:
            return True
        else:
            return False
def Main():
    

    checkedNodes = []
    #Get user urls. 
    #TODO: Switch to argparse for a command line interface
    firstUrl = input("Enter starting Url: ")
    goalUrl = input("Enter finishing Url: ")
    try:
        rootNode = UrlToWikiNode(firstUrl)
        goalNode = UrlToWikiNode(goalUrl)
    except:
        print("Error: There was a problem with one of your URLs")
        exit()
    
    #ensure that 
    checkedNodes.append(rootNode)
    #Start a queue for nodes
    q = queue.Queue()
    q.put(rootNode)
    found = False
    resultNode = None
    while not found and q.qsize != 0:
        currentNode = q.get()
        print("Testing Layer" + str(currentNode.layer))
        #For each url, create a node. Check to see if it is the goal page
        #If it is, stop. If not, add it to the queue and add the url to checked
        #urls
        for wikiUrl in currentNode.childUrls:
            n = UrlToWikiNode(wikiUrl,currentNode)
            print(n.title + ": " + n.url)
            print(goalNode.title + ": " + goalNode.url)
            if n == goalNode:
                found = True
                resultNode = n
                break
            else:
                if n not in checkedNodes:
                    q.put(n)
                    currentNode.addChild(n)

    if not resultNode is None:
        print("Shortest Number of Clicks: " + str(resultNode.layer))
        resultNode.printBranch()
    else:
        print('No path found.')


#Creates a WikiNode from a Wikipedia URL
#TODO: Validate the given url
def UrlToWikiNode(url,parent=None):
    print("Converting: " + url + " to node.")
    r = requests.get(url)
    p = WikiParser()
    p.feed(r.text)
    return WikiNode(p.getTitle(),p.getUrl(),p.getLinkedWikis(True,True),parent)

if __name__ == "__main__":
     Main()

