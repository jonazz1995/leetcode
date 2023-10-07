
def makeGraph(edges):
    graph = {}

    for a, b in edges:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph


def isValid(n, edges):
    if not n:
        return True
    
    visited = set()
    graph = makeGraph(edges)

    def dfs(node, prev):
        if node in visited:
            return False
        
        visited.add(node)

        for neighbour in graph[node]:
            if neighbour == prev:
                continue
            if not dfs(neighbour, node):
                return False
        return True

    return dfs(0, -1) and len(visited) == n

n = 5
edges = [[0, 1], [0, 2], [0, 3], [5, 4]]

print(isValid(n, edges))