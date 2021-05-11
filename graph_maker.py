s_input = ['AGC', 'GCT', 'CTA', 'TAA']
k = len(s_input[0]) #len of k-tuple
suf_pref = set()
for ktuple in s_input:
    suf_pref.add(ktuple[:-1]) #prefix
    suf_pref.add(ktuple[1:]) #suffix

n = len(suf_pref) # count of nodes in de Bruijn graph
graph = {}
count_graph = {}
for node in suf_pref:
    graph[node] = set()
    count_graph[node] = [0, 0]

for ktuple in s_input:
    graph[ktuple[:-1]].add(ktuple[1:])
    #obr_graph[ktuple[1:]].add(ktuple[:-1])
    count_graph[ktuple[:-1]][1] += 1
    count_graph[ktuple[1:]][0] += 1

print(graph)
print(count_graph)
'-----------------------------------------------------------'

for ktuple in count_graph:
    if count_graph[ktuple][0] < count_graph[ktuple][1]:
        left = ktuple
    elif count_graph[ktuple][0] > count_graph[ktuple][1]:
        right = ktuple
print(left, right)


graph[right].add(left)
print(graph)

