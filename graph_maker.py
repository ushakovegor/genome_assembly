def graph_maker(ktuples):
    suf_pref = set()
    for ktuple in ktuples:
        suf_pref.add(ktuple[:-1]) #prefix
        suf_pref.add(ktuple[1:]) #suffix

    # n = len(suf_pref) # count of nodes in de Bruijn graph
    graph = {}
    count_graph = {}
    for node in suf_pref:
        graph[node] = set()
        count_graph[node] = [0, 0]

    for ktuple in ktuples:
        graph[ktuple[:-1]].add(ktuple[1:])
        count_graph[ktuple[:-1]][1] += 1
        count_graph[ktuple[1:]][0] += 1
    return graph, count_graph
