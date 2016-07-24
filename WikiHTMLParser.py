from html.parser import HTMLParser

class WikiParser(HTMLParser):
    
    def __init__(self):
        super(WikiParser,self).__init__() 
        self._wikititle = ""
        self._linkedwikis = []
        self._handlingName = False
    def handle_starttag(self,tag,attrs):
        self._lasttag = tag
        if tag == "a":

            for name,value in attrs:
                if name == "href":
                    try:
                        if (value[0:6] == "/wiki/" and "#" not in value and ":" not in value):
                            self._linkedwikis.append(value)
                    except:
                        pass

        if tag == "h1":
            
            for name,value in attrs:
                if value == "firstHeading":
                    self._handlingName = True
                    
    def handle_data(self,data):
        if self._handlingName:
            self._wikititle = data
            self._handlingName = False            

    def getTitle(self):
        return self._wikititle

    def getLinkedWikis(self):
        return self._linkedwikis

