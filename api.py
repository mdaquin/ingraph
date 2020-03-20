from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
import ingraph

app = Flask('ingraph_api')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
@cross_origin()
def get_info():
    response_obj = {'system': 'ingraph', 'version':0.1, 'graphs': ingraph.list_graphs()}    
    response = app.response_class(
        response=json.dumps(response_obj),
        status=200,
        mimetype='application/json'
    )
    return response
    
@app.route('/<graphid>', methods=['POST'])
@cross_origin()
def create_graph(graphid):
    response_obj = {'error': 'something went wrong'}
    if ingraph.graph_exists(graphid):
        response_obj = {'error': 'graph already exists'}
        response = app.response_class(
            response=json.dumps(response_obj),
            status=400,
            mimetype='application/json'
        )
        return response
    data = request.get_json(force=True)
    print(data)
    directed = True
    if "directed" in data and data["directed"]==0:
        directed = False
    multi = False
    if "multigraph" in data and data["multigraph"]==1:
        multi=True
    labelled = False
    if "labelled" in data and data["labelled"]==1:
        labelled = True
    weighted = False
    if "weighted" in data and data["weighted"]==1:
        weighted = True
    r = ingraph.create_graph(graphid, directed, multi, labelled, weighted)
    response = app.response_class(
        response=json.dumps(r),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/<graphid>', methods=['GET'])
@cross_origin()
def get_graph(graphid):
    response_obj = {'error': 'graph does not exist or is not available'}
    res = ingraph.get_graph(graphid)
    if res != {}:
        response_obj = res
    response = app.response_class(
        response=json.dumps(response_obj),
        status=200,
        mimetype='application/json'
    )
    return response

# GET /graphname/nodeid: - return all info and edges
# (with weights, labels and directions depending on graph type)
@app.route('/<graphid>/<nodeid>', methods=['GET'])
@cross_origin()
def get_node(graphid, nodeid):
    response_obj = {'error': 'function not yet implemented'}
    response = app.response_class(
        response=json.dumps(response_obj),
        status=200,
        mimetype='application/json'
    )
    return response

# GET /graphname/nodeid/inedges/: -
# return inedges if directed (as above) all edges otherwise
@app.route('/<graphid>/<nodeid>/inedges', methods=['GET'])
@cross_origin()
def get_inedges(graphid, nodeid):
    response_obj = {'error': 'function not yet implemented'}
    response = app.response_class(
        response=json.dumps(response_obj),
        status=200,
        mimetype='application/json'
    )
    return response

# GET /graphname/nodeid/outedges/: -
# return ouedges if directed, all edges otherwise
@app.route('/<graphid>/<nodeid>/outedges', methods=['GET'])
@cross_origin()
def get_outedges(graphid, nodeid):
    response_obj = {'error': 'function not yet implemented'}
    response = app.response_class(
        response=json.dumps(response_obj),
        status=200,
        mimetype='application/json'
    )
    return response

# POST /graphname/nodeid: - object with
#    - edges: if undirected graph - array of objects including id of destination obj, and if relevant, weight (numerical), label (anything)
#    - inedges: same if directed
#    - outedges: same if directed
#    - label of node
#    - weight of node if weighted or weight_inc for increment
#    any other attribute: part of the node info
# Actually index in the same way but also update the origin/destination of in/outedges (or edges if undirected) as well. Can take time.
# Dont replace the whole object, just add to the edges. If attributes already exist, replace. Otherwise, add.
@app.route('/<graphid>/<nodeid>', methods=['POST'])
@cross_origin()
def update_node(graphid, nodeid):
    response_obj = {'error': 'function not yet implemented'}
    response = app.response_class(
        response=json.dumps(response_obj),
        status=200,
        mimetype='application/json'
    )
    return response

# DELETE /graphname: delete the graph
@app.route('/<graphid>', methods=['DELETE'])
@cross_origin()
def delete_graph(graphid):
    response_obj = {'error': 'function not yet implemented'}
    response = app.response_class(
        response=json.dumps(response_obj),
        status=200,
        mimetype='application/json'
    )
    return response

# DELETE /graphname/nodeid: delete the node and all edges
@app.route('/<graphid>/<nodeid>', methods=['DELETE'])
@cross_origin()
def delete_node(graphid, nodeid):
    response_obj = {'error': 'function not yet implemented'}
    response = app.response_class(
        response=json.dumps(response_obj),
        status=200,
        mimetype='application/json'
    )
    return response

# DELETE /graphname/nodeid/edge: include info to identify edge to remove (destination, etc.) remove first one that matches
@app.route('/<graphid>/<nodeid>/edge', methods=['DELETE'])
@cross_origin()
def delete_edge(graphid, nodeid):
    response_obj = {'error': 'function not yet implemented'}
    response = app.response_class(
        response=json.dumps(response_obj),
        status=200,
        mimetype='application/json'
    )
    return response


app.run(port=6060)





