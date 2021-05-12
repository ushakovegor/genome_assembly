from queue import LifoQueue

def checker(graph, count_graph):
    for ktuple in count_graph:
        if count_graph[ktuple][0] < count_graph[ktuple][1]:
            left = ktuple
        elif count_graph[ktuple][0] > count_graph[ktuple][1]:
            right = ktuple
    print(left, right)
    return left

def find_euler_path(graph, count_graph):
    left = checker(graph, count_graph)
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
    print(res)
    genome = [res.pop()]

    for i in range(len(res) - 1, -1, -1):
        genome.append(res[i][-1])
    genome_string = ''.join(genome)
    return genome_string
