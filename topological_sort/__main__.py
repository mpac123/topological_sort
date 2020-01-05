import click
import os
from topological_sort import utils, algorithm, data_generator, execution_time_stats

@ click.group()
def main():
    pass

def validate_path(ctx, param, value):
    if not os.path.exists(value):
        raise click.BadParameter("The given path does not exist")
    return value

@main.command()
@click.option('-p', '--path', callback=validate_path, required=True, help='Path to the file with input data')
@click.option('-o', '--output', help='Path where the rendered graph is to be saved')
def from_file(path, output):
    """Read graph from a given path and sort it"""
    result = []
    with open(path) as f:
        graph = utils.load_data_from_file(f)
        result = algorithm.topological_sort(graph)
    print(result)
    if (output != None):
        utils.visualise_result(graph, result, output)
        print("Graph has been rendered and saved in %s.png" % output)

@main.command()
@click.option('-n', type=int, default=100, 
    help='Complexity of the graph (|V| + |E|)', show_default=True)
@click.option('-o', '--output', help='Path where the rendered graph is to be saved')
def generated(n, output):
    """Generate graph of given complexity and sort it"""
    graph = data_generator.generate_graph(n)
    result = algorithm.topological_sort(graph)
    print("Generated graph:\n", graph)
    print("Sorted vertices:\n", result)
    if (output != None):
        utils.visualise_result(graph, result, output)
        print("Graph has been rendered and saved in %s.png" % output)

@main.command()
@click.option('-n', type=int, required=True, help="Initial complexity of the graph")
@click.option('-k', type=int, required=True, help="Number of steps")
@click.option('-s', '--step', type=int, required=True, help="How much complexity increases in every step")
@click.option('-r', type=int, required=True, help="Number of tests per step")
def statistics(n, k, step, r):
    """Compare execution time with teoretic complexity"""
    execution_time_stats.generate_report(n, k, step, r)