from topological_sort import exceptions

def topological_sort(adjacencyDict):

    # create a dictionary to store indegrees of all vertices
    in_degree = {}
    # initialize the dictionary with 0 for each vertex
    for V in adjacencyDict:
        in_degree[V] = 0
    # count the incoming edges for every vertex
    for V, adjacents in adjacencyDict.items():
        for adjacentV in adjacents:
            in_degree[adjacentV] += 1

    # create a queue to which all the vertices with the indegree
    # equal 0 will be enqueues
    queue = []
    for V, degree in in_degree.items():
        if degree == 0:
            queue.append(V)

    # create a result list
    result = []

    # traverse the queue until it becomes empty
    while queue:
        # move the vertex from the queue to the result list
        dequeuedV = queue.pop(0)
        result.append(dequeuedV)
        # decrease the indegree for all the neighbours of the dequeued verted
        for V in adjacencyDict[dequeuedV]:
            in_degree[V] -= 1
            if in_degree[V] == 0:
                queue.append(V)

    # check if the result list length is equal to the input adjacency list length
    # otherwise, there must have been a cycle
    if (len(result) != len(adjacencyDict)):
        raise exceptions.CycleDetectedException("There is a cycle in the input graph.")

    return result
