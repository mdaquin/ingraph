echo "list graphs"
curl http://127.0.0.1:6060/
echo ""

echo "create graph"
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:6060/co_graph -d '{"directed": 0, "multigraph": 0, "weighted": 1, "labelled": 0}'
echo ""

echo "get into on graph"
curl http://127.0.0.1:6060/co_graph
echo ""

