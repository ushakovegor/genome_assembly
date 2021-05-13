from queue import LifoQueue


def checks(graph, count_graph):
    '''
    Checks the graph for correctness and find the first k-1 - tuple of the genome

    Input:
        graph - the de Bruijn graph
        count_graph - graph with count of connections
    Output:
        left - the first k-1 - tuple of the genome
    '''
    n = 0
    for ktuple in count_graph:
        if count_graph[ktuple][0] < count_graph[ktuple][1]:
            left = ktuple
            n += 1
        elif count_graph[ktuple][0] > count_graph[ktuple][1]:
            right = ktuple
            n += 1
    if n != 2:
        raise ValueError
    return left


def find_euler_path(graph, count_graph):
    '''
    Find the Euler path in the de Bruijn graph

    Input:
        graph - the de Bruijn graph
        count_graph - graph with count of connections
    Output:
        genome_string - the result of genome assembly
    '''
    left = checks(graph, count_graph)
    stack = LifoQueue()
    stack.put(left)
    res = []
    while not stack.empty():
        v = stack.get()
        stack.put(v)
        if len(graph[v]) == 0:
            res.append(v)
            stack.get()
        else:
            stack.put(graph[v].pop())
    genome = [res.pop()]
    for i in range(len(res) - 1, -1, -1):
        genome.append(res[i][-1])
    genome_string = ''.join(genome)
    return genome_string
