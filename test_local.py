import ingraph.client

graph = InGraph("test_local", "http://localhost:9200")

graph.createGraph(directed=True, labelled=True, multi=True)

graph.updatenode("node1", {"outedges":[("p1", "node2"), ("p2","node3")], "label": "Node 1"})

graph.updatenode("node2", {"inedges":[("node3", "p2")], "label": "Node 2"})

graph.updatenode("node3", {"outedges":[("p3", "node3")], "label": "Node 3"})

