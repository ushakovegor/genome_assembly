from queue import LifoQueue

s_input = ['AGC', 'GCG', 'CGC', 'GCA']
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

for i in range(len(res) - 1, 0, -1):
    print(i)
    genome.append(res[i][-1])
genome_string = ''.join(genome)
print(genome_string)