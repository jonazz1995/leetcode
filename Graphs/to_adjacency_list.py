'''
Converting edge list to adjacency list
'''

edges = {(0,1),(0,2),(0,3),(2,4)}

def make_graph(edges):
    graph = {}

    for a, b in edges:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)
    
    return graph

xx = make_graph(edges)