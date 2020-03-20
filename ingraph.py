import hashlib
import requests
import json

es_base = 'http://localhost:9200/'
graph_index = 'ingraph_graphs'

# elasticsearch cache - get_doc and update doc to work together

def get_doc(index, id):    
    r=requests.get(es_base+index+'/_doc/'+id)
    return r

def update_doc(index, id, obj):    
    r=requests.put(es_base+index+'/_doc/'+id, json=obj)
    return r

def delete_doc(index, id):    
    r=requests.delete(es_base+index+'/_doc/'+id)
    return r

def search_doc(index, q=None):    
    if q != None:
        r=requests.get(es_base+index+'/_search?q='+q)
    else:
        r=requests.get(es_base+index+'/_search')        
    return r

def hashid(did):
    return hashlib.sha1(did).hexdigest()

def list_graphs():
    result = []
    r = search_doc('ingraph_graphs')
    if r.status_code != 200:
        return result
    data = json.loads(r.text)
    if "hits" in data and "hits" in data["hits"]:
        for hit in data["hits"]["hits"]:
            if "_source" in hit:
                result.append(hit["_source"])
    return result

def graph_exists(graphid):
    r = get_doc("ingraph_graphs", hashid(graphid))
    return r.status_code == 200

def get_graph(graphid):
    r = get_doc("ingraph_graphs", hashid(graphid))
    if r.status_code == 200 and "_source" in r.json():
        return r.json()["_source"]
    return {}

def delete_graph(gid):
    hgid=hashid(gid)
    r=requests.delete(es_base+hgid)
    if r.status_code != 200:        
        return False
    r=delete_doc('ingraph_graphs', hgid)
    if r.status_code != 200:        
        return False
    return True

def create_graph(gid, directed=True, multi=False, labelled=False, weighted=False):
    hgid=hashid(gid)
    r=requests.put(es_base+hgid)
    if r.status_code != 200:
        return {"error": "failed to create index"}
    if graph_exists(gid):
        return {"error": "graph already exists"}
    r=update_doc(graph_index,hgid,{'label': gid, 'gid': hgid, 'directed':directed, 'multi': multi, 'labelled': labelled, 'weighted': weighted})    
    if r.status_code != 200:
        return {"error": "failed to create graph"}
    return {"success": "graph created"}

