import requests
import threading
import queue
import argparse
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
    args = InitializeArgparser()
    firstUrl = args.startUrl
    goalUrl = args.goalUrl

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
    threadQueue = queue.Queue()
    
    q.put(rootNode)
    found = False
    resultNode = None
    currentLayer = 0
    while not found and q.qsize != 0:
        currentNode = q.get()
        #For each url, create a node. Check to see if it is the goal page
        #If it is, stop. If not, add it to the queue and add the url to checked
        #urls

        #If quiet was not requested, output a message when a new layer has been
        #reached
        if not args.quiet:
            if currentNode.layer != currentLayer:
                print("Now scanning layer: " +str( currentNode.layer))
                currentLayer = currentNode.layer

        for wikiUrl in currentNode.childUrls:
            n = UrlToWikiNode(wikiUrl,currentNode)
            if args.verbose:
                print("Current Parent: " + currentNode.title + ". Scanning " + n.title)
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
    r = requests.get(url)
    p = WikiParser()
    p.feed(r.text)
    return WikiNode(p.getTitle(),p.getUrl(),p.getLinkedWikis(True,True),parent)

def InitializeArgparser():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("startUrl",help="Enter a starting url.")
    argparser.add_argument("goalUrl",help="Enter a goal url.")
    argparser.add_argument("-q","--quiet",help="Run in quiet mode",action="store_true")
    argparser.add_argument("-v","--verbose",help="Run in verbose mode",action="store_true")
    args = argparser.parse_args()
    return args

if __name__ == "__main__":
     Main()

