import requests
import json
import util

class InGraph:
        
    es_base = 'http://localhost:9200/'
    graph_index = 'ingraph_graphs'
    graphid = ""
    
    def __init__(self, graphid, es_url):
        self.graphid = graphid
        self.es_base = es_url

    # elasticsearch cache - get_doc and update doc to work together

    def get_doc(self, index, id):    
        r=requests.get(self.es_base+index+'/_doc/'+id)
        return r

    def update_doc(self, index, id, obj):    
        r=requests.put(self.es_base+index+'/_doc/'+id, json=obj)
        return r

    def delete_doc(self, index, id):    
        r=requests.delete(self.es_base+index+'/_doc/'+id)
        return r

    def search_doc(self, index, q=None):    
        if q != None:
            r=requests.get(self.es_base+index+'/_search?q='+q)
        else:
            r=requests.get(self.es_base+index+'/_search')        
        return r

    def list_graphs(self):
        result = []
        r = search_doc(self.graph_index)
        if r.status_code != 200:
            return result
        data = json.loads(r.text)
        if "hits" in data and "hits" in data["hits"]:
            for hit in data["hits"]["hits"]:
                if "_source" in hit:
                    result.append(hit["_source"])
        return result

    def graph_exists(self):
        r = self.get_doc(self.graph_index, util.hashid(self.graphid))
        return r.status_code == 200

    def get_info(self):
        r = self.get_doc(self.graph_index, util.hashid(self.graphid))
        if r.status_code == 200 and "_source" in r.json():
            return r.json()["_source"]
        return {}

    def delete_graph(self):
        hgid=util.hashid(self.graphid)
        r=requests.delete(self.es_base+hgid)
        if r.status_code != 200:        
            return False
        r=self.delete_doc(self.graph_index, hgid)
        if r.status_code != 200:        
            return False
        return True

    def create_graph(self, **kwargs):
        directed = kwargs.get("directed", True)
        labelled = kwargs.get("labelled", True)
        weighted = kwargs.get("weighted", False)
        multi = kwargs.get("multi", False)
        hgid=util.hashid(self.graphid)
        if self.graph_exists():
            return {"error": "graph already exists"}
        r=requests.put(self.es_base+hgid)
        r=self.update_doc(self.graph_index,hgid,{'label': self.graphid, 'gid': hgid, 'directed':directed, 'multi': multi, 'labelled': labelled, 'weighted': weighted})    
        if r.status_code != 201:
            return {"error": "failed to create graph"}
        return {"success": "graph created"}

    def update_node(self, nid, data):
        graph = self.get_info()
        odata = self.get_doc(util.hashid(self.graphid), util.hashid(nid))
        if odata.status_code != 200:
            odata = {}
        else:
            odata = json.loads(odata.text)
            if "_source" in odata:
                odata = odata["_source"]
        ndata = util.mergeNodeInfo(nid, odata, data, graph)
        r = self.update_doc(util.hashid(self.graphid), util.hashid(nid), ndata)
        anu = util.otherNodeUpdates(nid, data, graph)
        print(anu)
        for node in anu:
            oodata = self.get_doc(util.hashid(self.graphid), util.hashid(node))
            if oodata.status_code != 200:
                oodata = {}
            else:
                oodata = json.loads(oodata.text)
                if "_source" in oodata:
                    oodata = oodata["_source"]
            print("oodata")
            print(oodata)
            print("update")
            print(anu[node])            
            ondata = util.mergeNodeInfo(node, oodata, anu[node], graph)
            print("Result")
            print(ondata)
            self.update_doc(util.hashid(self.graphid), util.hashid(node), ondata)
        return {"success": "node created or updated"}
    
    def search(self, query=None):
        r = ""
        if query == None:
            r = self.search_doc(util.hashid(self.graphid))
        else:
            r = self.search_doc(util.hashid(self.graphid), q=query)
            # search with the query in the index
        # post process the list of results, mergin out and inedges if
        # undirected
        res = json.loads(r.text)
        ret = []
        for hit in res["hits"]["hits"]:
            if "_source" in hit:
                ret.append(hit["_source"])        
        return ret

    
