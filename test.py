# list graphs
curl http://127.0.0.1:6060/

# create graph
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:6060/test_graph -d '{"directed": 1, "multigraph": 1, "weighted": 1, "labelled": 1}'



