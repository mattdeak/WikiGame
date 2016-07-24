from html.parser import HTMLParser

class WikiParser(HTMLParser):
    
    def __init__(self):
        HTMLParser.__init__
        self._wikititle = ""
        self._linkedwikis = []
    
    def handle_starttag(self,tag,attrs):
        if tag == "a":

            for name,value in attrs:
                if name == "href":
                    try:
                        if (value[0:6] == "/wiki/" and "#" not in value and ":"
                        not in value):
                            self._linkedwikis.append(value)
                    except:
                        pass

        if tag == "h1":
            
            for name,value in attrs:
                if name=="firstHeading":
                    self._wikititle = value
        

    def getTitle():
        return self._wikititle

    def getLinkedWikis():
        return self._linkedwikis

