# Topological sort
Project for algorithms analysis course (AAL) in Warsaw University of Technology

Student: Marta Pacuszka

## Prepare environment
 - Create virtual environment: `python -m venv .venv`
 - Setup project: `pip install -e .`
 - Run unit tests: `pytest`

## Requirements
Graphs and obtained topological order can be visualised (using `-o/--output` option, details below). In order to do it [Graphviz](https://www.graphviz.org/download/) has to be installed on your machine.

## Run program
Usage:
```
topological_sort COMMAND [OPTIONS]
```

Program can be run with 3 different commands:

1. `from-file`: Read graph from a given path and sort it topologically.
    This command accepts the following options:
    ```
    -p, --path TEXT    Path to the file with input data  [required]
    -o, --output TEXT  Path where the rendered graph is to be saved
    ```
    The input file should contain pairs of vertices that create an edge, every pair in a seperate line. The order of vertices is important: the edge origins from the first vertex in the pair and enters the second vertex. The example file can be structured as follows:
    ```
    1 3
    3 2
    2 5
    ```
    If the output option is specified, the image in PNG format with graph will be rendered and saved.

2. `generated`: Generate graph of given complexity (defined as a sum of number of vertices and edges) and sort it topologically. This command accepts the following options:
    ```
    -n INTEGER         Complexity of the graph (|V| + |E|)  [default: 100]
    -o, --output TEXT  Path where the rendered graph is to be saved
    ```
    In the standard output both the generated graph and sorted vertices will be printed.
    Again, if the output option is specified, the image in PNG format with graph will be rendered and saved.

3. `statistics`: Run a series of test with generated graph of increasing complexity and compare to theoretic complecity (|V| + |E|). This command accepts the following options:
    ```
    -n INTEGER          Initial complexity of the graph  [required]
    -k INTEGER          Number of steps  [required]
    -s, --step INTEGER  How much complexity increases in every step  [required]
    -r INTEGER          Number of tests per step  [required]
    ```
    
## Project structure
Main module is `topological_sort`. The entry point is `__main__.py` file. The remaining files are:
 - `algorithm.py`: contains implementation of the topological sort algorithm. Kahn's algorithm has been chosen as it is easy to detect cycles using it.
 - `data_generator.py`: contains a function generating a graph of given complexity, defined as a sum of number of edges and vertices
 - `execution_time_stats.py`: functions for measuring the execution time 
 - `utils.py`: functions with common code used by the rest of the module