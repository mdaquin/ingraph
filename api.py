from flask import Flask, request
from flask_cors import CORS, cross_origin
import json

app = Flask('ingraph_api')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# ingraph.py module realising operations. Includes:
## indexcache module so that details of indices stay in cache
## nodecache module that temporary keeps any node being 

# POST /graphname: createindex - config:
#     directed(def)/undirected,
#     uni(def)/multi,
#     unlabelled(def)/labelled, 
#     edge unweighted(def)/weighted
#     nodes weighted/unweighted
@app.route('/<graphid>', methods=['POST'])
@cross_origin()
def create_graph(graphid):
    response_obj = {'error': 'function not yet implemented'}
    response = app.response_class(
        response=json.dumps(response_obj),
        status=200,
        mimetype='application/json'
    )
    return response
    
# GET /graphname/nodeid: - return all info and edges (with weights, labels and directions depending on graph type)
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

# GET /graphname/nodeid/inedges/: - return inedges if directed (as above) all edges otherwise
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

# GET /graphname/nodeid/outedges/: - return ouedges if directed, all edges otherwise
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
#    - weight of node if weighted.
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




