import hashlib

def hashid(did):
    return hashlib.sha1(did).hexdigest()

# need some error handling...
def mergeNodeInfo(nid, odata, ndata, graph):
    res = dict(odata)
    res["nodeid"] = nid
    if "outedges" not in res:
        res["outedges"] = []
    if "inedges" not in res:
        res["inedges"] = []
    for k in ndata:
        if k != "outedges" and k!= "inedges" and k!= "edges":
            if k in res:
                if isinstance(res[k], list):
                    if isinstance(ndata[k], list):
                        res[k].extend(ndata[k])
                    else:
                        res[k].append(ndata[k])
                else:
                    res[k] = ndata[k]
            else:
                res[k] = ndata[k]
    # check if multi and avoid creating multiple edges if not
    # weight inc...
    print(" in ndata")
    print(ndata)
    if "edges" in ndata:
        for e in ndata["edges"]:
            if validateEdge(e, graph):
                res["outedges"].append(e)
                res["inedges"].append(e)
    if "outedges" in ndata:
        for e in ndata["outedges"]:
            if validateOutedge(e, graph):
                res["outedges"].append(e)
    if "inedges" in ndata:
        for e in ndata["inedges"]:
            if validateInedge(e, graph):
                res["inedges"].append(e)
    return res

def validateEdge(e, graph):
    return True

def validateOutedge(e, graph):
    return True

def validateInedge(e, graph):
    return True

# again, should avoid duplicates... especially when non multi
def otherNodeUpdates(cid, data, graph):
    ret = {}
    if "edges" in data:
        for e in data["edges"]:
            nid = e[0]
            ne = list(e)
            ne[0] = cid
            if nid in ret:
                ret[nid]["outedges"].append(e)
                ret[nid]["inedges"].append(e)                
            else:
                ret[nid] = {"outedges": [e], "inedges": [e]}
    if "outedges" in data:
        for e in data["outedges"]:
            nid = e[0]
            ne = list(e)
            ne[0] = cid
            if graph["labelled"]:
                nid = e[1]
                ne[0] = e[1]
                ne[1] = e[0]
                ne[0] = cid
            if nid in ret:
                ret[nid]["outedges"].append(ne)
            else:
                ret[nid] = {"outedges": [], "inedges": [ne]}
    if "inedges" in data:
        for e in data["inedges"]:
            nid = e[0]
            ne = list(e)
            ne[0] = cid
            if graph["labelled"]:
                ne[0] = e[1]
                ne[1] = e[0]
                ne[1] = cid
            if nid in ret:
                ret[nid]["inedges"].append(ne)
            else:
                ret[nid] = {"outedges": [ne], "inedges": []}
    return ret
