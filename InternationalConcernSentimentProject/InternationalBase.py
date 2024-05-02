import pandas as pd
import sklearn as sk

class Keywords:
    def __init__(self):
        self._keywords = {"Country":{},"Leader":{},"Events":{},"Issues":{},
                          "Emotions":{},"Opinion":{},"counter-Narrative":{},
                          }

    @property
    def keywords(self):
        return self._keywords
    
    @keywords.setter
    def keywordssetter(self,key,value):
        self._keywords[key] = value

    def updatekeywords(self,**kwargs):
        for k,v in kwargs.items():
            if k in self._keywords.keys():
                self.keywordssetter = k
            else:
                print("{}: Key Not Found".format(k))
                
def Main():
    words = Keywords()
    val ={"Country":{"America","Mexico"},"Leader":{"Biden","Obrador"}}
    words.keywords.update(val)
    val ={"evets":{"Opps","Nope"}}
    words.updatekeywords(**val)
    print(words._keywords)


if __name__ == "__main__":
    Main()