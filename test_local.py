from ingraph.ingraph import InGraph
import time

graph = InGraph("test_local", "http://localhost:9200/")

print("delete graph")
print(graph.delete_graph())

print("create graph")
print(graph.create_graph(directed=True, labelled=True, multi=True))

print("node 1")
print(graph.update_node("node1", {"outedges":[["p1", "node2"], ["p2","node3"]], "label": "Node 1"}))

print("node 2")
print(graph.update_node("node2", {"inedges":[["node3", "p2"]], "label": "Node 2"}))

print("node 3")
print(graph.update_node("node3", {"outedges":[["p3", "node3"]], "label": "Node 3"}))

time.sleep(5)

print("search")
print(graph.search())



