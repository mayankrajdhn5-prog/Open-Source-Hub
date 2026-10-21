"""
Unit test suite verifying Dijkstra shortest path implementation.
"""
from algorithms.dijkstra import dijkstra

def test_dijkstra():
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }
    dist = dijkstra(graph, 'A')
    assert dist['D'] == 4
    assert dist['C'] == 3
