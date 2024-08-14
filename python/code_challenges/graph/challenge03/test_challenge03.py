import pytest
from challenge03 import Graph  # Assuming the graph class is in challenge03.py

def test_strongly_connected_graph():
    g = Graph(5)
    edges = [[1, 2], [1, 0], [0, 4], [4, 3], [3, 2], [3, 1], [2, 1], [2, 4]]
    for u, v in edges:
        g.add_edge(u, v)  # Do not subtract 1 if input is already 0-based
    assert g.is_strongly_connected() == "Strongly connected"

def test_not_strongly_connected_graph():
    g = Graph(7)
    edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 4], [1, 7], [7, 3]]
    for u, v in edges:
        g.add_edge(u-1, v-1)  # Adjust if input is 1-based
    assert g.is_strongly_connected() == "Not strongly connected"

def test_single_vertex():
    g = Graph(1)
    assert g.is_strongly_connected() == "Strongly connected"

def test_two_vertices_connected():
    g = Graph(2)
    g.add_edge(0, 1)
    g.add_edge(1, 0)
    assert g.is_strongly_connected() == "Strongly connected"

def test_two_vertices_not_connected():
    g = Graph(2)
    g.add_edge(0, 1)
    assert g.is_strongly_connected() == "Not strongly connected"

def test_disconnected_graph():
    g = Graph(4)
    edges = [[0, 1], [1, 2], [2, 3]]
    for u, v in edges:
        g.add_edge(u, v)
    assert g.is_strongly_connected() == "Not strongly connected"

if __name__ == "__main__":
    pytest.main()
