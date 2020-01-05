import os
import graphviz

def load_data_from_file(f):
    V_dict = {}
    for line in f.readlines():
        line = line.rstrip('\n').split(' ')
        if (len(line) != 2):
            raise Exception("Invalid input data")

        # make sure that the vertices are in the dictionary
        if not line[0] in V_dict:
            V_dict[line[0]] = []
        if not line[1] in V_dict:
            V_dict[line[1]] = []

        # add the edge to the dictionary
        V_dict[line[0]].append(line[1])

    return V_dict

def visualise_result(graph, sorted_vertices, out_file):
    dot = graphviz.Digraph(format='png')
    for i, V in enumerate(sorted_vertices):
        dot.node(str(V), '%s #%s' % (V, i))
    for V, adj_list in graph.items():
        for adj_V in adj_list:
            dot.edge(str(V), str(adj_V))
    dot.render(out_file, view=True)

