

class WikiNode:

    def __init__(self,url=None):
        self.url = url
        self.children = []

    def __eq__(self,other):
        if self.url == other.url:
            return True
        else:
            return False

    def countChildren(self,option=1):
        assert option == 1 or option == 2,"Option must be 1 or 2"
        if option == 2:
            return len(self.children)
        else:
            if self.children == []:
                return 1;
            childCount = 1
            for child in self.children:
                childCount = childCount + child.countChildren()
            return childCount
                
           

    def addChild(self,child):
        self.children.append(child)

class WikiTree:

    def __init__(self,root):
        self.root = root
        
    def getLevels(self):
        print("Placeholder")

    def getNodeList(self,level):
        currentlevel = 0
        done = False
        while currentlevel <> 0 or done:

    def printPath(self,url):
        print("Placeholder")

    def exists(self,searchUrl):
        if children == []:
            return False
        else:
            print("placeholder")

