import requests
import ingraph

# this should really be a class
# constructed with ingraph server and graphid,
# and the other things.
# Test if graph exists and exception if not

class InGraph:

    ig_url = None
    es_url = None
    graphid = None
    
    def __init__(self, graphid, ig_url=None, es_url=None):
        self.graphid = graphid
        self.ig_url = ig_url
        self.es_url = es_url

    
    def createGraph(self, directed=True, labelled=False, weighted=False, multi=False):
        return True


    def updateNode(self, nid, nodedata):
        return True
