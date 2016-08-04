from html.parser import HTMLParser

class WikiParser(HTMLParser):
    #Constructor
    def __init__(self):
        super(WikiParser,self).__init__() 
        self._wikititle = ""
        self._linkedwikis = []
        self._url = ""
        self._handlingName = False
    
    #Start Tag Handler
    def handle_starttag(self,tag,attrs):
        self._lasttag = tag
       #if this is a link
        if tag == "a":
            #If it's a link, make sure it's a wiki link and pass it to linked
            #wikis

            for name,value in attrs:
                if name == "href":
                    try:
                        if (value[0:6] == "/wiki/" and "#" not in value and ":" not in value):
                            self._linkedwikis.append(value)
                    except:
                        pass
        #If it's a link, search for the canonical tag as that has the current
        #URL
        elif tag == "link":

            for name,value in attrs:
                if value == "canonical":
                    self._url = attrs[1][1]

        if tag == "h1":
            
            for name,value in attrs:
                if value == "firstHeading":
                    self._handlingName = True
    
    #Set the title when the flag is true
    def handle_data(self,data):
        if self._handlingName:
            self._wikititle = data
            self._handlingName = False     
    

    def getTitle(self):
        return self._wikititle

    def getUrl(self):
        return self._url

    def getLinkedWikis(self,unique=False,fullUrls=False):
       
        BASE_URL = "http://en.wikipedia.org"
        wikiUrls = self._linkedwikis
        resultWikis = []
        if fullUrls:
            for wiki in wikiUrls:
                resultWikis.append(BASE_URL + wiki)

            wikiUrls = resultWikis
        
        if unique == False:
            return wikiUrls
        else:
            #Return a version of linked wikis with duplicates removed
            duplicateFree = []
            for wiki in wikiUrls:
                if wiki not in duplicateFree:
                    duplicateFree.append(wiki)

            return duplicateFree

