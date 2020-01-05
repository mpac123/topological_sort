import functools
import timeit
from topological_sort import algorithm, data_generator
from tabulate import tabulate

def count_execution_time(graph, times):

    snippet_to_measure = functools.partial(algorithm.topological_sort, graph)

    elapsed_time = timeit.timeit(snippet_to_measure, number=times)/times
    return elapsed_time

def count_all_execution_times(graph_complexity, repetitions):
    time = 0
    for _ in range(repetitions):
        graph = data_generator.generate_graph(graph_complexity)
        time += count_execution_time(graph, 10)
    return time / repetitions

def generate_report(initial_problem_size, num_instances, step_size, repetitions_per_step):
    n_median = initial_problem_size + ((num_instances - 1) / 2) * step_size
    t_median = count_all_execution_times(n_median, repetitions_per_step)
    T_median = n_median

    c = t_median / T_median
    print("n\tt\t\t\tq(n)")
    for n in range(initial_problem_size, initial_problem_size + num_instances * step_size, step_size):
        t = count_all_execution_times(n, repetitions_per_step)
        T = n
        q = t / (c * T)
        print("%s\t%s\t%s" % (n, t * 1000, q))
