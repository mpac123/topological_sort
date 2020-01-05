import pytest
from topological_sort import algorithm

def test_emptyAdjacencyList():
    adj_dict = {}
    result = algorithm.topological_sort(adj_dict)
    assert result == []

def test_samplegraph():
    adj_dict = {'A': ['B', 'E','G'],
                'B': [],
                'C': ['G'],
                'D': ['B', 'F', 'G'],
                'E': ['D', 'G'],
                'F': [],
                'G': []}
    result = algorithm.topological_sort(adj_dict)
    assert result == ['A', 'C', 'E', 'D', 'B', 'F', 'G']

def test_samplegraphwithcycle():
    adj_dict = {'A': ['B', 'E','G'],
                'B': [],
                'C': ['G'],
                'D': ['B', 'F', 'G'],
                'E': ['D', 'G'],
                'F': [],
                'G': ['A']}
    with pytest.raises(Exception):
        algorithm.topological_sort(adj_dict)
