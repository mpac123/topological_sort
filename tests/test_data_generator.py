from topological_sort import data_generator
import pytest


@pytest.mark.parametrize("size", [0, 1, 2, 5, 10, 50, 100, 1000, 5000, 10000, 64313, 100000, 1000000])
def test_generate_graph(size):
    graph = data_generator.generate_graph(size)
    print("graph", graph)
    cnt = 0
    for adjacent_Vs in graph.values():
        cnt += len(adjacent_Vs) + 1
    assert cnt == size
