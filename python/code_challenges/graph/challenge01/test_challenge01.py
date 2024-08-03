import pytest
from challenge01 import Graph  # Assuming the Graph class is in a file named graph.py

@pytest.fixture
def example_graph():
    graph = Graph()
    edges = [
        ("A", "C"), ("A", "E"), ("A", "B"),
        ("C", "F"), ("E", "F"), ("B", "G"),
        ("F", "G"), ("F", "D"), ("D", "I"),
        ("G", "I"), ("I", "H"), ("H", "K")
    ]
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    return graph

def test_bfs(example_graph):
    start_value = "A"
    expected_output = ["A", "C", "E", "B", "F", "G", "D", "I", "H", "K"]
    assert example_graph.breadth_first_search(start_value) == expected_output

def test_bfs_single_node():
    graph = Graph()
    graph.add_edge("A", "A")  # Self-loop for single node
    start_value = "A"
    expected_output = ["A"]
    assert graph.breadth_first_search(start_value) == expected_output

def test_bfs_disconnected_graph():
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("C", "D")
    start_value = "A"
    expected_output = ["A", "B"]
    assert graph.breadth_first_search(start_value) == expected_output

    start_value = "C"
    expected_output = ["C", "D"]
    assert graph.breadth_first_search(start_value) == expected_output

def test_bfs_no_edges():
    graph = Graph()
    start_value = "A"
    expected_output = ["A"]
    assert graph.breadth_first_search(start_value) == expected_output

